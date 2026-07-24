"""
VERIDEX X
RSS Hunter
"""

from hunters.github_live_hunter import Opportunity


def scan_rss():

    return [
        Opportunity(
            "Website Needs Fix",
            "RSS"
        )
    ]
