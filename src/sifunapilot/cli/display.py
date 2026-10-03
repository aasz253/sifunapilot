from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def print_welcome() -> None:
    welcome = Panel(
        "Your computer. Your commands. Your AI.",
        title="SIFUNAPILOT",
        box=box.DOUBLE,
        padding=(1, 2),
    )
    console.print(welcome)


def print_status(
    status: str = "STOPPED",
    ai: str = "Ollama",
    mode: str = "Assist",
    voice: str = "Disabled",
    browser: str = "READY",
    desktop: str = "READY",
) -> None:
    table = Table(title="SifunaPilot Status", box=box.ROUNDED)
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Status", status)
    table.add_row("Mode", mode)
    table.add_row("AI", ai)
    table.add_row("Voice", voice)
    table.add_row("Browser", browser)
    table.add_row("Desktop", desktop)
    console.print(table)


def print_success(message: str) -> None:
    console.print(f"✓ {message}", style="green")


def print_info(message: str) -> None:
    console.print(f"→ {message}", style="cyan")


def print_warning(message: str) -> None:
    console.print(f"⚠ {message}", style="yellow")


def print_error(message: str) -> None:
    console.print(f"✗ {message}", style="red")
