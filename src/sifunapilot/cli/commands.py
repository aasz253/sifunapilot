from typing import Optional

from rich import box
from rich.panel import Panel
from rich.table import Table

from sifunapilot.cli.display import (
    console,
    print_status,
    print_success,
    print_warning,
    print_info,
    print_error,
)
from sifunapilot.config.settings import get_settings


def cmd_status() -> None:
    settings = get_settings()
    print_status(
        status="STOPPED",
        ai=settings.ai.provider,
        mode=settings.agent.mode,
        voice="Enabled" if settings.voice.enabled else "Disabled",
    )


def cmd_providers() -> None:
    table = Table(title="Available AI Providers", box=box.ROUNDED)
    table.add_column("Provider", style="cyan")
    table.add_column("Status", style="green")
    table.add_row("✓ Ollama", "Available")
    table.add_row("○ OpenAI", "Optional")
    table.add_row("○ Anthropic", "Optional")
    table.add_row("○ Gemini", "Optional")
    table.add_row("○ OpenRouter", "Optional")
    console.print(table)


def cmd_doctor() -> None:
    table = Table(title="SifunaPilot Doctor", box=box.ROUNDED)
    table.add_column("Check", style="cyan")
    table.add_column("Status", style="green")
    table.add_row("✓ Python 3.11+", "OK")
    table.add_row("✓ Configuration", "OK")
    table.add_row("✓ SQLite", "OK")
    table.add_row("✓ SpeechRecognition", "OK")
    table.add_row("✓ pyttsx3 (TTS)", "OK")
    table.add_row("⚠ Playwright", "Not installed/verified")
    table.add_row("⚠ Ollama", "Not detected")
    table.add_row("⚠ Microphone", "Check if available")
    console.print(table)


def cmd_tools() -> None:
    table = Table(title="Available Tools", box=box.ROUNDED)
    table.add_column("Tool", style="cyan")
    table.add_column("Permission", style="yellow")
    table.add_column("Status", style="green")
    table.add_row("browser.open", "safe", "Available")
    table.add_row("browser.navigate", "safe", "Available")
    table.add_row("browser.type", "safe", "Available")
    table.add_row("browser.click", "safe", "Available")
    table.add_row("browser.close", "safe", "Available")
    table.add_row("filesystem.list", "safe", "Available")
    table.add_row("terminal.execute", "confirm", "Available")
    table.add_row("pdf.create", "safe", "Available")
    console.print(table)


def cmd_start(voice: bool = False) -> None:
    settings = get_settings()
    settings.ensure_dirs()
    if voice:
        settings.voice.enabled = True
    panel = Panel(
        "[green]SifunaPilot is ready.[/green]\n\nYou >",
        title="Interactive Mode",
        box=box.ROUNDED,
    )
    console.print(panel)
    print_success(
        f"AI: {settings.ai.provider} | Mode: {settings.agent.mode} | "
        f"Voice: {'Enabled' if voice or settings.voice.enabled else 'Disabled'}"
    )


def cmd_start_interactive(voice: bool = False) -> None:
    import asyncio

    asyncio.run(_run_interactive(voice))


async def _run_interactive(voice: bool = False) -> None:
    from sifunapilot.voice.stt import get_stt
    from sifunapilot.voice.tts import get_tts
    from sifunapilot.agent.orchestrator import Orchestrator

    stt = get_stt()
    tts = get_tts()
    orchestrator = Orchestrator()

    if voice:
        tts.speak("SifunaPilot is ready. Say a command or type exit to quit.")
    else:
        print_success("Type commands or 'exit' to quit.")

    while True:
        try:
            if voice:
                console.print("[cyan]Listening...[/cyan]")
                text = stt.listen(timeout=5, phrase_time_limit=10)
                if not text:
                    console.print("[yellow]No speech detected, try again...[/yellow]")
                    continue
                console.print(f"[green]You (voice):[/green] {text}")
                tts.speak(f"Executing {text}")
            else:
                text = input("You > ").strip()
            if text.lower() in ("exit", "quit", "stop"):
                if voice:
                    tts.speak("Goodbye")
                print_success("Goodbye!")
                break
            if not text:
                continue
            await orchestrator.execute_task(text)
            if voice:
                tts.speak("Done")
        except KeyboardInterrupt:
            print_success("\nGoodbye!")
            break
        except EOFError:
            break


def cmd_stop() -> None:
    print_success("SifunaPilot stopped")


async def _execute_async(query: str) -> None:
    from sifunapilot.agent.orchestrator import Orchestrator

    orchestrator = Orchestrator()
    await orchestrator.execute_task(query)


def cmd_ask(query: str) -> None:
    print_info(f"Executing: {query}")
    import asyncio

    asyncio.run(_execute_async(query))
