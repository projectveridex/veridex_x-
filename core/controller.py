"""
VERIDEX X
MASTER CONTROLLER
"""

from core.hunter_manager import run_hunters
from core.duplicate_detector import remove_duplicates
from core.proposal_engine import generate_proposal
from core.learning_engine import LearningEngine
from core.approval_queue import ApprovalQueue
from core.task_planner import TaskPlanner
from core.database import add_record
from core.scoring_engine import score_opportunity


learning = LearningEngine()
approval_queue = ApprovalQueue()
planner = TaskPlanner()

LAST_SCAN = []


def run_veridex():

    global LAST_SCAN

    opportunities = run_hunters()

    opportunities = remove_duplicates(opportunities)

    LAST_SCAN = opportunities

    for opportunity in opportunities:

        score = score_opportunity(opportunity)

        add_record({
            "title": opportunity.title,
            "source": opportunity.source,
            "score": score,
            "url": opportunity.url
        })

        proposal = generate_proposal(opportunity)

        approval_queue.add({

            "opportunity": opportunity,

            "proposal": proposal,

            "plan": planner.plan(opportunity),

            "score": score
        })

        learning.record_submission()

    return approval_queue.pending()


def get_last_scan():

    return LAST_SCAN


def get_approval_queue():

    return approval_queue
