"""
VERIDEX X
Opportunity Scoring
"""


def score_opportunity(opportunity):

    score = 50

    text = (
        opportunity.title +
        " " +
        opportunity.description
    ).lower()


    if "urgent" in text:
        score += 15

    if "bug" in text:
        score += 10

    if "help wanted" in text:
        score += 10

    if "automation" in text:
        score += 10


    return min(score, 100)
