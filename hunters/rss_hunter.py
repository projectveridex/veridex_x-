"""
VERIDEX X
RSS Live Hunter
"""

import feedparser

from core.opportunity import Opportunity


RSS_FEEDS = [
    "https://www.reddit.com/r/forhire/.rss",
    "https://www.reddit.com/r/webdev/.rss",
    "https://www.reddit.com/r/Wordpress/.rss"
]


def scan_rss():

    opportunities = []


    for feed_url in RSS_FEEDS:

        try:

            feed = feedparser.parse(
                feed_url
            )


            for entry in feed.entries[:10]:

                title = getattr(
                    entry,
                    "title",
                    "Untitled Opportunity"
                )

                link = getattr(
                    entry,
                    "link",
                    ""
                )

                description = getattr(
                    entry,
                    "summary",
                    ""
                )


                opportunities.append(

                    Opportunity(
                        title=title,
                        source="RSS",
                        url=link,
                        description=description[:200]
                    )

                )


        except Exception:

            continue


    return opportunities
