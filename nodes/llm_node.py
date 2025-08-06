import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from state import AgentState, NodeResult, ValidationResult

class LLMNode:
    """Node for calling Google Gemini LLM"""
    
    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-lite"):
        self.llm = ChatGoogleGenerativeAI(
            google_api_key=api_key,
            model=model_name,
            temperature=0.7
        )
    
    def validate_input(self, state: AgentState) -> ValidationResult:
        """Validate LLM input"""
        errors = []
        warnings = []
        
        prompt = state["parsed_input"].get("prompt")
        if not prompt or len(prompt.strip()) == 0:
            errors.append("Prompt cannot be empty")
        elif len(prompt) > 10000:
            warnings.append("Prompt is very long, response may be truncated")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    async def execute(self, state: AgentState) -> AgentState:
        """Execute LLM call"""
        start_time = time.time()
        
        try:
            # Validate input
            validation = self.validate_input(state)
            state["validation_results"]["llm"] = validation
            
            if not validation.is_valid:
                raise ValueError(f"Validation failed: {', '.join(validation.errors)}")
            
            # Prepare prompt
            prompt = state["parsed_input"]["prompt"]
            system_message = state["parsed_input"].get("system_message", "")
            
            if system_message:
                full_prompt = f"System: {system_message}\n\nUser: {prompt}"
            else:
                full_prompt = prompt
            
            # Execute LLM call
            message = HumanMessage(content=full_prompt)
            response = await self.llm.ainvoke([message])
            
            # Create result
            execution_time = time.time() - start_time
            result = NodeResult(
                success=True,
                data={
                    "prompt": prompt,
                    "response": response.content,
                    "model": "gemini-2.0-flash-lite",
                    "tokens_estimated": len(prompt.split()) + len(response.content.split())
                },
                execution_time=execution_time,
                context=state["execution_context"]
            )
            
            state["node_results"]["llm"] = result
            state["current_node"] = "output"
            
        except Exception as e:
            execution_time = time.time() - start_time
            result = NodeResult(
                success=False,
                error=str(e),
                execution_time=execution_time,
                context=state["execution_context"]
            )
            state["node_results"]["llm"] = result
            state["error_message"] = str(e)
        
        return state