"""
Utility module to manipulate queries

This module exports the requested implementation to the rest of the package.
"""

# Copyright (C) 2023 The Psycopg Team

from typing import Type
from . import abc

from . import _queries_py

PostgresQuery: Type[abc.PostgresQuery]
PostgresClientQuery: Type[abc.PostgresQuery]


PostgresQuery = _queries_py.PostgresQuery
PostgresClientQuery = _queries_py.PostgresClientQuery

# Exposed only for testing purposes
_split_query = _queries_py._split_query
