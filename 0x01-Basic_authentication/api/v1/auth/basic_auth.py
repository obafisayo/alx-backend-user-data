#!/usr/bin/env python3
''' Basic Auth module
'''
from api.v1.auth.auth import Auth
import base64


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

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode base64 authorization header
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(
                base64_authorization_header, validate=True)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
