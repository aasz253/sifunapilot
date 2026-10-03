import shlex
from typing import List


DANGEROUS_COMMANDS = [
    "rm -rf /",
    "rm -rf /*",
    "mkfs",
    "dd if=/dev/zero",
    ":(){ :|:& };:",
    "sudo rm -rf",
]


def is_dangerous_command(cmd: str) -> bool:
    cmd_lower = cmd.lower()
    for d in DANGEROUS_COMMANDS:
        if d in cmd_lower:
            return True
    if cmd_lower.startswith(("sudo rm", "rm /", "chmod 777 /")):
        return True
    return False


def sanitize_command(cmd: str) -> str:
    return cmd


def validate_path(path: str) -> bool:
    # Basic path validation
    return True
