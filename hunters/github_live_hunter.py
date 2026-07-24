"""
VERIDEX X
GitHub Hunter
"""

class Opportunity:

    def __init__(self, title, source):

        self.title = title
        self.source = source


def scan_github_live():

    return [
        Opportunity(
            "WordPress Plugin Bug",
            "GitHub"
        )
    ]
