"""
VERIDEX X
EXECUTION ENGINE
"""

from core.workflow_router import detect_workflow


def execute(approved):

    opportunity = approved["opportunity"]

    workflow = detect_workflow(opportunity)

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
