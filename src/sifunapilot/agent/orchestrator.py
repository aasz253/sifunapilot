from typing import Any, Dict, Optional

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from sifunapilot.agent.planner import Planner, TaskPlan
from sifunapilot.tools.browser import BrowserTools
from sifunapilot.tools.filesystem import FileSystemTools
from sifunapilot.tools.pdf import PDFTools
from sifunapilot.tools.terminal import TerminalTools
from sifunapilot.tools.applications import ApplicationTools
from sifunapilot.tools.registry import Tool, ToolRegistry

console = Console()


class Orchestrator:
    def __init__(self) -> None:
        self.planner = Planner()
        self.registry = ToolRegistry()
        self.browser_tools = BrowserTools()
        self.fs_tools = FileSystemTools()
        self.pdf_tools = PDFTools()
        self.term_tools = TerminalTools()
        self.app_tools = ApplicationTools()
        self._register_tools()

    def _register_tools(self) -> None:
        self.registry.register(
            Tool(
                name="browser.open",
                description="Open browser",
                permission="safe",
                executor=self.browser_tools.open_browser,
            )
        )
        self.registry.register(
            Tool(
                name="browser.close",
                description="Close browser",
                permission="safe",
                executor=self.browser_tools.close_browser,
            )
        )
        self.registry.register(
            Tool(
                name="browser.navigate",
                description="Navigate to URL",
                permission="safe",
                executor=self.browser_tools.navigate,
            )
        )
        self.registry.register(
            Tool(
                name="browser.type",
                description="Type text",
                permission="safe",
                executor=self.browser_tools.type_text,
            )
        )
        self.registry.register(
            Tool(
                name="browser.press_enter",
                description="Press Enter",
                permission="safe",
                executor=self.browser_tools.press_enter,
            )
        )
        self.registry.register(
            Tool(
                name="browser.click",
                description="Click element",
                permission="safe",
                executor=self.browser_tools.click,
            )
        )
        self.registry.register(
            Tool(
                name="browser.new_tab",
                description="Open new tab",
                permission="safe",
                executor=self.browser_tools.new_tab,
            )
        )
        self.registry.register(
            Tool(
                name="browser.close_tab",
                description="Close tab",
                permission="safe",
                executor=self.browser_tools.close_tab,
            )
        )
        self.registry.register(
            Tool(
                name="browser.screenshot",
                description="Take screenshot",
                permission="safe",
                executor=self.browser_tools.screenshot,
            )
        )
        self.registry.register(
            Tool(
                name="filesystem.list",
                description="List files",
                permission="safe",
                executor=self.fs_tools.list_files,
            )
        )
        self.registry.register(
            Tool(
                name="filesystem.read",
                description="Read file",
                permission="safe",
                executor=self.fs_tools.read_file,
            )
        )
        self.registry.register(
            Tool(
                name="filesystem.write",
                description="Write file",
                permission="confirm",
                executor=self.fs_tools.write_file,
            )
        )
        self.registry.register(
            Tool(
                name="pdf.create",
                description="Create PDF",
                permission="safe",
                executor=self.pdf_tools.create_pdf,
            )
        )

    async def execute_task(self, goal: str) -> Dict[str, Any]:
        console.print("[cyan]Planning...[/cyan]")
        plan = self.planner.create_plan(goal)

        if plan.steps:
            table = Table(box=box.ROUNDED, show_header=False)
            table.add_column("Step", style="cyan")
            table.add_column("Tool", style="yellow")
            table.add_column("Intent", style="white")
            for i, step in enumerate(plan.steps, 1):
                table.add_row(str(i), step.tool, step.intent)
            console.print(table)

        console.print("[cyan]Executing...[/cyan]")
        for step in plan.steps:
            tool = self.registry.get(step.tool)
            if tool:
                console.print(
                    f"[cyan]→ Executing {step.tool}...[/cyan]"
                )
                try:
                    result = await tool.execute(**step.arguments)
                    step.status = "completed"
                    step.result = str(result)
                    console.print(f"[green]✓ {result}[/green]")
                except Exception as e:
                    step.status = "failed"
                    step.error = str(e)
                    console.print(f"[red]✗ Failed: {e}[/red]")
            else:
                console.print(f"[red]✗ Tool not found: {step.tool}[/red]")

        console.print("[green]✓ Task completed[/green]")
        return {"goal": goal, "plan": plan}
