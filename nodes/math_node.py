import time
import operator
from typing import Dict, Any, Callable
from state import AgentState, NodeResult, ValidationResult

class MathNode:
    """Node for mathematical operations"""
    
    def __init__(self):
        self.operations: Dict[str, Callable] = {
            "add": operator.add,
            "subtract": operator.sub,
            "multiply": operator.mul,
            "divide": operator.truediv,
            "power": operator.pow,
            "modulo": operator.mod
        }
    
    def validate_input(self, state: AgentState) -> ValidationResult:
        """Validate math input"""
        errors = []
        warnings = []
        
        parsed = state["parsed_input"]
        operation = parsed.get("operation")
        
        if not operation:
            errors.append("Operation is required")
        elif operation not in self.operations:
            errors.append(f"Unsupported operation: {operation}. Available: {list(self.operations.keys())}")
        
        # Validate operands
        operands = parsed.get("operands", [])
        if len(operands) < 2:
            errors.append("At least 2 operands are required")
        
        for i, operand in enumerate(operands):
            try:
                float(operand)
            except (ValueError, TypeError):
                errors.append(f"Operand {i+1} is not a valid number: {operand}")
        
        # Division by zero check
        if operation == "divide" and len(operands) >= 2:
            try:
                if float(operands[1]) == 0:
                    errors.append("Division by zero is not allowed")
            except (ValueError, TypeError):
                pass
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    async def execute(self, state: AgentState) -> AgentState:
        """Execute math operation"""
        start_time = time.time()
        
        try:
            # Validate input
            validation = self.validate_input(state)
            state["validation_results"]["math"] = validation
            
            if not validation.is_valid:
                raise ValueError(f"Validation failed: {', '.join(validation.errors)}")
            
            # Parse input
            operation = state["parsed_input"]["operation"]
            operands = [float(x) for x in state["parsed_input"]["operands"]]
            
            # Execute operation
            result_value = operands[0]
            for operand in operands[1:]:
                result_value = self.operations[operation](result_value, operand)
            
            # Create result
            execution_time = time.time() - start_time
            result = NodeResult(
                success=True,
                data={
                    "operation": operation,
                    "operands": operands,
                    "result": result_value,
                    "expression": self._format_expression(operation, operands, result_value)
                },
                execution_time=execution_time,
                context=state["execution_context"]
            )
            
            state["node_results"]["math"] = result
            state["current_node"] = "output"
            
        except Exception as e:
            execution_time = time.time() - start_time
            result = NodeResult(
                success=False,
                error=str(e),
                execution_time=execution_time,
                context=state["execution_context"]
            )
            state["node_results"]["math"] = result
            state["error_message"] = str(e)
        
        return state
    
    def _format_expression(self, operation: str, operands: list, result: float) -> str:
        """Format mathematical expression for display"""
        symbols = {
            "add": "+",
            "subtract": "-", 
            "multiply": "×",
            "divide": "÷",
            "power": "^",
            "modulo": "%"
        }
        
        symbol = symbols.get(operation, operation)
        operands_str = f" {symbol} ".join(map(str, operands))
        return f"{operands_str} = {result}"