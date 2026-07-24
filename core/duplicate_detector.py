"""
VERIDEX X
SMART DUPLICATE DETECTOR
"""

import re


def normalize(text):

    text = text.lower()

    text = re.sub(r"[^a-z0-9 ]", "", text)

    text = " ".join(text.split())

    return text


def remove_duplicates(opportunities):

    seen_titles = set()
    seen_urls = set()

    unique = []

    for item in opportunities:

        title = normalize(getattr(item, "title", ""))

        source = getattr(item, "source", "")

        url = getattr(item, "url", "")

        repo = ""

        if "github.com" in url:

            parts = url.split("/")

            if len(parts) >= 5:

                repo = f"{parts[3]}/{parts[4]}"

        title_key = (repo, title)

        if url in seen_urls:

            continue

        if title_key in seen_titles:

            continue

        seen_urls.add(url)

        seen_titles.add(title_key)

        unique.append(item)

    return unique
