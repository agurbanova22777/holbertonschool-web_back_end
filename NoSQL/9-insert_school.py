#!/usr/bin/env python3
"""module for mongodb"""


def insert_school(mongo_collection, **kwargs):
    """insert a new doc"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
