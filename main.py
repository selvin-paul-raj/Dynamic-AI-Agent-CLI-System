import asyncio
import os
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from agent import MultiFlowAgent

app = typer.Typer(
    name="multi-flow-agent",
    help="A production-grade multi-flow AI agent system",
    add_completion=False
)

console = Console()

# Global agent instance
agent: Optional[MultiFlowAgent] = None

def initialize_agent():
    """Initialize the agent with configuration"""
    global agent
    if agent is None:
        config_path = Path("configs/flows.yaml")
        if not config_path.exists():
            console.print("[red]Error: Configuration file not found at configs/flows.yaml[/red]")
            console.print("Please ensure the file exists and contains valid flow definitions.")
            raise typer.Exit(1)
        
        try:
            agent = MultiFlowAgent(str(config_path))
            console.print("[green]✓ Agent initialized successfully[/green]")
        except Exception as e:
            console.print(f"[red]Error initializing agent: {e}[/red]")
            raise typer.Exit(1)

@app.command()
def run(
    input_text: str = typer.Argument(..., help="Input text to process"),
    flow: Optional[str] = typer.Option(None, "--flow", "-f", help="Explicit flow type (search/llm/math)"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed execution info"),
):
    """Run the agent with the given input"""
    initialize_agent()
    
    console.print(Panel(
        f"[bold blue]Processing:[/bold blue] {input_text}",
        title="Multi-Flow AI Agent"
    ))
    
    # Execute agent
    result = asyncio.run(agent.execute(input_text, flow))
    
    # Display results
    if result["success"]:
        console.print(Panel(
            result["output"],
            title=f"✅ Result (Flow: {result['flow_used']})",
            border_style="green"
        ))
        
        if verbose:
            # Show execution details
            table = Table(title="Execution Details")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="white")
            
            table.add_row("Flow Used", result["flow_used"])
            table.add_row("Total Execution Time", f"{result.get('execution_time', 0):.3f}s")
            table.add_row("Nodes Executed", str(len(result.get('node_results', {}))))
            
            console.print(table)
            
            # Show node results
            if result.get("node_results"):
                node_table = Table(title="Node Execution Results")
                node_table.add_column("Node", style="cyan")
                node_table.add_column("Status", style="white")
                node_table.add_column("Time", style="yellow")
                
                for name, details in result["node_results"].items():
                    status = "✅ Success" if details["success"] else f"❌ Error: {details.get('error', 'Unknown')}"
                    node_table.add_row(name, status, f"{details['execution_time']:.3f}s")
                
                console.print(node_table)
    else:
        console.print(Panel(
            f"[red]{result.get('error', 'Unknown error')}[/red]",
            title="❌ Error",
            border_style="red"
        ))

@app.command()
def interactive():
    """Run the agent in interactive mode"""
    initialize_agent()
    
    console.print(Panel(
        "[bold green]Multi-Flow AI Agent - Interactive Mode[/bold green]\n"
        "Available flows: search, llm, math\n"
        "Type 'help' for commands, 'quit' to exit",
        title="Interactive Mode"
    ))
    
    async def run_interactive():
        """Async interactive loop"""
        import sys
        
        while True:
            try:
                # Use standard input instead of typer.prompt for better async compatibility
                console.print("\n🤖 Enter your request: ", end="")
                user_input = input().strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    console.print("[yellow]Goodbye![/yellow]")
                    break
                elif user_input.lower() == 'help':
                    show_help()
                    continue
                elif user_input.lower().startswith('flow:'):
                    # Parse explicit flow specification
                    parts = user_input.split(':', 1)
                    if len(parts) == 2:
                        flow_type, actual_input = parts[0].strip(), parts[1].strip()
                        flow_type = flow_type.replace('flow', '').strip()
                    else:
                        console.print("[red]Invalid flow syntax. Use: flow:type your request[/red]")
                        continue
                else:
                    flow_type = None
                    actual_input = user_input
                
                # Execute request
                with console.status("[bold green]Processing..."):
                    result = await agent.execute(actual_input, flow_type)
                
                # Display result
                if result["success"]:
                    console.print(Panel(
                        result["output"],
                        title=f"✅ Result (Flow: {result['flow_used']})",
                        border_style="green"
                    ))
                else:
                    console.print(Panel(
                        f"[red]{result.get('error', 'Unknown error')}[/red]",
                        title="❌ Error",
                        border_style="red"
                    ))
                    
            except KeyboardInterrupt:
                console.print("\n[yellow]Goodbye![/yellow]")
                break
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
    
    # Run the async interactive loop
    asyncio.run(run_interactive())

def show_help():
    """Show help information"""
    help_text = """
[bold cyan]Available Commands:[/bold cyan]
• help - Show this help message
• quit/exit/q - Exit interactive mode

[bold cyan]Flow Types:[/bold cyan]
• search - Web search using Serper API
• llm - Chat with Google Gemini
• math - Mathematical calculations

[bold cyan]Usage Examples:[/bold cyan]
• "search for latest AI news"
• "explain quantum computing"
• "calculate 15 + 25 * 3"
• "flow:search latest Python tutorials"
• "flow:math divide 100 by 4"

[bold cyan]Auto-Detection:[/bold cyan]
The agent can automatically detect the appropriate flow based on your input.
Use explicit flow specification (flow:type) to override auto-detection.
    """
    console.print(Panel(help_text, title="Help"))

