#!/usr/bin/env python3
"""Auth module
"""
from typing import TypeVar, List
from flask import request


class Auth():
    """Auth Class
    """
    def __init__(self) -> None:
        """initialize auth class"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Middleware to require auth"""

        if path is None or excluded_paths is None:
            return True

        normalized_path = path.rstrip('/')

        n_excluded_paths = [e_path.rstrip('/') for e_path in excluded_paths]

        if not excluded_paths:
            return True

        if normalized_path not in n_excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """middleware to authorize headers"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """middleware to check current user"""
        return None
