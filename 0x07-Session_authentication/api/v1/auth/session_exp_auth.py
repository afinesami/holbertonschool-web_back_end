#!/usr/bin/env python3
""" session expiration
"""

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """ self descriptive
    """

    def __init__(self):
        """ init method
        """
        self.session_duration = 0
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            pass

    def create_session(self, user_id=None):
        """ Creates a Session id
        """
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        if not user_id:
            return None
        session_dictionary = {'user_id': user_id, 'created_at': datetime.now()}
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ self descriptive
        """
        if not session_id:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary:
            user = session_dictionary.get('user_id')
            if user:
                if self.session_duration <= 0:
                    return user
                created_at = session_dictionary.get('created_at')
                if created_at is None:
                    return None
                if (created_at + timedelta(seconds=self.session_duration) <
                        datetime.now()):
                    return None
                return user
