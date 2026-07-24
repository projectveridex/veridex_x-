"""
VERIDEX X
EXECUTION ENGINE
"""

from core.workflow_router import detect_workflow
from core.wordpress_engine import analyze as wordpress_analyze


def execute(approved):

    opportunity = approved["opportunity"]

    workflow = detect_workflow(opportunity)

    if workflow.name == "wordpress":

        result = wordpress_analyze(opportunity)

        return result

    return {
        "status": "READY",
        "job_type": workflow.name,
        "engine": workflow.execution_module,
        "confidence": workflow.confidence,
        "workflow_steps": [
            "Analyze task",
            f"Select engine: {workflow.execution_module}",
            "Prepare proposal",
            "Prepare execution plan",
            "Await confirmation"
        ]
    }
