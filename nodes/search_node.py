import time
import httpx
from typing import Dict, Any
from state import AgentState, NodeResult, ExecutionContext, ValidationResult

class SearchNode:
    """Node for performing web searches using Serper API"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://google.serper.dev/search"
    
    def validate_input(self, state: AgentState) -> ValidationResult:
        """Validate search input"""
        errors = []
        warnings = []
        
        query = state["parsed_input"].get("query")
        if not query or len(query.strip()) == 0:
            errors.append("Search query cannot be empty")
        elif len(query) > 500:
            warnings.append("Query is very long, results may be limited")
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    async def execute(self, state: AgentState) -> AgentState:
        """Execute search operation"""
        start_time = time.time()
        
        try:
            # Validate input
            validation = self.validate_input(state)
            state["validation_results"]["search"] = validation
            
            if not validation.is_valid:
                raise ValueError(f"Validation failed: {', '.join(validation.errors)}")
            
            # Prepare search request
            query = state["parsed_input"]["query"]
            headers = {
                "X-API-KEY": self.api_key,
                "Content-Type": "application/json"
            }
            payload = {
                "q": query,
                "num": state["parsed_input"].get("num_results", 5)
            }
            
            # Execute search
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.base_url,
                    json=payload,
                    headers=headers,
                    timeout=30.0
                )
                response.raise_for_status()
                results = response.json()
            
            # Format results
            formatted_results = self._format_search_results(results)
            
            # Create result
            execution_time = time.time() - start_time
            result = NodeResult(
                success=True,
                data=formatted_results,
                execution_time=execution_time,
                context=state["execution_context"]
            )
            
            state["node_results"]["search"] = result
            state["current_node"] = "output"
            
        except Exception as e:
            execution_time = time.time() - start_time
            result = NodeResult(
                success=False,
                error=str(e),
                execution_time=execution_time,
                context=state["execution_context"]
            )
            state["node_results"]["search"] = result
            state["error_message"] = str(e)
        
        return state
    
    def _format_search_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Format search results for output"""
        organic = results.get("organic", [])
        formatted = {
            "query": results.get("searchParameters", {}).get("q", ""),
            "total_results": len(organic),
            "results": []
        }
        
        for item in organic[:5]:  # Top 5 results
            formatted["results"].append({
                "title": item.get("title", ""),
                "link": item.get("link", ""),
                "snippet": item.get("snippet", "")
            })
        
        return formatted
