#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Telegram Message Sender
File: config.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Configuration utilities: load API keys and session paths from environment (.env supported).

Usage:
from telegram_sender.config import Settings
settings = Settings.load()
print(settings.api_id)

Notes:
- Uses python-dotenv if a .env file is present.
- Resolves platform-specific config directory for session storage by default.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
from typing import Optional

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover - optional at runtime
    def load_dotenv(*_args, **_kwargs):  # type: ignore
        return False


@dataclass(frozen=True)
class Settings:
    api_id: int
    api_hash: str
    phone: Optional[str]
    session_name: str
    session_dir: Path

    @staticmethod
    def default_session_dir() -> Path:
        """Return a platform-appropriate directory for storing Telethon sessions."""
        # Respect XDG on *nix; use AppData on Windows
        if os.name == "nt":
            base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
        else:
            base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
        return base / "telegram_sender"

    @classmethod
    def load(cls) -> "Settings":
        """Load settings from environment (supports .env)."""
        load_dotenv()

        api_id_str = os.environ.get("API_ID")
        api_hash = os.environ.get("API_HASH")
        phone = os.environ.get("PHONE") or None
        session_name = os.environ.get("SESSION_NAME", "telegram_sender")
        session_dir_env = os.environ.get("SESSION_DIR")
        session_dir = Path(session_dir_env) if session_dir_env else cls.default_session_dir()

        if not api_id_str or not api_hash:
            raise ValueError(
                "Missing API_ID or API_HASH. Set them in environment or .env file."
            )

        api_id = int(api_id_str)
        session_dir.mkdir(parents=True, exist_ok=True)
        return cls(
            api_id=api_id,
            api_hash=api_hash,
            phone=phone,
            session_name=session_name,
            session_dir=session_dir,
        )

    def session_path(self) -> Path:
        return self.session_dir / f"{self.session_name}.session"
