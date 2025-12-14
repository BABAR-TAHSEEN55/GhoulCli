<div align="center">

```
     ██████╗  ██╗  ██╗  ██████╗  ██╗   ██╗ ██╗       ██████╗ ██╗      ██╗
    ██╔════╝  ██║  ██║ ██╔═══██╗ ██║   ██║ ██║      ██╔════╝ ██║      ██║
    ██║  ███╗ ███████║ ██║   ██║ ██║   ██║ ██║      ██║      ██║      ██║
    ██║   ██║ ██╔══██║ ██║   ██║ ██║   ██║ ██║      ██║      ██║      ██║
    ╚██████╔╝ ██║  ██║ ╚██████╔╝ ╚██████╔╝ ███████╗ ╚██████╗ ███████╗ ██║
     ╚═════╝  ╚═╝  ╚═╝  ╚═════╝   ╚═════╝  ╚══════╝  ╚═════╝ ╚══════╝ ╚═╝
```

**An intelligent AI-Agent command-line assistant with autonomous reasoning capabilities**

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/)
[![Rich](https://img.shields.io/badge/Rich-Terminal-purple.svg)](https://rich.readthedocs.io/)

</div>

---

## Overview

GhoulAI is a sophisticated command-line AI Agent assistant that combines OpenAI's powerful language models with a structured reasoning framework to help you accomplish various tasks through natural language interactions. From weather queries to complex development workflows, GhoulAI understands your intent and executes solutions with precision.

## Key Features

### **Autonomous Reasoning**

- Multi-phase problem-solving approach (Start → Plan → Action → Observe → Result)
- Deep intent analysis and strategic task breakdown
- Self-correcting execution with error handling

### **Comprehensive Tool Suite**

- **🌤️ Weather Information** - Get real-time weather data for any city
- **💻 Terminal Operations** - Execute system commands and shell operations
- **📁 File Management** - Read, search, and analyze files in your codebase
- **🔍 Code Search** - Find patterns and text within your projects
- **🔧 Git Integration** - Generate commits and perform version control tasks
- **🐳 Docker Support** - Container orchestration capabilities

### **Safety & Security**

- Command timeout protection (30s limit)
- Environment-based API key management
- Structured JSON communication protocol
- Web search disabled for security

## Quick Start

### Prerequisites

- Python 3.13 or higher
- OpenAI API key
- UV package manager (recommended) or pip

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/GhoulAI.git
    cd GhoulAI
    ```

2. **Set up your environment**

    ```bash
    # Create a .env file
    echo "OPENAI_API_KEY=your_api_key_here" > .env
    echo "WEATHER_API=your_weather_api_url" >> .env
    ```

3. **Install dependencies**

    ```bash
    # Using UV (recommended)
    uv sync

    # Or using pip
    pip install -e .
    ```

4. **Run GhoulAI**
    ```bash
    python main.py
    ```

## Usage Examples

### Weather Queries

```
🤖 What can I help you with? What's the weather in Tokyo?

🧠 Planning: Fetching weather data for Tokyo...
🔧 Running get_weather...
✅ Result: The current weather in Tokyo is 18°C with clear skies.
   Humidity is at 55% with winds at 8 km/h.
```

### File Operations

```
🤖 What can I help you with? Search for TODO comments in my code

🧠 Planning: Searching for TODO patterns across the codebase...
🔧 Running grep_search...
✅ Result: Found 3 TODO items:
   1. main.py:25 - Add websearch with tavily
   2. setup.py:120 - Make the todo in react
   3. setup.py:122 - Create video and paste it in readme.md
```

### Development Workflows

```
🤖 What can I help you with? Create a React todo application

🧠 Planning: Setting up React project with Vite template...
🔧 Running run_terminal_cmd...
✅ Result: Successfully created a React todo application with full
   CRUD functionality. App is running on localhost:3000.
```

### Git Operations

```
🤖 What can I help you with? Stage all modified files and commit them

🧠 Planning: Checking git status and staging files individually...
🔧 Running run_terminal_cmd...
✅ Result: Successfully staged and committed 3 files:
   - main.py: "Add error handling for API configuration"
   - setup.py: "Improve conversation loop and progress indicators"
   - README.md: "Update comprehensive documentation"
```

## 🏗️ Architecture

### Project Structure

```
GhoulAI/
├── agent/
│   ├── agent.py        # Branding and intro functionality
│   ├── setup.py        # Main conversation loop and AI interaction
│   ├── tools.py        # Available tool implementations
│   ├── prompt.py       # System prompt and AI behavior configuration
│   ├── helpers.py      # UI utilities and display functions
│   └── flagDetect.py   # Command-line argument parsing
├── main.py             # Entry point
├── pyproject.toml      # Project configuration and dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Required
OPENAI_API_KEY=sk-your-openai-api-key-here

# Optional
WEATHER_API=https://api.weatherapi.com/v1/current.json?key=YOUR_WEATHER_KEY
```

### Command-Line Options

```bash
# Run with minimal output (hide reasoning steps)
python main.py --noreason
```

## Development

### Adding New Tools

1. **Create your tool function in `tools.py`:**

    ```python
    def my_custom_tool(input_param: str) -> dict:
        try:
            # Your tool logic here
            result = do_something(input_param)
            return {"success": True, "data": result}
        except Exception as e:
            return {"success": False, "error": str(e)}
    ```

2. **Register the tool:**

    ```python
    available_tools = {
        # ... existing tools
        "my_custom_tool": my_custom_tool,
    }
    ```

3. **Update the system prompt** in `prompt.py` to describe your new tool.

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## Requirements

- **Python**: 3.13+
- **Dependencies**:
    - `openai>=2.8.1` - OpenAI API integration
    - `rich>=14.2.0` - Terminal UI and formatting
    - `requests>=2.32.5` - HTTP requests for APIs
    - `termcolor>=3.2.0` - Terminal color output
    - `dotenv>=0.9.9` - Environment variable management

<!--## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

----->

<!--<div align="center">
  <p><strong>Made with 🧙‍♂️ by the GhoulAI team</strong></p>
  <p><em>Empowering developers with intelligent automation</em></p>
</div>-->
