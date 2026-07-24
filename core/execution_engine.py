"""
VERIDEX X
EXECUTION ENGINE
"""

from core.job_classifier import classify

def execute(job):

    opportunity = job["opportunity"]

    job_type = classify(opportunity)

    return {
        "status": "READY",
        "job_type": job_type,
        "workflow_steps": [
            "Analyze task",
            "Prepare proposal",
            "Prepare execution plan",
            "Await confirmation"
        ]
    }
