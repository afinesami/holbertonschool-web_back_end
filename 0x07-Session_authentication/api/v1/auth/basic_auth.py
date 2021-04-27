#!/usr/bin/env python3
""" basic auth module
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar
from models.user import User
import base64
import binascii


class BasicAuth(Auth):
    '''self descriptive'''

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''self descriptive'''
        if authorization_header and isinstance(
                authorization_header,
                str) and authorization_header.startswith("Basic "):
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_auth_header: str) -> str:
        '''self descriptive'''
        if base64_auth_header and isinstance(
                base64_auth_header, str):
            try:
                encoded = base64_auth_header.encode('utf-8')
                base = base64.b64decode(encoded)
                return base.decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        '''self descriptive'''
        if (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ":" in decoded_base64_authorization_header):
            res = decoded_base64_authorization_header.split(":", 1)
            return (res[0], res[1])
        return (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        '''self descriptive'''
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''self descriptive'''
        auth_header = self.authorization_header(request)
        base64_sha = self.extract_base64_authorization_header(auth_header)
        decoded_sha = self.decode_base64_authorization_header(base64_sha)
        credentials = self.extract_user_credentials(decoded_sha)
        user = self.user_object_from_credentials(
            credentials[0], credentials[1])
        return user
