from rich.console import Console

from agent.setup import setup

console = Console()


def main():
    try:
        setup()
    except KeyboardInterrupt:
        console.print("\n[bold magenta]Thanks for using GhoulCli[/bold magenta]")
    except Exception as e:
        console.print(
            f"[bold red]Fatal error: {str(e)}[/bold red]",
        )
        raise


if __name__ == "__main__":
    main()

# Add websearch with tavily