@app.command()
def list_flows():
    """List available flows and their configurations"""
    initialize_agent()
    
    table = Table(title="Available Flows")
    table.add_column("Flow", style="cyan")
    table.add_column("Name", style="white")
    table.add_column("Description", style="yellow")
    table.add_column("Tags", style="green")
    
    for flow_id, flow_config in agent.flows.items():
        tags = ", ".join(flow_config.get("tags", []))
        table.add_row(
            flow_id,
            flow_config.get("name", ""),
            flow_config.get("description", ""),
            tags
        )
    
    console.print(table)

@app.command()
def validate_config():
    """Validate the configuration file"""
    config_path = Path("configs/flows.yaml")
    
    if not config_path.exists():
        console.print("[red]❌ Configuration file not found at configs/flows.yaml[/red]")
        raise typer.Exit(1)
    
    try:
        agent = MultiFlowAgent(str(config_path))
        console.print("[green]✅ Configuration is valid[/green]")
        
        # Show summary
        table = Table(title="Configuration Summary")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="white")
        
        table.add_row("Flows", str(len(agent.flows)))
        table.add_row("Nodes Initialized", str(len(agent.nodes)))
        table.add_row("Graphs Built", str(len(agent.graphs)))
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[red]❌ Configuration validation failed: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def setup():
    """Setup the project structure and environment"""
    console.print("[bold blue]Setting up Multi-Flow AI Agent...[/bold blue]")
    
    # Create directory structure
    directories = [
        "configs",
        "nodes",
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        console.print(f"✅ Created directory: {directory}")
    
    # Create __init__.py files
    init_files = [
        "nodes/__init__.py",
    ]
    
    for init_file in init_files:
        Path(init_file).touch()
        console.print(f"✅ Created: {init_file}")
    
    # Check .env file
    env_path = Path(".env")
    if not env_path.exists():
        env_content = """# Add your API keys here
GOOGLE_API_KEY=your_google_api_key_here
SERPER_API_KEY=your_serper_api_key_here
"""
        env_path.write_text(env_content)
        console.print("✅ Created .env template")
        console.print("[yellow]⚠️  Please add your actual API keys to .env file[/yellow]")
    else:
        console.print("✅ .env file already exists")
    
    console.print("\n[green]✅ Setup complete![/green]")
    console.print("\n[bold]Next steps:[/bold]")
    console.print("1. Add your API keys to the .env file")
    console.print("2. Install dependencies: uv add langchain langchain-google-genai langgraph pydantic typer python-dotenv pyyaml httpx rich")
    console.print("3. Run: python main.py validate-config")
    console.print("4. Start using: python main.py interactive")

@app.command()
def test(
    flow: str = typer.Option("all", "--flow", "-f", help="Flow to test (all/search/llm/math)"),
):
    """Test the agent with sample inputs"""
    initialize_agent()
    
    test_cases = {
        "search": [
            "search for latest Python tutorials",
            "find information about climate change"
        ],
        "llm": [
            "explain quantum computing in simple terms",
            "what is the meaning of life"
        ],
        "math": [
            "calculate 15 + 25",
            "divide 100 by 4"
        ]
    }
    
    flows_to_test = [flow] if flow != "all" else list(test_cases.keys())
    
    async def run_tests():
        """Run all tests in a single async context"""
        for flow_name in flows_to_test:
            if flow_name not in test_cases:
                console.print(f"[red]Unknown flow: {flow_name}[/red]")
                continue
                
            console.print(f"\n[bold cyan]Testing {flow_name} flow:[/bold cyan]")
            
            for test_input in test_cases[flow_name]:
                console.print(f"\n📝 Input: {test_input}")
                
                try:
                    with console.status("[bold green]Processing..."):
                        result = await agent.execute(test_input, flow_name)
                    
                    if result["success"]:
                        console.print("[green]✅ Success[/green]")
                        console.print(f"Output preview: {result['output'][:100]}...")
                    else:
                        console.print(f"[red]❌ Failed: {result.get('error', 'Unknown error')}[/red]")
                        
                except Exception as e:
                    console.print(f"[red]❌ Failed: {str(e)}[/red]")
    
    # Run all tests in a single event loop
    asyncio.run(run_tests())

@app.command()
def visualize(
    output_dir: str = typer.Option("diagrams", "--output", "-o", help="Output directory for diagrams"),
    format: str = typer.Option("png", "--format", "-f", help="Output format (png, svg, pdf)"),
):
    """Generate flow diagrams for all LangGraph workflows"""
    initialize_agent()
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        from matplotlib.patches import FancyBboxPatch
        import networkx as nx
        
        console.print(f"[bold blue]Generating flow diagrams...[/bold blue]")
        console.print(f"Output directory: {output_path.absolute()}")
        
        for flow_name, flow_config in agent.flows.items():
            console.print(f"\n📊 Creating diagram for {flow_name} flow...")
            
            # Create a directed graph
            G = nx.DiGraph()
            
            # Add nodes from flow configuration
            nodes = flow_config.get("nodes", [])
            for i, node_config in enumerate(nodes):
                node_name = node_config["name"]
                node_type = node_config["type"]
                G.add_node(node_name, type=node_type, order=i)
            
            # Add edges from flow configuration
            for node_config in nodes:
                node_name = node_config["name"]
                next_node = node_config.get("next")
                if next_node:
                    G.add_edge(node_name, next_node)
                else:
                    # Add END node if not exists
                    if "END" not in G.nodes():
                        G.add_node("END", type="end", order=len(nodes))
                    G.add_edge(node_name, "END")
            
            # Create the visualization
            fig, ax = plt.subplots(1, 1, figsize=(12, 8))
            
            # Use a hierarchical layout
            pos = {}
            levels = {}
            
            # Group nodes by their order/level
            for node, data in G.nodes(data=True):
                level = data.get('order', 0)
                if level not in levels:
                    levels[level] = []
                levels[level].append(node)
            
            # Position nodes in levels
            for level, level_nodes in levels.items():
                y = 1 - (level * 0.3)  # Top to bottom
                for i, node in enumerate(level_nodes):
                    x = (i + 1) / (len(level_nodes) + 1)
                    pos[node] = (x, y)
            
            # Define colors for different node types
            node_colors = {
                "SearchNode": "#FF6B6B",  # Red
                "LLMNode": "#4ECDC4",     # Teal
                "MathNode": "#45B7D1",    # Blue
                "OutputNode": "#96CEB4",  # Green
                "end": "#DDA0DD"          # Purple
            }
            
            # Draw nodes with custom styling
            for node, (x, y) in pos.items():
                node_data = G.nodes[node]
                node_type = node_data.get('type', 'unknown')
                color = node_colors.get(node_type, "#CCCCCC")
                
                # Create fancy box for node
                bbox = FancyBboxPatch(
                    (x-0.08, y-0.04), 0.16, 0.08,
                    boxstyle="round,pad=0.01",
                    facecolor=color,
                    edgecolor='black',
                    linewidth=2,
                    alpha=0.8
                )
                ax.add_patch(bbox)
                
                # Add node label
                ax.text(x, y, node, ha='center', va='center', 
                       fontsize=10, fontweight='bold', color='white')
                
                # Add node type as subtitle
                if node != "END":
                    ax.text(x, y-0.02, f"({node_type})", ha='center', va='center',
                           fontsize=8, color='white', style='italic')
            
            # Draw edges with arrows
            for edge in G.edges():
                start_pos = pos[edge[0]]
                end_pos = pos[edge[1]]
                
                # Calculate arrow positions (avoid overlapping with nodes)
                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]
                
                # Adjust start and end points to node edges
                start_x = start_pos[0] + (0.08 if dx > 0 else -0.08 if dx < 0 else 0)
                start_y = start_pos[1] + (-0.04 if dy < 0 else 0.04 if dy > 0 else 0)
                end_x = end_pos[0] + (-0.08 if dx > 0 else 0.08 if dx < 0 else 0)
                end_y = end_pos[1] + (0.04 if dy < 0 else -0.04 if dy > 0 else 0)
                
                ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                           arrowprops=dict(arrowstyle='->', lw=2, color='#333333'))
            
            # Customize the plot
            flow_title = flow_config.get("name", f"{flow_name.title()} Flow")
            ax.set_title(f"{flow_title}\n{flow_config.get('description', '')}", 
                        fontsize=16, fontweight='bold', pad=20)
            
            ax.set_xlim(-0.1, 1.1)
            ax.set_ylim(-0.1, 1.2)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Add legend
            legend_elements = []
            for node_type, color in node_colors.items():
                if node_type != "end" and any(G.nodes[n].get('type') == node_type for n in G.nodes()):
                    legend_elements.append(patches.Patch(color=color, label=node_type))
            
            if legend_elements:
                ax.legend(handles=legend_elements, loc='upper right', 
                         bbox_to_anchor=(1, 1), fontsize=10)
            
            # Save the diagram
            output_file = output_path / f"{flow_name}_flow.{format}"
            plt.tight_layout()
            plt.savefig(output_file, dpi=300, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            plt.close()
            
            console.print(f"✅ Saved: {output_file}")
        
        console.print(f"\n[green]✅ All flow diagrams generated successfully![/green]")
        console.print(f"📁 Check the '{output_dir}' directory for your diagrams")
        
    except ImportError as e:
        console.print(f"[red]❌ Missing required packages: {e}[/red]")
        console.print("Install with: uv add matplotlib networkx")
    except Exception as e:
        console.print(f"[red]❌ Error generating diagrams: {e}[/red]")

if __name__ == "__main__":
    app()
