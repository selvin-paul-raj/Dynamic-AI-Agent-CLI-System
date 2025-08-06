import time
from typing import Dict, Any
from state import AgentState, NodeResult

class OutputNode:
    """Shared node for formatting final output"""
    
    def __init__(self):
        self.formatters = {
            "search": self._format_search_output,
            "llm": self._format_llm_output,
            "math": self._format_math_output
        }
    
    async def execute(self, state: AgentState) -> AgentState:
        """Format and prepare final output"""
        start_time = time.time()
        
        try:
            flow_type = state["flow_type"]
            node_result = state["node_results"].get(flow_type.value)
            
            if not node_result:
                raise ValueError(f"No result found for flow type: {flow_type}")
            
            if not node_result.success:
                state["final_output"] = f"Error in {flow_type} operation: {node_result.error}"
            else:
                formatter = self.formatters.get(flow_type.value)
                if formatter:
                    state["final_output"] = formatter(node_result.data)
                else:
                    state["final_output"] = str(node_result.data)
            
            # Create output result
            execution_time = time.time() - start_time
            result = NodeResult(
                success=True,
                data=state["final_output"],
                execution_time=execution_time,
                context=state["execution_context"]
            )
            
            state["node_results"]["output"] = result
            
        except Exception as e:
            execution_time = time.time() - start_time
            result = NodeResult(
                success=False,
                error=str(e),
                execution_time=execution_time,
                context=state["execution_context"]
            )
            state["node_results"]["output"] = result
            state["final_output"] = f"Output formatting error: {str(e)}"
        
        return state
    
    def _format_search_output(self, data: Dict[str, Any]) -> str:
        """Format search results for display"""
        output = [f"🔍 Search Results for: '{data['query']}'"]
        output.append(f"Found {data['total_results']} results\n")
        
        for i, result in enumerate(data['results'], 1):
            output.append(f"{i}. {result['title']}")
            output.append(f"   {result['snippet']}")
            output.append(f"   🔗 {result['link']}\n")
        
        return "\n".join(output)
    
    def _format_llm_output(self, data: Dict[str, Any]) -> str:
        """Format LLM response for display"""
        output = ["🤖 AI Response:"]
        output.append("-" * 50)
        output.append(data['response'])
        output.append("-" * 50)
        output.append(f"Model: {data['model']} | Estimated tokens: {data['tokens_estimated']}")
        
        return "\n".join(output)
    
    def _format_math_output(self, data: Dict[str, Any]) -> str:
        """Format math result for display"""
        output = ["🧮 Mathematical Calculation:"]
        output.append(f"Operation: {data['operation'].title()}")
        output.append(f"Expression: {data['expression']}")
        output.append(f"Result: {data['result']}")
        
        return "\n".join(output)
