#!/usr/bin/env python3
""" pymongo
"""


def update_topics(mongo_collection, name, topics):
    """ function that changes all topics of a school
        document based on the name
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
