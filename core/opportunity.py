"""
VERIDEX X
Opportunity Model
"""


class Opportunity:

    def __init__(
        self,
        title,
        source,
        url="",
        description=""
    ):

        self.title = title
        self.source = source
        self.url = url
        self.description = description

        self.status = "NEW"
