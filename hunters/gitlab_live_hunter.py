"""
VERIDEX X
GitLab Hunter
"""

from hunters.github_live_hunter import Opportunity


def scan_gitlab_live():

    return [
        Opportunity(
            "Python Automation Task",
            "GitLab"
        )
    ]
