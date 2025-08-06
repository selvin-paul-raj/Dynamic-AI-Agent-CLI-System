from typing import Any, Dict, List, Optional, TypedDict, Literal
from pydantic import BaseModel, Field
from enum import Enum

class FlowType(str, Enum):
    """Available flow types"""
    SEARCH = "search"
    LLM = "llm" 
    MATH = "math"

class NodeStatus(str, Enum):
    """Node execution status"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class ExecutionContext(BaseModel):
    """Shared execution context across nodes"""
    flow_id: str
    node_id: str
    timestamp: float
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ValidationResult(BaseModel):
    """Result of input validation"""
    is_valid: bool
    errors: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)

class NodeResult(BaseModel):
    """Standard result format for all nodes"""
    success: bool
    data: Any = None
    error: Optional[str] = None
    execution_time: float = 0.0
    context: Optional[ExecutionContext] = None

class AgentState(TypedDict):
    """Main state object that flows through the graph"""
    # Input processing
    user_input: str
    flow_type: FlowType
    parsed_input: Dict[str, Any]
    
    # Execution tracking
    current_node: str
    execution_context: ExecutionContext
    node_results: Dict[str, NodeResult]
    
    # Results
    final_output: Optional[str]
    error_message: Optional[str]
    
    # Routing and validation
    routing_decision: Dict[str, Any]
    validation_results: Dict[str, ValidationResult]