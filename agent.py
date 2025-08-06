import os
import yaml
import time
import uuid
from typing import Dict, Any, Optional, List
from pathlib import Path
from dotenv import load_dotenv

from langgraph.graph import StateGraph, END
from state import AgentState, FlowType, ExecutionContext, ValidationResult
from nodes import SearchNode, LLMNode, MathNode, OutputNode

class MultiFlowAgent:
    """Main agent orchestrator for handling multiple dynamic flows"""
    
    def __init__(self, config_path: str = "configs/flows.yaml"):
        load_dotenv()
        
        # Load configuration
        self.config = self._load_config(config_path)
        self.flows = self.config["flows"]
        self.routing_patterns = self.config.get("routing", {}).get("patterns", {})
        
        # Initialize nodes
        self.nodes = self._initialize_nodes()
        
        # Build graphs for each flow
        self.graphs = self._build_graphs()
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load YAML configuration"""
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML configuration: {e}")
    
    def _initialize_nodes(self) -> Dict[str, Any]:
        """Initialize all node instances"""
        nodes = {}
        
        # Get API keys
        google_api_key = os.getenv("GOOGLE_API_KEY")
        serper_api_key = os.getenv("SERPER_API_KEY")
        
        if not google_api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is required")
        if not serper_api_key:
            raise ValueError("SERPER_API_KEY environment variable is required")
        
        # Initialize nodes
        nodes["SearchNode"] = SearchNode(serper_api_key)
        nodes["LLMNode"] = LLMNode(google_api_key)
        nodes["MathNode"] = MathNode()
        nodes["OutputNode"] = OutputNode()
        
        return nodes
    
    def _build_graphs(self) -> Dict[str, StateGraph]:
        """Build LangGraph workflows for each flow"""
        graphs = {}
        
        for flow_name, flow_config in self.flows.items():
            graph = StateGraph(AgentState)
            
            # Add nodes to graph
            for node_config in flow_config["nodes"]:
                node_name = node_config["name"]
                node_type = node_config["type"]
                
                if node_type in self.nodes:
                    node_instance = self.nodes[node_type]
                    graph.add_node(node_name, node_instance.execute)
                else:
                    raise ValueError(f"Unknown node type: {node_type}")
            
            # Add edges
            for node_config in flow_config["nodes"]:
                node_name = node_config["name"]
                next_node = node_config.get("next")
                
                if next_node:
                    graph.add_edge(node_name, next_node)
                else:
                    graph.add_edge(node_name, END)
            
            # Set entry point (first node)
            first_node = flow_config["nodes"][0]["name"]
            graph.set_entry_point(first_node)
            
            graphs[flow_name] = graph.compile()
        
        return graphs
    
    def determine_flow(self, user_input: str, explicit_flow: Optional[str] = None) -> FlowType:
        """Determine which flow to use based on input or explicit specification"""
        if explicit_flow:
            try:
                return FlowType(explicit_flow.lower())
            except ValueError:
                raise ValueError(f"Unknown flow type: {explicit_flow}")
        
        # Auto-detect flow based on patterns
        user_input_lower = user_input.lower()
        
        for flow_type, patterns in self.routing_patterns.items():
            for pattern in patterns:
                if pattern.lower() in user_input_lower:
                    return FlowType(flow_type)
        
        # Default to LLM flow if no pattern matches
        return FlowType.LLM
    
    def parse_input(self, user_input: str, flow_type: FlowType) -> Dict[str, Any]:
        """Parse user input based on flow type"""
        if flow_type == FlowType.SEARCH:
            return self._parse_search_input(user_input)
        elif flow_type == FlowType.LLM:
            return self._parse_llm_input(user_input)
        elif flow_type == FlowType.MATH:
            return self._parse_math_input(user_input)
        else:
            raise ValueError(f"Unknown flow type: {flow_type}")
    
    def _parse_search_input(self, user_input: str) -> Dict[str, Any]:
        """Parse search-specific input"""
        # Extract query from common search patterns
        query = user_input
        for pattern in ["search for", "find information about", "look up", "google"]:
            if pattern in user_input.lower():
                query = user_input.lower().replace(pattern, "").strip()
                break
        
        return {
            "query": query,
            "num_results": 5
        }
    
    def _parse_llm_input(self, user_input: str) -> Dict[str, Any]:
        """Parse LLM-specific input"""
        return {
            "prompt": user_input,
            "system_message": "You are a helpful AI assistant."
        }
    
    def _parse_math_input(self, user_input: str) -> Dict[str, Any]:
        """Parse math-specific input"""
        import re
        
        user_input_clean = user_input.strip()
        
        # Try to parse simple arithmetic expressions like "2+3", "10-5", "4*6", "8/2"
        # Look for patterns like number operator number
        arithmetic_pattern = r'(\d+(?:\.\d+)?)\s*([+\-*/×÷])\s*(\d+(?:\.\d+)?)'
        arithmetic_match = re.search(arithmetic_pattern, user_input_clean)
        
        if arithmetic_match:
            num1, operator, num2 = arithmetic_match.groups()
            operands = [float(num1), float(num2)]
            
            # Map operators to operation names
            operator_map = {
                '+': 'add',
                '-': 'subtract', 
                '*': 'multiply',
                '/': 'divide',
                '×': 'multiply',
                '÷': 'divide'
            }
            operation = operator_map.get(operator, 'add')
            
        else:
            # Fallback to word-based detection
            user_input_lower = user_input.lower()
            
            # Detect operation by keywords
            operation = "add"  # default
            if any(word in user_input_lower for word in ["add", "plus", "+"]):
                operation = "add"
            elif any(word in user_input_lower for word in ["subtract", "minus", "-"]):
                operation = "subtract"
            elif any(word in user_input_lower for word in ["multiply", "times", "*", "×"]):
                operation = "multiply"
            elif any(word in user_input_lower for word in ["divide", "divided by", "/", "÷"]):
                operation = "divide"
            
            # Extract all positive numbers only (no negative signs)
            numbers = re.findall(r'\d+(?:\.\d+)?', user_input)
            operands = [float(n) for n in numbers if n]
            
            if len(operands) < 2:
                # Fallback: default numbers for demo
                operands = [10, 5]
        
        return {
            "operation": operation,
            "operands": operands
        }
    
    async def execute(
        self, 
        user_input: str, 
        flow_type: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Execute the agent with given input"""
        try:
            # Determine flow
            determined_flow = self.determine_flow(user_input, flow_type)
            
            # Parse input
            parsed_input = self.parse_input(user_input, determined_flow)
            
            # Create execution context
            context = ExecutionContext(
                flow_id=str(uuid.uuid4()),
                node_id="start",
                timestamp=time.time(),
                metadata=kwargs
            )
            
            # Initialize state
            initial_state: AgentState = {
                "user_input": user_input,
                "flow_type": determined_flow,
                "parsed_input": parsed_input,
                "current_node": "start",
                "execution_context": context,
                "node_results": {},
                "final_output": None,
                "error_message": None,
                "routing_decision": {"flow_type": determined_flow.value},
                "validation_results": {}
            }
            
            # Execute flow
            graph = self.graphs[determined_flow.value]
            result_state = await graph.ainvoke(initial_state)
            
            # Format response
            return {
                "success": result_state.get("error_message") is None,
                "output": result_state.get("final_output", "No output generated"),
                "flow_used": determined_flow.value,
                "execution_time": sum(
                    result.execution_time 
                    for result in result_state.get("node_results", {}).values()
                ),
                "node_results": {
                    name: {
                        "success": result.success,
                        "execution_time": result.execution_time,
                        "error": result.error
                    }
                    for name, result in result_state.get("node_results", {}).items()
                },
                "validation_results": result_state.get("validation_results", {}),
                "error": result_state.get("error_message")
            }
            
        except Exception as e:
            return {
                "success": False,
                "output": f"Agent execution failed: {str(e)}",
                "error": str(e),
                "flow_used": flow_type or "unknown"
            }
