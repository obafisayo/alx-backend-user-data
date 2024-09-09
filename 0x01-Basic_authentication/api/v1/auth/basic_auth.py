#!/usr/bin/env python3
''' Basic Auth module
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ creates a basic authorization for the user"""

    def __init__(self) -> None:
        """initialize auth class"""
        super().__init__()
        pass
