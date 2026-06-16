#!/usr/bin/env python3
"""module for mongodb"""


def schools_by_topic(mongo_collection, topic):
    """find by topic"""
    return list(mongo_collection.find(
        {"topics": topic}
    ))
