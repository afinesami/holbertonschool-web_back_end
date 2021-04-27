#!/usr/bin/env python3
'''hash password'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''self descriptive'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''self descriptive'''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
