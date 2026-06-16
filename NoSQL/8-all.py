#!/usr/bin/env python3
"""module for mongodb operations"""


def list_all(mongo_collection):
    """List all docs"""
    return list(mongo_collection.find())
