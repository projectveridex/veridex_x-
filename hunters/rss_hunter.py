"""
VERIDEX X
RSS Live Hunter
"""

import feedparser

from core.opportunity import Opportunity


RSS_FEEDS = [
    "https://www.reddit.com/r/forhire/.rss",
    "https://www.reddit.com/r/webdev/.rss"
]


def scan_rss():

    opportunities = []

    for feed_url in RSS_FEEDS:

        try:

            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:5]:

                opportunities.append(
                    Opportunity(
                        title=entry.title,
                        source="RSS",
                        url=entry.link,
                        description=getattr(
                            entry,
                            "summary",
                            ""
                        )[:200]
                    )
                )

        except Exception:

            continue

    return opportunities
