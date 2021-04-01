#!/usr/bin/env python3
''' Module of Basic_auth
'''
import base64
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    ''' BasicAuth class
    '''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' def extract base64 authorization header '''
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header.startswith("Basic "):
            return "".join(authorization_header.split(" ")[1:])

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' def decode base 64 authorization '''
        if base64_authorization_header and type(
                    base64_authorization_header) == str:
            try:
                x = base64_authorization_header.encode('utf-8')
                base = base64.b64decode(x)
                return base.decode('utf-8')
            except Exception:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' return the user mail and the password '''
        c = decoded_base64_authorization_header
        if c and type(c) == str and ":" in c:
            mail = c.split(':')[0]
            password = "".join(c.split(':', 1)[1:])
            return(mail, password)
        return(None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        ''' def user object from credentials '''
        if type(user_email) != str:
            return None
        if type(user_pwd) != str:
            return None
        if user_email and user_pwd:
            users = User.search({"email": user_email})
            for user in users:
                if user and user.is_valid_password(user_pwd):
                    return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' complete basic Authentification '''
        if request:
            auth_head = self.authorization_header(request)
            extract = self.extract_base64_authorization_header(auth_head)
            decode = self.decode_base64_authorization_header(extract)
            (email, password) = self.extract_user_credentials(decode)
            return self.user_object_from_credentials(email, password)
