"""
compatibility functions for different Python versions
"""

# Copyright (C) 2021 The Psycopg Team

import sys

if sys.version_info >= (3, 11):
    from typing import LiteralString, Self
else:
    from typing_extensions import LiteralString, Self

if sys.version_info >= (3, 12):
    _asyncio_run_snippet = (
        "running 'asyncio.run(...,"
        " loop_factory=asyncio.SelectorEventLoop(selectors.SelectSelector()))'"
    )

else:
    _asyncio_run_snippet = (
        "setting 'asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())'"
    )

if sys.version_info >= (3, 13):
    from typing import TypeVar
else:
    from typing_extensions import TypeVar

__all__ = [
    "LiteralString",
    "Self",
    "TypeVar",
]
