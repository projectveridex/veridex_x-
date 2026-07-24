"""
VERIDEX X
JOB CLASSIFIER
"""

def classify(opportunity):

    title = opportunity.title.lower()

    if "wordpress" in title:
        return "wordpress"

    if "python" in title:
        return "python"

    if "bug" in title:
        return "bugfix"

    return "general"
