#!/usr/bin/env python3
""" auth module
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    '''self descriptive'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''self descriptive'''
        if not path or not excluded_paths:
            return True

        path += '/' if path[-1] != '/' else ''
        wildcard = any(rex.endswith("*") for rex in excluded_paths)

        if not wildcard:
            if path in excluded_paths:
                return False

        for rex in excluded_paths:
            if rex[-1] == '*':
                if path.startswith(rex[:-1]):
                    return False
            if rex == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        '''self descriptive'''
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        '''self descriptive'''
        return None

    def session_cookie(self, request=None):
        '''self descriptive'''
        if not request:
            return None

        session_name = os.getenv("SESSION_NAME")
        return request.cookies.get(session_name)
