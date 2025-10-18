#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Telegram Message Sender
File: client.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Thin wrapper around Telethon for login and sending messages. The functions are synchronous
for easy integration with Tkinter; under the hood they run async coroutines.

Usage:
from telegram_sender.client import login, send_message
login(settings)
send_message(settings, to="@example_user", message="Hello")
"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from telethon import TelegramClient

from .config import Settings


@dataclass
class LoginResult:
    session_path: Path
    authorized: bool


def _client(settings: Settings) -> TelegramClient:
    return TelegramClient(
        str(settings.session_path()), settings.api_id, settings.api_hash
    )


def login(settings: Settings) -> LoginResult:
    """Interactive login in the terminal. Returns when session is saved."""
    async def _run() -> LoginResult:
        async with _client(settings) as client:
            await client.start(phone=settings.phone)
            return LoginResult(settings.session_path(), await client.is_user_authorized())

    return asyncio.run(_run())


def send_message(settings: Settings, to: str, message: str) -> None:
    """Send a message using an existing session. Raises on auth errors.

    Args:
        settings: loaded configuration
        to: username ("@user"), phone ("+123..."), or "me" for Saved Messages
        message: text content
    """

    async def _run() -> None:
        async with _client(settings) as client:
            if not await client.is_user_authorized():
                raise RuntimeError(
                    "Session is not authorized. Run 'python -m telegram_sender login' first."
                )
            entity = to
            await client.send_message(entity, message)

    asyncio.run(_run())
