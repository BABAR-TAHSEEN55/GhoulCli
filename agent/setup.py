import json
import sys

from openai import OpenAI
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt

from agent.flagDetect import options
from agent.helpers import (
    display_result,
    display_step,
    display_tool_call,
    print_capabilities,
)

from .agent import intro
from .prompt import SYSTEM_PROMPT
from .tools import available_tools

console = Console()


def setup():
    intro()
    print_capabilities()

    try:
        client = OpenAI()
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    except Exception as e:
        console.print(
            f"[bold red] API Configuration Error[/bold red]\n\n"
            f"[yellow]Error:[/yellow] {str(e)}\n"
            f"[dim]Please check your OpenAI API key configuration.[/dim]"
        )
        sys.exit(1)

    while True:
        console.print()
        query = Prompt.ask(
            "[bold cyan] What can I help you with?[/bold cyan]",
        )

        if not query.strip():
            console.print("[bold red] Query cannot be empty [/bold red]")
            continue

        if query.lower() in ["exit", "quit", "bye"]:
            console.print("[bold green]👋 Goodbye Anon ![/bold green]")
            break

        messages.append({"role": "user", "content": query})

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task("🧠 AI is thinking...", total=None)

            while True:
                try:
                    res = client.chat.completions.create(
                        model="gpt-4.1-nano",
                        response_format={"type": "json_object"},
                        messages=messages,
                    )

                    content = res.choices[0].message.content
                    if not content:
                        console.print("[red]❌ No response from AI[/red]")
                        break

                    messages.append({"role": "assistant", "content": content})
                    parsed_response = json.loads(content)

                    step = parsed_response.get("step")

                    if step == "start":
                        if not options.noreason:
                            display_step("Starting", parsed_response.get("content", ""))
                            progress.update(task, description="🧠 Planning...")
                        continue

                    elif step == "plan":
                        if not options.noreason:
                            display_step("Planning", parsed_response.get("content", ""))
                            progress.update(task, description="⚡ Taking action...")

                        continue

                    elif step == "action":
                        tool_name = parsed_response.get("function")
                        tool_input = parsed_response.get("input")

                        if not options.noreason:
                            display_tool_call(tool_name, tool_input)
                            progress.update(
                                task, description=f"🔧 Running {tool_name}..."
                            )

                        if available_tools.get(tool_name):
                            observe_output = available_tools[tool_name](tool_input)

                            messages.append(
                                {
                                    "role": "user",
                                    "content": json.dumps(
                                        {
                                            "step": "observe",
                                            "output": observe_output,
                                        }
                                    ),
                                }
                            )

                            if not options.noreason:
                                progress.update(
                                    task, description="🧠 Processing results..."
                                )

                            continue
                        else:
                            console.print(f"[red] Unknown tool: {tool_name}[/red]")
                            break

                    elif step == "result":
                        progress.stop()
                        display_result(parsed_response.get("content", ""))
                        break

                except json.JSONDecodeError as e:
                    progress.stop()
                    console.print(f"[red]❌ Failed to parse AI response: {e}[/red]")
                    break
                except Exception as e:
                    progress.stop()
                    console.print(f"[red]❌ Error: {e}[/red]")
                    break


# Make the todo in react
# Make the commit prompt more better
# and include react example
# Create video and paste it in readme.md
