from typing import Optional

import typer
from rich.console import Console

from sifunapilot.cli import commands
from sifunapilot.cli.display import print_welcome, print_info, print_success, console
from sifunapilot import __version__
from sifunapilot.voice.stt import get_stt
from sifunapilot.voice.tts import get_tts

app = typer.Typer(
    name="sifunapilot",
    help="SifunaPilot - Your computer. Your commands. Your AI.",
    no_args_is_help=False,
)

console_obj = Console()


@app.callback()
def callback() -> None:
    pass


@app.command()
def version() -> None:
    console_obj.print(f"SifunaPilot v{__version__}")


@app.command()
def start(voice: bool = typer.Option(False, "--voice", help="Start with voice mode")):
    """Start interactive mode"""
    print_welcome()
    console.print("\n[cyan]Options:[/cyan]")
    console.print("1. Continue in text mode")
    console.print("2. Use voice mode (with microphone)")
    try:
        choice = input("\nSelect option (1 or 2): ").strip()
    except:
        choice = "1"
    if choice == "2":
        voice = True
    if voice:
        console.print("[green]Voice mode enabled. Speak your command after the prompt.[/green]")
        tts = get_tts()
        tts.speak("Voice mode active. I am listening.")
    commands.cmd_start_interactive(voice=voice)


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
    console_obj.print(settings.model_dump_json(indent=2))


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
    console_obj.print(get_policy().model_dump_json(indent=2))


@app.command()
def history():
    """Show task history"""
    console_obj.print("[yellow]History (stub - implementation pending)[/yellow]")


@app.command()
def logs():
    """Show logs"""
    console_obj.print("[yellow]Logs (stub - implementation pending)[/yellow]")


@app.command()
def doctor():
    """Run health check"""
    commands.cmd_doctor()


@app.command()
def voice_start():
    """Start voice mode"""
    print_welcome()
    commands.cmd_start_interactive(voice=True)


@app.command()
def voice_stop():
    """Stop voice mode"""
    commands.cmd_stop()
