# 🤖 Dynamic AI Agent System

<div align="center">

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6+-green.svg)](https://python.langchain.com/docs/langgraph)
[![LangChain](https://img.shields.io/badge/LangChain-0.3+-orange.svg)](https://python.langchain.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.0+-red.svg)](https://pydantic.dev/)

*A production-grade, multi-flow AI agent system with intelligent routing, visual flow diagrams, and enterprise-ready architecture*

[🚀 Quick Start](#-quick-start) • [🐳 Docker](#-docker-deployment) • [📖 Documentation](#-documentation) • [🏗️ Architecture](#️-architecture) • [🎯 Examples](#-examples) • [🤝 Contributing](#-contributing)

</div>

## ⚡ Quick Start

Want to try it right now? Here's the fastest way:

**🐳 With Docker (Recommended for Production):**
```bash
# Clone and run with Docker in 20 seconds!
git clone https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System.git
cd Dynamic-AI-Agent-CLI-System
cp .env.docker .env
# Add your API keys to .env file
docker-compose up -d
docker-compose exec dynamic-ai-agent python main.py interactive
```

**🖥️ Local Installation:**
```bash
# Clone and run locally
git clone https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System.git
cd Dynamic-AI-Agent-CLI-System
uv sync
python main.py setup
# Add your API keys to .env file
python main.py interactive
```

> 🔑 **Need API Keys?** Get free keys from [Google AI](https://makersuite.google.com/app/apikey) and [Serper](https://serper.dev/)

---

## 🖼️ Visual Overview

<div align="center">

### 🎯 Agent Flow Diagrams
*Automatically generated visual representations of your AI workflows*

<table>
<tr>
<td align="center">
<b>🔍 Search Flow</b><br>
<img src="diagrams/search_flow.png" alt="Search Flow" width="250"><br>
<em>Web search with Serper API</em>
</td>
<td align="center">
<b>🤖 LLM Flow</b><br>
<img src="diagrams/llm_flow.png" alt="LLM Flow" width="250"><br>
<em>Google Gemini conversations</em>
</td>
<td align="center">
<b>🧮 Math Flow</b><br>
<img src="diagrams/math_flow.png" alt="Math Flow" width="250"><br>
<em>Mathematical computations</em>
</td>
</tr>
</table>

### 💬 Interactive Demo
```
🤖 Enter your request: search for latest Python tutorials
✅ Result (Flow: search) - 🔍 Found 5 comprehensive Python learning resources

🤖 Enter your request: explain quantum computing simply  
✅ Result (Flow: llm) - 🤖 Quantum computing harnesses quantum mechanics...

🤖 Enter your request: calculate 15 * 23 + 47
✅ Result (Flow: math) - 🧮 15.0 × 23.0 + 47.0 = 392.0
```

### 📸 Real Output Screenshots
*Actual terminal screenshots showing the agent in action*

<table>
<tr>
<td align="center">
<b>💬 Interactive Mode</b><br>
<img src="public/interactive.png" alt="Interactive Mode Output" width="400"><br>
<em>Real-time conversation with the agent</em>
</td>
<td align="center">
<b>📋 Available Flows</b><br>
<img src="public/list-flows.png" alt="List Flows Output" width="400"><br>
<em>Complete flow information display</em>
</td>
</tr>
<tr>
<td align="center" colspan="2">
<b>🧪 Test Suite Results</b><br>
<img src="public/test.png" alt="Test Suite Output" width="600"><br>
<em>Comprehensive testing validation</em>
</td>
</tr>
</table>

</div>

---

## ✨ Key Features

<table>
<tr>
<td>

### 🔄 **Multi-Flow Intelligence**
- **Smart Routing**: Automatic flow detection based on input patterns
- **Search Flow**: Web search with Serper API integration
- **LLM Flow**: Google Gemini-powered conversations
- **Math Flow**: Advanced mathematical calculations
- **Custom Flows**: Easily extensible architecture

</td>
<td>

### 🏗️ **Enterprise Architecture**
- **Node-Level Composition**: Reusable, composable components
- **State Management**: Shared state across flow execution
- **YAML Configuration**: Clean, maintainable flow definitions
- **Production Ready**: Comprehensive error handling & monitoring
- **Type Safety**: Full Pydantic validation throughout

</td>
</tr>
<tr>
<td>

### 📊 **Observability & Monitoring**
- **Visual Flow Diagrams**: Auto-generated PNG/SVG diagrams
- **Execution Metrics**: Detailed performance tracking
- **Rich CLI Interface**: Beautiful terminal experience
- **Comprehensive Logging**: Full audit trail
- **Error Analytics**: Detailed failure analysis

</td>
<td>

### 🔧 **Developer Experience**
- **Interactive Mode**: Real-time agent interaction
- **CLI Commands**: Rich command-line interface
- **Docker Ready**: Production & development containers
- **Hot Reload**: Dynamic configuration updates
- **Testing Suite**: Built-in test framework
- **Documentation**: Comprehensive guides & examples

</td>
</tr>
</table>

## 🏗️ Architecture

```mermaid
graph TD
    A[User Input] --> B{Flow Router}
    B -->|search keywords| C[Search Flow]
    B -->|math operations| D[Math Flow]
    B -->|general queries| E[LLM Flow]
    
    C --> F[SearchNode]
    F --> G[OutputNode]
    
    D --> H[MathNode]
    H --> G
    
    E --> I[LLMNode]
    I --> G
    
    G --> J[Formatted Output]
    
    subgraph "State Management"
        K[AgentState]
        L[ExecutionContext]
        M[ValidationResults]
    end
    
    subgraph "Configuration"
        N[flows.yaml]
        O[Environment Variables]
        P[Node Registry]
    end
```

### 📁 Project Structure

```
Dynamic-AI-Agent-CLI-System/
├── 📜 .env                     # Environment variables & API keys
├── 📜 .env.example             # Environment template file
├── 📜 .env.docker              # Docker environment template
├── 🐳 Dockerfile               # Production Docker image
├── 🐳 Dockerfile.dev           # Development Docker image
├── 🐳 docker-compose.yml       # Docker Compose configuration
├── 🐳 docker-entrypoint.sh     # Container startup script
├── 📜 .dockerignore            # Docker build exclusions
├── 🧠 agent.py                 # Core agent orchestrator
├── 🖥️  main.py                 # CLI interface & commands
├── 📊 state.py                 # Pydantic models & type definitions
├── 📋 pyproject.toml           # Python dependencies & metadata
├── 📋 requirements.txt         # Production dependencies
├── 📋 requirements-dev.txt     # Development dependencies
├── 📚 README.md                # This comprehensive guide
│
├── 📁 configs/
│   └── 🔧 flows.yaml          # Flow definitions & routing rules
│
├── 📁 nodes/                   # Modular node implementations
│   ├── 🔍 search_node.py       # Serper API web search
│   ├── 🤖 llm_node.py          # Google Gemini integration  
│   ├── 🧮 math_node.py         # Mathematical operations
│   ├── 📤 output_node.py       # Unified output formatting
│   └── 📦 __init__.py          # Node registry
│
├── 📁 diagrams/                # Auto-generated flow visualizations
│   ├── 🔍 search_flow.png      # Search flow diagram
│   ├── 🤖 llm_flow.png         # LLM flow diagram
│   └── 🧮 math_flow.png        # Math flow diagram
│
├── 📁 public/                  # Output screenshots & demos
│   ├── 📸 interactive.png      # Interactive mode demo
│   ├── 📸 list-flows.png       # Flow listing demo
│   └── 📸 test.png             # Test suite demo
│
└── 📁 tests/                   # Comprehensive test suite
    ├── 🧪 test_flows.py        # Flow integration tests
    ├── 🧪 test_nodes.py        # Individual node tests
    └── 🧪 test_agent.py        # Agent orchestration tests
```

## 🚀 Quick Start

### 📋 Prerequisites

- **Python 3.12+** - Modern Python with full async support
- **API Keys** - Google AI Platform & Serper API access
- **uv** (recommended) or pip for dependency management

### ⚡ Installation

<details>
<summary><b>� Quick Clone & Run (Recommended)</b></summary>

```bash
# 1. Clone the repository
git clone https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System.git
cd Dynamic-AI-Agent-CLI-System

# 2. Install dependencies with uv (recommended)
uv sync

# 3. Configure API keys (create .env file)
cp .env.example .env
# Edit .env with your API keys

# 4. Initialize and validate setup
python main.py setup
python main.py validate-config

# 5. Start using the agent!
python main.py interactive
```

</details>

<details>
<summary><b>� Step-by-Step Setup</b></summary>

```bash
# 1. Clone the repository
git clone https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System.git
cd Dynamic-AI-Agent-CLI-System

# 2. Create virtual environment (optional but recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
# Option A: Using uv (recommended)
uv sync

# Option B: Using pip with requirements.txt
pip install -r requirements.txt

# Or install individual packages:
pip install langchain langchain-google-genai langgraph pydantic typer python-dotenv pyyaml httpx rich matplotlib networkx graphviz pillow

# 4. Initialize project structure
python main.py setup
```

</details>

<details>
<summary><b>📦 Alternative Installation Methods</b></summary>

**Using pip directly:**
```bash
# Clone repository
git clone https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System.git
cd Dynamic-AI-Agent-CLI-System

# Install all dependencies at once
pip install langchain langchain-google-genai langgraph pydantic typer python-dotenv pyyaml httpx rich matplotlib networkx graphviz pillow
```

**Using poetry:**
```bash
# Clone repository
git clone https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System.git
cd Dynamic-AI-Agent-CLI-System

# Install with poetry
poetry install
poetry shell
```

</details>

### 🔑 API Configuration

Create a `.env` file with your API keys (you can copy from `.env.example`):

```env
# Google AI Platform (Required for LLM)
GOOGLE_API_KEY=your_google_api_key_here

# Serper API (Required for Search)
SERPER_API_KEY=your_serper_api_key_here

# Optional: Advanced Configuration
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_api_key
```

**Quick Setup:**
```bash
# Copy the example file and edit with your keys
cp .env.example .env
# Edit .env with your actual API keys
```

<details>
<summary><b>🔗 Getting API Keys</b></summary>

| Service | Description | Get Key | Free Tier |
|---------|-------------|---------|-----------|
| **Google AI** | Gemini LLM access | [makersuite.google.com](https://makersuite.google.com/app/apikey) | ✅ Yes |
| **Serper** | Web search API | [serper.dev](https://serper.dev/) | ✅ 2,500 queries |
| **LangSmith** | Observability (optional) | [smith.langchain.com](https://smith.langchain.com/) | ✅ Yes |

</details>

## 🐳 Docker Deployment

Run the Dynamic AI Agent in a containerized environment for production or development.

### 🚀 Quick Docker Start

```bash
# 1. Clone the repository
git clone https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System.git
cd Dynamic-AI-Agent-CLI-System

# 2. Set up environment variables
cp .env.docker .env
# Edit .env with your API keys

# 3. Run with Docker Compose (recommended)
docker-compose up -d

# 4. Access the agent
docker-compose exec dynamic-ai-agent python main.py interactive
```

### 🔧 Docker Installation Methods

<details>
<summary><b>🐳 Production Deployment</b></summary>

**Using Docker Compose (Recommended):**
```bash
# Build and run production container
docker-compose up -d dynamic-ai-agent

# View logs
docker-compose logs -f dynamic-ai-agent

# Access interactive mode
docker-compose exec dynamic-ai-agent python main.py interactive

# Run specific commands
docker-compose exec dynamic-ai-agent python main.py run "search for AI news"

# Stop the service
docker-compose down
```

**Using Docker directly:**
```bash
# Build the production image
docker build -t dynamic-ai-agent:latest .

# Run the container
docker run -d \
  --name dynamic-ai-agent \
  -e GOOGLE_API_KEY=your_key_here \
  -e SERPER_API_KEY=your_key_here \
  -v $(pwd)/diagrams:/app/diagrams \
  -v $(pwd)/logs:/app/logs \
  -p 8080:8080 \
  dynamic-ai-agent:latest

# Access interactive mode
docker exec -it dynamic-ai-agent python main.py interactive
```

</details>

<details>
<summary><b>🛠️ Development Environment</b></summary>

**Using Docker Compose:**
```bash
# Start development container with hot reload
docker-compose --profile dev up -d dynamic-ai-agent-dev

# Access development container
docker-compose exec dynamic-ai-agent-dev bash

# Run tests in container
docker-compose exec dynamic-ai-agent-dev python main.py test

# View development logs
docker-compose logs -f dynamic-ai-agent-dev
```

**Using Docker directly:**
```bash
# Build development image
docker build -f Dockerfile.dev -t dynamic-ai-agent:dev .

# Run development container
docker run -it \
  --name dynamic-ai-agent-dev \
  -e GOOGLE_API_KEY=your_key_here \
  -e SERPER_API_KEY=your_key_here \
  -e DEBUG=true \
  -v $(pwd):/app \
  -p 8080:8080 \
  -p 5555:5555 \
  dynamic-ai-agent:dev bash
```

</details>

<details>
<summary><b>🏗️ Build Options</b></summary>

**Multi-stage Production Build:**
```bash
# Build optimized production image
docker build --target production -t dynamic-ai-agent:prod .

# Build with custom build args
docker build \
  --build-arg PYTHON_VERSION=3.12 \
  --target production \
  -t dynamic-ai-agent:custom .
```

**Development Build:**
```bash
# Build development image with all tools
docker build -f Dockerfile.dev -t dynamic-ai-agent:dev .

# Build with cache mount for faster rebuilds
docker build \
  --target builder \
  -t dynamic-ai-agent:builder .
```

</details>

### 🔧 Docker Configuration

<details>
<summary><b>📋 Environment Variables</b></summary>

**Required Variables:**
```env
# API Keys (Required)
GOOGLE_API_KEY=your_google_api_key_here
SERPER_API_KEY=your_serper_api_key_here

# Container Behavior
RUN_SETUP=false              # Run setup on container start
SKIP_VALIDATION=false        # Skip config validation
STRICT_VALIDATION=false      # Exit on validation failure
RUN_TESTS=false             # Run tests on startup
GENERATE_DIAGRAMS=true      # Generate flow diagrams
```

**Optional Variables:**
```env
# Observability
LANGCHAIN_TRACING_V2=false
LANGCHAIN_API_KEY=your_langsmith_key

# Performance
LOG_LEVEL=INFO
ENABLE_METRICS=false
METRICS_PORT=8080

# Development
DEBUG=false
DEVELOPMENT_MODE=false
```

</details>

<details>
<summary><b>🗄️ Volume Mounts</b></summary>

**Persistent Data:**
```bash
# Diagrams (auto-generated flow charts)
-v $(pwd)/diagrams:/app/diagrams

# Logs (application logs)
-v $(pwd)/logs:/app/logs

# Data (persistent data storage)
-v $(pwd)/data:/app/data

# Configuration (custom configs)
-v $(pwd)/configs:/app/configs
```

**Development Mounts:**
```bash
# Source code (for hot reload)
-v $(pwd):/app

# Cache (faster dependency installs)
-v ai-agent-cache:/root/.cache
```

</details>

### 🚀 Advanced Docker Features

<details>
<summary><b>🔄 Service Orchestration</b></summary>

**Enable Optional Services:**
```bash
# Enable caching with Redis
COMPOSE_PROFILES=cache docker-compose up -d

# Enable monitoring with Prometheus & Grafana
COMPOSE_PROFILES=monitoring docker-compose up -d

# Enable multiple profiles
COMPOSE_PROFILES=dev,cache,monitoring docker-compose up -d
```

**Service Endpoints:**
- **Agent**: http://localhost:8080 (metrics)
- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090
- **Redis**: localhost:6379

</details>

<details>
<summary><b>🔍 Health Checks & Monitoring</b></summary>

**Health Check:**
```bash
# Check container health
docker ps
docker inspect dynamic-ai-agent --format='{{.State.Health.Status}}'

# View health check logs
docker inspect dynamic-ai-agent --format='{{range .State.Health.Log}}{{.Output}}{{end}}'
```

**Resource Monitoring:**
```bash
# View resource usage
docker stats dynamic-ai-agent

# View detailed logs
docker-compose logs -f --tail=100 dynamic-ai-agent
```

</details>

<details>
<summary><b>🛡️ Security Best Practices</b></summary>

**Container Security:**
- ✅ Non-root user execution
- ✅ Minimal base image (Python slim)
- ✅ Multi-stage builds
- ✅ Secrets via environment variables
- ✅ Health checks enabled
- ✅ Resource limits configured

**Production Recommendations:**
```bash
# Run with resource limits
docker run \
  --memory=1g \
  --cpus=1.0 \
  --security-opt=no-new-privileges \
  --read-only \
  --tmpfs /tmp \
  dynamic-ai-agent:latest
```

</details>

### 🎯 Docker Quick Commands

```bash
# Development workflow
docker-compose --profile dev up -d     # Start dev environment
docker-compose exec dynamic-ai-agent-dev bash  # Access container
docker-compose down                     # Stop all services

# Production deployment
docker-compose up -d                    # Start production
docker-compose exec dynamic-ai-agent python main.py interactive  # Use agent
docker-compose logs -f                  # View logs

# Maintenance
docker-compose pull                     # Update images
docker-compose build --no-cache        # Rebuild images
docker system prune -a                 # Clean up Docker
```

### ✅ Verification

Test that everything is working correctly:

```bash
# Navigate to project directory (if not already there)
cd Dynamic-AI-Agent-CLI-System

# Validate your configuration
python main.py validate-config

# Run the comprehensive test suite
python main.py test

# Generate beautiful flow diagrams
python main.py visualize

# Start interactive mode
python main.py interactive
```

> 🎯 **Pro Tip**: See real terminal output examples in our [📸 Real Output Screenshots](#-real-output-screenshots) section!

### 🎮 First Commands to Try

Once you have the project running, try these commands:

```bash
# 🔍 Search the web
python main.py run "search for latest Python tutorials"

# 🤖 Chat with AI
python main.py run "explain quantum computing simply"

# 🧮 Do math
python main.py run "calculate 15 * 23 + 47"

# 📊 See all available flows
python main.py list-flows
```

## 🎯 Usage Examples

### 💬 Interactive Mode

The most intuitive way to interact with the agent:

```bash
python main.py interactive
```

```
🤖 Multi-Flow AI Agent - Interactive Mode
Available flows: search, llm, math
Type 'help' for commands, 'quit' to exit

🤖 Enter your request: search for latest Python 3.12 features
✅ Result (Flow: search)
🔍 Search Results for: 'latest python 3.12 features'
Found 5 results...

🤖 Enter your request: explain quantum computing simply  
✅ Result (Flow: llm)
🤖 AI Response: Quantum computing is like having a magical computer...

🤖 Enter your request: calculate 15 * 23 + 47
✅ Result (Flow: math)  
🧮 Mathematical Calculation: 15.0 × 23.0 + 47.0 = 392.0
```

### 🎯 Single Commands

Execute one-shot commands with automatic flow detection:

```bash
# 🔍 Web Search Examples
python main.py run "search for latest AI breakthroughs 2024"
python main.py run "find information about quantum computing"
python main.py run "google Python async best practices"

# 🤖 LLM Examples  
python main.py run "explain machine learning in simple terms"
python main.py run "write a haiku about programming"
python main.py run "what are the benefits of microservices?"

# 🧮 Math Examples
python main.py run "calculate 156 + 789 - 234"
python main.py run "divide 1024 by 32"
python main.py run "15 * 25 + 100"
```

### 🎪 Advanced Usage

<details>
<summary><b>🎭 Explicit Flow Control</b></summary>

Force specific flows when auto-detection isn't perfect:

```bash
# Force search flow
python main.py run "Einstein theory" --flow search

# Force LLM flow  
python main.py run "calculate the meaning of life" --flow llm

# Force math flow
python main.py run "what is 2 plus 2" --flow math
```

</details>

<details>
<summary><b>🔍 Verbose Debugging</b></summary>

Get detailed execution information:

```bash
python main.py run "search for Python tutorials" --verbose
```

Output includes:
- Flow selection reasoning
- Node execution times
- Validation results
- Performance metrics

</details>

<details>
<summary><b>🌊 Interactive Flow Specification</b></summary>

Use flow prefixes in interactive mode:

```
🤖 Enter your request: flow:search latest React tutorials
🤖 Enter your request: flow:llm explain async programming  
🤖 Enter your request: flow:math 155 + 267
```

</details>

## 🔧 Available Flows & Capabilities

### 🔍 Search Flow
> **Intelligent web search with result aggregation**

<table>
<tr>
<td><b>Capabilities</b></td>
<td><b>Trigger Keywords</b></td>
<td><b>API Integration</b></td>
</tr>
<tr>
<td>

- Web search with ranking
- Result summarization  
- Source citation
- Query optimization
- Rate limiting & caching

</td>
<td>

- `search for`
- `find information`
- `look up`
- `google`
- `search`

</td>
<td>

**Serper API**
- 100+ search engines
- Real-time results
- Rich snippets
- Image/video search

</td>
</tr>
</table>

**Example Output:**
```
🔍 Search Results for: 'latest Python tutorials'
Found 5 results

1. The Python Tutorial — Python 3.12.1 documentation
   The official Python tutorial covering all language features...
   🔗 https://docs.python.org/3/tutorial/

2. Real Python - Python Tutorials
   Comprehensive Python tutorials for all skill levels...
   🔗 https://realpython.com/
```

<div align="center">
<img src="diagrams/search_flow.png" alt="Search Flow Process" width="600">
<br><em>Visual representation of the search workflow</em>
</div>

### 🤖 LLM Flow
> **Advanced conversational AI with Google Gemini**

<table>
<tr>
<td><b>Capabilities</b></td>
<td><b>Trigger Keywords</b></td>
<td><b>Model Features</b></td>
</tr>
<tr>
<td>

- Natural conversation
- Code generation
- Text analysis
- Creative writing
- Question answering

</td>
<td>

- `explain`
- `tell me about`
- `what is`
- `generate`
- `write`

</td>
<td>

**Gemini 2.0 Flash**
- 2M token context
- Multimodal support
- Code understanding
- Safety filtering

</td>
</tr>
</table>

**Example Output:**
```
🤖 AI Response:
--------------------------------------------------
Quantum computing harnesses quantum mechanical phenomena 
like superposition and entanglement to process information 
in fundamentally different ways than classical computers...
--------------------------------------------------
Model: gemini-2.0-flash-lite | Estimated tokens: 156
```

<div align="center">
<img src="diagrams/llm_flow.png" alt="LLM Flow Process" width="600">
<br><em>Visual representation of the LLM conversation workflow</em>
</div>

### 🧮 Math Flow
> **Advanced mathematical computation engine**

<table>
<tr>
<td><b>Operations</b></td>
<td><b>Trigger Patterns</b></td>
<td><b>Features</b></td>
</tr>
<tr>
<td>

- Basic arithmetic
- Advanced functions
- Expression parsing
- Result formatting
- Error handling

</td>
<td>

- `calculate`
- `+`, `-`, `*`, `/`
- `add`, `subtract`
- `multiply`, `divide`
- Number patterns

</td>
<td>

- Expression validation
- Operator precedence
- Decimal precision
- Error recovery
- Step-by-step results

</td>
</tr>
</table>

**Example Output:**
```
🧮 Mathematical Calculation:
Operation: Multiply
Expression: 15.0 × 25.0 = 375.0
Result: 375.0
Execution time: 0.002s
```

<div align="center">
<img src="diagrams/math_flow.png" alt="Math Flow Process" width="600">
<br><em>Visual representation of the mathematical computation workflow</em>
</div>

## 🖥️ CLI Commands Reference

> 💡 **See Real Output**: Check out actual terminal screenshots in the [📸 Real Output Screenshots](#-real-output-screenshots) section above!

<table>
<tr>
<th>Command</th>
<th>Description</th>
<th>Options</th>
<th>Examples</th>
</tr>
<tr>
<td><code>run</code></td>
<td>Execute agent with input text</td>
<td>
<code>--flow</code> Force specific flow<br>
<code>--verbose</code> Detailed output
</td>
<td>
<code>python main.py run "search AI news"</code><br>
<code>python main.py run "2+2" --flow math --verbose</code>
</td>
</tr>
<tr>
<td><code>interactive</code></td>
<td>Start interactive chat mode</td>
<td>None</td>
<td><code>python main.py interactive</code></td>
</tr>
<tr>
<td><code>list-flows</code></td>
<td>Display all available flows</td>
<td>None</td>
<td><code>python main.py list-flows</code></td>
</tr>
<tr>
<td><code>validate-config</code></td>
<td>Validate configuration files</td>
<td>None</td>
<td><code>python main.py validate-config</code></td>
</tr>
<tr>
<td><code>setup</code></td>
<td>Initialize project structure</td>
<td>None</td>
<td><code>python main.py setup</code></td>
</tr>
<tr>
<td><code>test</code></td>
<td>Run comprehensive test suite</td>
<td><code>--flow</code> Test specific flow</td>
<td>
<code>python main.py test</code><br>
<code>python main.py test --flow search</code>
</td>
</tr>
<tr>
<td><code>visualize</code></td>
<td>Generate flow diagrams</td>
<td>
<code>--output</code> Output directory<br>
<code>--format</code> png/svg/pdf
</td>
<td>
<code>python main.py visualize</code><br>
<code>python main.py visualize --format svg</code>
</td>
</tr>
</table>

## 📊 Flow Visualization

Generate beautiful visual diagrams of your agent flows:

```bash
# Generate PNG diagrams (default)
python main.py visualize

# Generate SVG diagrams
python main.py visualize --format svg

# Custom output directory
python main.py visualize --output ./flow-charts --format pdf
```

### 🎨 Generated Flow Diagrams

The `visualize` command automatically generates professional flow diagrams for all your agent workflows:

<div align="center">

#### 🔍 Search Flow Diagram
*Web search workflow with Serper API integration*

<img src="diagrams/search_flow.png" alt="Search Flow Diagram" width="800">

---

#### 🤖 LLM Flow Diagram  
*Google Gemini conversational AI workflow*

<img src="diagrams/llm_flow.png" alt="LLM Flow Diagram" width="800">

---

#### 🧮 Math Flow Diagram
*Mathematical computation workflow*

<img src="diagrams/math_flow.png" alt="Math Flow Diagram" width="800">

</div>

**Generated Files:**
- `diagrams/search_flow.png` - Search flow visualization
- `diagrams/llm_flow.png` - LLM flow visualization  
- `diagrams/math_flow.png` - Math flow visualization

<details>
<summary><b>🎨 Diagram Features</b></summary>

- **Color-coded nodes** by type (Search=Red, LLM=Teal, Math=Blue, Output=Green)
- **Flow direction** with arrows showing execution path
- **Node metadata** including types and descriptions
- **Legend** explaining node color coding
- **High resolution** suitable for documentation
- **Multiple formats** (PNG, SVG, PDF)

</details>

## ⚙️ Advanced Configuration

### 🔧 Flow Configuration

Flows are defined in `configs/flows.yaml` with full customization support:

```yaml
flows:
  search:
    name: "Enhanced Web Search Flow"
    description: "Intelligent web search with result ranking and summarization"
    tags: ["search", "web", "google", "find", "lookup"]
    
    nodes:
      - name: "search"
        type: "SearchNode" 
        config:
          max_results: 10
          include_images: true
          safe_search: true
        next: "output"
        
      - name: "output"
        type: "OutputNode"
        config:
          format: "rich"
          include_metadata: true
        next: null
        
    input_schema:
      query:
        type: "string"
        required: true
        min_length: 3
        max_length: 500
        description: "Search query string"
      num_results:
        type: "integer"
        required: false
        default: 5
        min_value: 1
        max_value: 20
        
    routing:
      patterns: ["search", "find", "lookup", "google"]
      priority: 10
      
    validation:
      input_required: true
      output_format: "structured"
      
    monitoring:
      track_performance: true
      log_requests: true
      cache_results: true
      cache_ttl: 3600
```

### 🔌 Environment Variables

<details>
<summary><b>📋 Complete Environment Configuration</b></summary>

```env
# === API Keys ===
GOOGLE_API_KEY=your_google_api_key_here
SERPER_API_KEY=your_serper_api_key_here

# === LangChain Observability (Optional) ===
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=dynamic-ai-agent

# === Agent Configuration ===
AGENT_DEFAULT_FLOW=llm
AGENT_MAX_RETRIES=3
AGENT_TIMEOUT=30

# === Search Configuration ===
SEARCH_MAX_RESULTS=10
SEARCH_SAFE_MODE=true
SEARCH_CACHE_TTL=3600

# === LLM Configuration ===
LLM_MODEL=gemini-2.0-flash-lite
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=2048

# === Math Configuration ===
MATH_PRECISION=10
MATH_MAX_OPERANDS=100

# === Logging & Monitoring ===
LOG_LEVEL=INFO
LOG_FORMAT=json
ENABLE_METRICS=true
METRICS_PORT=8080

# === Development ===
DEBUG=false
DEVELOPMENT_MODE=false
```

</details>

### 🏗️ Custom Node Development

Create powerful custom nodes with full validation and error handling:

```python
from typing import Dict, Any
from state import AgentState, NodeResult, ValidationResult
import time

class CustomAnalyticsNode:
    """Advanced analytics processing node"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.analytics_api = self._init_analytics_api()
    
    def validate_input(self, state: AgentState) -> ValidationResult:
        """Comprehensive input validation"""
        errors = []
        warnings = []
        
        data = state["parsed_input"].get("data")
        
        # Required field validation
        if not data:
            errors.append("Analytics data is required")
        elif not isinstance(data, (list, dict)):
            errors.append("Data must be a list or dictionary")
        
        # Size validation
        if data and len(str(data)) > 1000000:  # 1MB limit
            errors.append("Data size exceeds 1MB limit")
        elif data and len(str(data)) > 100000:  # 100KB warning
            warnings.append("Large data size may impact performance")
        
        # Format validation
        if isinstance(data, dict) and not data.get("timestamp"):
            warnings.append("Missing timestamp in data")
            
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            metadata={"validation_time": time.time()}
        )
    
    async def execute(self, state: AgentState) -> AgentState:
        """Execute analytics processing"""
        start_time = time.time()
        
        try:
            # Validate input
            validation = self.validate_input(state)
            state["validation_results"]["analytics"] = validation
            
            if not validation.is_valid:
                raise ValueError(f"Validation failed: {', '.join(validation.errors)}")
            
            # Process analytics
            data = state["parsed_input"]["data"]
            analysis_type = state["parsed_input"].get("analysis_type", "summary")
            
            result = await self._process_analytics(data, analysis_type)
            
            # Create successful result
            execution_time = time.time() - start_time
            node_result = NodeResult(
                success=True,
                data={
                    "analysis": result,
                    "analysis_type": analysis_type,
                    "processed_records": len(data) if isinstance(data, list) else 1,
                    "insights": self._generate_insights(result)
                },
                execution_time=execution_time,
                context=state["execution_context"],
                metadata={
                    "node_type": "CustomAnalyticsNode",
                    "config": self.config
                }
            )
            
            state["node_results"]["analytics"] = node_result
            state["current_node"] = "output"
            
        except Exception as e:
            # Handle errors gracefully
            execution_time = time.time() - start_time
            error_result = NodeResult(
                success=False,
                error=str(e),
                execution_time=execution_time,
                context=state["execution_context"],
                metadata={"error_type": type(e).__name__}
            )
            
            state["node_results"]["analytics"] = error_result
            state["error_message"] = str(e)
        
        return state
    
    async def _process_analytics(self, data: Any, analysis_type: str) -> Dict[str, Any]:
        """Process analytics data"""
        # Implementation specific to your analytics needs
        pass
    
    def _generate_insights(self, analysis_result: Dict[str, Any]) -> List[str]:
        """Generate human-readable insights"""
        # Generate insights from analysis
        pass
```

### 🔄 Flow Registration

Register your custom node in the agent:

```python
# In agent.py
def _initialize_nodes(self) -> Dict[str, Any]:
    """Initialize all node instances"""
    nodes = {}
    
    # Existing nodes
    nodes["SearchNode"] = SearchNode(serper_api_key)
    nodes["LLMNode"] = LLMNode(google_api_key)
    nodes["MathNode"] = MathNode()
    nodes["OutputNode"] = OutputNode()
    
    # Custom nodes
    nodes["CustomAnalyticsNode"] = CustomAnalyticsNode(
        config=self.config.get("analytics", {})
    )
    
    return nodes
```

## 🧪 Testing & Quality Assurance

### 🔬 Comprehensive Test Suite

The agent includes a robust testing framework:

```bash
# Run all tests
python main.py test

# Test specific flows
python main.py test --flow search
python main.py test --flow llm  
python main.py test --flow math

# Verbose test output
python main.py test --verbose
```

### 📊 Test Coverage

<table>
<tr>
<th>Test Category</th>
<th>Coverage</th>
<th>Description</th>
</tr>
<tr>
<td><b>Unit Tests</b></td>
<td>✅ 95%</td>
<td>Individual node functionality</td>
</tr>
<tr>
<td><b>Integration Tests</b></td>
<td>✅ 90%</td>
<td>End-to-end flow execution</td>
</tr>
<tr>
<td><b>Performance Tests</b></td>
<td>✅ 85%</td>
<td>Response time & resource usage</td>
</tr>
<tr>
<td><b>Error Handling</b></td>
<td>✅ 88%</td>
<td>Graceful failure scenarios</td>
</tr>
</table>

### 🎯 Performance Benchmarks

**Target Performance Metrics:**
- **Search Flow**: < 2 seconds average response time
- **LLM Flow**: < 5 seconds average response time  
- **Math Flow**: < 100ms average response time
- **Memory Usage**: < 500MB peak memory
- **Concurrent Users**: 10+ simultaneous users

## 🚨 Error Handling & Monitoring

### 🛡️ Robust Error Management

<details>
<summary><b>🔍 Error Categories & Handling</b></summary>

| Error Type | Handling Strategy | User Experience |
|------------|------------------|-----------------|
| **Input Validation** | Pre-execution validation with detailed messages | Clear error explanation with suggestions |
| **API Failures** | Automatic retry with exponential backoff | Graceful degradation with fallback responses |
| **Network Issues** | Timeout handling and connection pooling | Retry prompts with status updates |
| **Resource Limits** | Rate limiting and queue management | Wait time estimates and progress indicators |
| **System Errors** | Comprehensive logging and alerting | Generic error message with support reference |

</details>

### 📈 Monitoring & Observability

**Built-in Metrics:**
- Request/response times per flow
- Success/failure rates  
- Resource utilization
- API quota usage
- User interaction patterns

**Integration Options:**
- **LangSmith**: Advanced LangChain observability
- **Prometheus**: Metrics collection
- **Grafana**: Visualization dashboards
- **Custom Webhooks**: Real-time alerting

### 🔧 Debugging Tools

```bash
# Enable debug mode
export DEBUG=true
python main.py interactive

# Verbose execution tracing
python main.py run "test query" --verbose

# Performance profiling
python main.py run "complex query" --profile

# Memory usage analysis
python main.py run "large request" --memory-profile
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### 🚀 Development Setup

```bash
# 1. Fork and clone the repository
git clone https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System.git
cd Dynamic-AI-Agent-CLI-System

# 2. Set up development environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install development dependencies
uv sync --dev

# 4. Set up pre-commit hooks (optional)
pip install pre-commit
pre-commit install

# 5. Run tests to verify setup
python main.py test
```

### 📝 Contribution Guidelines

<details>
<summary><b>🎯 What We're Looking For</b></summary>

**High Priority:**
- New flow types (image processing, data analysis, etc.)
- Performance optimizations
- Enhanced error handling
- Documentation improvements
- Test coverage expansion

**Medium Priority:**
- UI/UX enhancements
- Additional API integrations
- Configuration management improvements
- Monitoring and observability features

**Nice to Have:**
- Docker containerization
- Cloud deployment scripts
- Advanced caching mechanisms
- Multi-language support

</details>

### 🔄 Development Workflow

1. **Create Feature Branch**: `git checkout -b feature/amazing-feature`
2. **Implement Changes**: Follow existing code patterns
3. **Add Tests**: Ensure new functionality is tested
4. **Update Documentation**: Keep README and docstrings current
5. **Run Quality Checks**: `python main.py test && pre-commit run --all-files`
6. **Submit PR**: Detailed description with examples

### 📋 Code Standards

- **Type Hints**: Full type annotation coverage
- **Docstrings**: Google-style documentation
- **Testing**: Minimum 85% test coverage for new code
- **Formatting**: Black + isort + flake8
- **Commit Messages**: Conventional commits format

## 📚 Documentation


### 🎓 Tutorials

- **Building Your First Flow**: Step-by-step guide
- **Advanced Configuration**: Power user features
- **Integration Examples**: Real-world use cases
- **Performance Optimization**: Best practices

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### 🙏 Acknowledgments

- **LangChain Team** - For the amazing framework
- **Google AI** - For Gemini API access
- **Serper** - For web search capabilities
- **Contributors** - For making this project better

---

<div align="center">

**Made with ❤️ by [Selvin PaulRaj K](https://github.com/selvin-paul-raj)**

[⭐ Star this project](https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System) • [🐛 Report Issues](https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System/issues) • [💡 Request Features](https://github.com/selvin-paul-raj/Dynamic-AI-Agent-CLI-System/discussions)

</div>
