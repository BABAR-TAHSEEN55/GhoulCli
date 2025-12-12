import os
from typing import Any, Optional

from rich.console import Console
from rich.text import Text

console = Console()
GET_CURRENT_DIR = os.getcwd()


def display_step(title: str, content: str):
    console.print(f"[bold blue]{title}[/bold blue]")
    console.print(Text(content, style="bright_white"))
    console.print()


def display_tool_call(tool_name: Optional[str], tool_input: Any):
    input_text = str(tool_input) if tool_input else "No input"
    console.print("[bold orange]🔧 Executing Tool[/bold orange]")
    console.print(f"[yellow]Function:[/yellow] [bold white]{tool_name}[/bold white]")
    console.print(f"[yellow]Input:[/yellow] [dim]{input_text}[/dim]")
    console.print()


def display_result(content: str):
    console.print("")
    console.print("[bold green]Result[/bold green]")
    console.print(Text(content, style="bright_green"))
    console.print()


def print_capabilities():
    console.print("[bold red]⚠️  Web Search Disabled[/bold red]")
    console.print()
    console.print(
        "[dim]Web search functionality is disabled for security reasons.[/dim]"
    )
    console.print(f"[dim]Current working dir : {GET_CURRENT_DIR}[/dim]")
    console.print()

    console.print("[bold cyan] Available Capabilities[/bold cyan]")
    console.print()

    tools_data = [
        ("🌤️", "Weather Information", "Get current weather conditions for any city"),
        ("💻", "Terminal Commands", "Execute system commands and shell operations"),
        ("📁", "File Operations", "Read, write, and search through local files"),
        ("🔍", "Code Search", "Search for patterns and text within your codebase"),
        ("🔧", "Git Operations", "Generate commits and perform version control tasks"),
    ]

    for emoji, name, description in tools_data:
        console.print(f"[bold green]{emoji} {name}[/bold green]")
        console.print(f"[dim]{description}[/dim]")
        console.print()

    console.print("[dim]Type your request below, or try:[/dim]")
    console.print("• [cyan]'What's the weather in Tokyo?'[/cyan]")
    console.print("• [cyan]'List files in my project'[/cyan]")
    console.print("• [cyan]'Search for TODO comments'[/cyan]")
    console.print("• [cyan]'Create a git commit'[/cyan]")
