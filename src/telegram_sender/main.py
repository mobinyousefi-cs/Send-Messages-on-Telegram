#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Telegram Message Sender
File: main.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
CLI entry point. Provides subcommands for `login`, `gui`, and `send`.

Usage:
python -m telegram_sender login
python -m telegram_sender gui
python -m telegram_sender send --to "@example" --message "Hello"
"""
from __future__ import annotations

import argparse
import sys

from .config import Settings
from .client import login as login_fn, send_message
from .gui import run_gui


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="telegram_sender", description="Telegram message sender")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("login", help="Authenticate and create a local session")
    sub.add_parser("gui", help="Launch the Tkinter GUI")

    p_send = sub.add_parser("send", help="Send a single message via CLI")
    p_send.add_argument("--to", required=True, help="username (@user), phone (+123...), or 'me'")
    p_send.add_argument("--message", required=True, help="message content")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    ns = _parse_args(argv or sys.argv[1:])

    try:
        settings = Settings.load()
    except Exception as exc:
        print(f"[config] {exc}")
        return 2

    if ns.cmd == "login":
        res = login_fn(settings)
        if res.authorized:
            print(f"[login] Authorized. Session: {res.session_path}")
            return 0
        print("[login] Not authorized; please retry.")
        return 1

    if ns.cmd == "gui":
        run_gui(settings)
        return 0

    if ns.cmd == "send":
        try:
            send_message(settings, to=ns.to, message=ns.message)
        except Exception as exc:
            print(f"[send] {exc}")
            return 1
        print("[send] Message sent.")
        return 0

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
