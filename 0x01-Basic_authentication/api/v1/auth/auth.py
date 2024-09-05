#!/usr/bin/env python3
"""Auth module
"""
from typing import TypeVar
from flask import request


class Auth():
    """Auth Class
    """
    def __init__(self) -> None:
        """initialize auth class"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """middleware to require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """middleware to authorize headers"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """middleware to check current user"""
        return None
