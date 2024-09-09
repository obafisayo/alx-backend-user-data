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

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ extract base64 authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.split()[0] is not "Basic":
            return None
        return authorization_header.split()[1]
