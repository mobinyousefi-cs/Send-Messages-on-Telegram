#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Telegram Message Sender
File: __main__.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-18
Updated: 2025-10-18
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Module entrypoint to enable `python -m telegram_sender ...`.
"""
from .main import main

if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
