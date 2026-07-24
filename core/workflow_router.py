from dataclasses import dataclass

@dataclass
class Workflow:

    name: str
    confidence: int
    execution_module: str


def detect_workflow(job):

    text = (
        f"{job.title} {getattr(job,'description','')}"
    ).lower()

    if any(x in text for x in [
        "wordpress",
        "plugin",
        "woocommerce",
        "theme",
        "elementor"
    ]):
        return Workflow(
            "wordpress",
            95,
            "wordpress_engine"
        )

    if any(x in text for x in [
        "python",
        "django",
        "flask",
        "fastapi"
    ]):
        return Workflow(
            "python",
            95,
            "python_engine"
        )

    if any(x in text for x in [
        "api",
        "rest",
        "json",
        "endpoint"
    ]):
        return Workflow(
            "api",
            90,
            "api_engine"
        )

    if any(x in text for x in [
        "scrape",
        "crawler",
        "selenium",
        "beautifulsoup"
    ]):
        return Workflow(
            "scraping",
            92,
            "scraping_engine"
        )

    if any(x in text for x in [
        "excel",
        "spreadsheet",
        "data entry",
        "typing"
    ]):
        return Workflow(
            "data",
            80,
            "data_engine"
        )

    return Workflow(
        "general",
        50,
        "general_engine"
    )
