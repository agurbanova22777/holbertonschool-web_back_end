#!/usr/bin/env python3
"""Log statistics script"""

from pymongo import MongoClient


def log_stats():
    """Print statistics about nginx logs."""

    client = MongoClient("mongodb://localhost:27017")
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    print("Methods: ")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
       count = nginx_collection.count_documents(
          {"methods": method}
       )
        print("\tmethod {}: {}".format(method, count))

    status_count = nginx_collection.count_documents(
        {
            "method": "GET",
            "path": "/status"
        }
    )

    print("{}".format(status_count))

if __name__ == "__main__":
    log_stats()
