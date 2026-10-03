from enum import Enum
from typing import Dict

from pydantic import BaseModel, Field


class PermissionLevel(str, Enum):
    SAFE = "safe"
    CONFIRM = "confirm"
    RESTRICTED = "restricted"
    BLOCKED = "blocked"


class PermissionPolicy(BaseModel):
    browser_navigation: PermissionLevel = Field(default=PermissionLevel.SAFE)
    browser_click: PermissionLevel = Field(default=PermissionLevel.SAFE)
    browser_type: PermissionLevel = Field(default=PermissionLevel.SAFE)
    browser_upload: PermissionLevel = Field(default=PermissionLevel.CONFIRM)
    social_post: PermissionLevel = Field(default=PermissionLevel.CONFIRM)
    email_send: PermissionLevel = Field(default=PermissionLevel.CONFIRM)
    file_read: PermissionLevel = Field(default=PermissionLevel.SAFE)
    file_write: PermissionLevel = Field(default=PermissionLevel.CONFIRM)
    file_delete: PermissionLevel = Field(default=PermissionLevel.CONFIRM)
    terminal: PermissionLevel = Field(default=PermissionLevel.CONFIRM)
    sudo: PermissionLevel = Field(default=PermissionLevel.BLOCKED)
    financial_transactions: PermissionLevel = Field(default=PermissionLevel.BLOCKED)
    app_launch: PermissionLevel = Field(default=PermissionLevel.SAFE)
    app_close: PermissionLevel = Field(default=PermissionLevel.CONFIRM)


def get_policy() -> PermissionPolicy:
    return PermissionPolicy()
