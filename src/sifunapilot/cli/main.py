from typing import Optional

import typer
from rich.console import Console

from sifunapilot.cli import commands
from sifunapilot.cli.display import print_welcome

app = typer.Typer(
    name="sifunapilot",
    help="SifunaPilot - Your computer. Your commands. Your AI.",
    no_args_is_help=True,
)

console = Console()


@app.callback()
def callback() -> None:
    """SifunaPilot CLI"""
    pass


@app.command()
def start(voice: bool = typer.Option(False, "--voice", help="Start with voice mode")):
    """Start interactive mode"""
    print_welcome()
    commands.cmd_start(voice=voice)


@app.command()
def stop():
    """Stop SifunaPilot"""
    commands.cmd_stop()


@app.command()
def status():
    """Show status"""
    commands.cmd_status()


@app.command()
def ask(query: str = typer.Argument(..., help="Task to execute")):
    """Execute a single task"""
    commands.cmd_ask(query)


@app.command()
def config():
    """Show configuration"""
    from sifunapilot.config.settings import get_settings

    settings = get_settings()
    console.print(settings.model_dump_json(indent=2))


@app.command()
def providers():
    """List available AI providers"""
    commands.cmd_providers()


@app.command()
def tools():
    """List available tools"""
    commands.cmd_tools()


@app.command()
def permissions():
    """Show permission settings"""
    from sifunapilot.permissions.policy import get_policy

    console.print(get_policy().model_dump_json(indent=2))


@app.command()
def history():
    """Show task history"""
    console.print("[yellow]History (stub - implementation pending)[/yellow]")


@app.command()
def logs():
    """Show logs"""
    console.print("[yellow]Logs (stub - implementation pending)[/yellow]")


@app.command()
def doctor():
    """Run health check"""
    commands.cmd_doctor()


@app.command()
def voice_start():
    """Start voice mode"""
    print_welcome()
    commands.cmd_start(voice=True)


@app.command()
def voice_stop():
    """Stop voice mode"""
    commands.cmd_stop()
