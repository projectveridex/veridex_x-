"""
VERIDEX X
Duplicate Detector
"""


def remove_duplicates(opportunities):

    seen = set()

    result = []

    for item in opportunities:

        key = (item.title, item.source)

        if key not in seen:

            seen.add(key)

            result.append(item)

    return result
