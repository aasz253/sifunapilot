from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class PlanStep:
    step_id: int
    tool: str
    intent: str
    arguments: Dict[str, Any] = field(default_factory=dict)
    status: str = "pending"  # pending, in_progress, completed, failed
    result: Optional[str] = None
    error: Optional[str] = None
    recoverable: bool = True


@dataclass
class TaskPlan:
    goal: str
    steps: List[PlanStep] = field(default_factory=list)
    status: str = "pending"  # pending, executing, completed, failed


class Planner:
    def __init__(self) -> None:
        pass

    def _detect_browser(self, goal_lower: str) -> str:
        if "firefox" in goal_lower:
            return "firefox"
        if "brave" in goal_lower:
            return "chromium"
        if "edge" in goal_lower or "microsoft edge" in goal_lower:
            return "chromium"
        if "safari" in goal_lower or "webkit" in goal_lower:
            return "webkit"
        return "chromium"

    def create_plan(self, goal: str) -> TaskPlan:
        plan = TaskPlan(goal=goal)
        goal_lower = goal.lower()
        steps_added = 0
        browser = self._detect_browser(goal_lower)

        if "close" in goal_lower and ("tab" in goal_lower or "window" in goal_lower):
            steps_added += 1
            plan.steps.append(PlanStep(step_id=steps_added, tool="browser.close_tab", intent="Close tab"))
            return plan

        if "open chrome" in goal_lower:
            steps_added += 1
            plan.steps.append(PlanStep(step_id=steps_added, tool="browser.open", intent="Open Chrome browser", arguments={"browser": "chromium"}))
            if "go to" in goal_lower and "google" in goal_lower:
                steps_added += 1
                plan.steps.append(PlanStep(step_id=steps_added, tool="browser.navigate", intent="Navigate to Google", arguments={"url": "https://google.com"}))
                return plan

        if "go to google" in goal_lower or goal_lower.strip() == "go to google" or "navigate to google" in goal_lower:
            if not any("open" in s.tool for s in plan.steps):
                steps_added += 1
                plan.steps.append(PlanStep(step_id=steps_added, tool="browser.open", intent="Open Chrome browser", arguments={"browser": "chromium"}))
            steps_added += 1
            plan.steps.append(PlanStep(step_id=steps_added, tool="browser.navigate", intent="Navigate to Google", arguments={"url": "https://google.com"}))
            return plan

        if "go to" in goal_lower:
            if not any("open" in s.tool for s in plan.steps):
                steps_added += 1
                plan.steps.append(PlanStep(step_id=steps_added, tool="browser.open", intent="Open Chrome browser", arguments={"browser": browser}))
            try:
                url_part = goal_lower.split("go to", 1)[-1].strip().rstrip(".")
                for sep in [" and", " then"]:
                    if sep in url_part:
                        url_part = url_part.split(sep)[0].strip()
                if url_part == "google" or "google" in url_part:
                    url = "https://google.com"
                elif url_part.startswith("http"):
                    url = url_part
                else:
                    url = f"https://{url_part}"
            except:
                url = "https://google.com"
            steps_added += 1
            plan.steps.append(PlanStep(step_id=steps_added, tool="browser.navigate", intent=f"Navigate to {url}", arguments={"url": url}))
            return plan

        if "search" in goal_lower:
            if not any("open" in s.tool for s in plan.steps):
                steps_added += 1
                plan.steps.append(PlanStep(step_id=steps_added, tool="browser.open", intent="Open Chrome browser", arguments={"browser": browser}))
            if not any("navigate" in s.tool for s in plan.steps):
                steps_added += 1
                plan.steps.append(PlanStep(step_id=steps_added, tool="browser.navigate", intent="Navigate to Google", arguments={"url": "https://google.com"}))
            query = goal
            if "search for" in goal_lower:
                query = goal_lower.split("search for")[-1].strip().rstrip(".")
            steps_added += 1
            plan.steps.append(PlanStep(step_id=steps_added, tool="browser.type", intent=f"Search for {query}", arguments={"text": query}))
            steps_added += 1
            plan.steps.append(PlanStep(step_id=steps_added, tool="browser.press_enter", intent="Submit search"))
            return plan

        if len(plan.steps) == 0:
            steps_added += 1
            plan.steps.append(PlanStep(step_id=steps_added, tool="browser.open", intent=f"Execute task: {goal}", arguments={"browser": browser}))
        return plan
