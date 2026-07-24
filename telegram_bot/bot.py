"""
VERIDEX X
TELEGRAM CONTROL BOT
"""

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from telegram_bot.config import BOT_TOKEN
from telegram_bot.dashboard import dashboard

from core.controller import (
    run_veridex,
    get_last_scan,
    get_approval_queue
)

from core.execution_engine import execute


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        dashboard()
    )


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔍 VERIDEX is scanning live sources..."
    )

    run_veridex()

    jobs = get_last_scan()

    await update.message.reply_text(
        f"""
🔥 VERIDEX REPORT

Live Opportunities Found:
{len(jobs)}

Use /jobs to view them.
"""
    )


async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):

    jobs = get_last_scan()

    if not jobs:

        await update.message.reply_text(
            "No scan yet."
        )

        return


    message = """
📋 VERIDEX LIVE OPPORTUNITIES

"""


    for i, job in enumerate(jobs, start=1):

        message += (
            f"{i}. {job.title}\n"
            f"🌐 Source: {job.source}\n"
            f"⭐ Score: {getattr(job, 'score', 'N/A')}/100\n\n"
        )


    message += "Use /approve <number>"


    await update.message.reply_text(
        message
    )


async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:

        await update.message.reply_text(
            "Usage: /approve 1"
        )

        return


    try:

        index = int(context.args[0]) - 1

    except ValueError:

        await update.message.reply_text(
            "Please use a number."
        )

        return


    queue = get_approval_queue()

    approved = queue.approve(index)


    if approved is None:

        await update.message.reply_text(
            "Invalid selection."
        )

        return


    result = execute(approved)


    opportunity = approved["opportunity"]


    message = f"""
✅ APPROVED

Job:
{opportunity.title}

Engine:
{result.get('engine', result.get('job_type', 'general'))}

Status:
{result.get('status', 'READY')}
"""


    if "confidence" in result:

        message += (
            f"\nConfidence:\n"
            f"{result['confidence']}%\n"
        )


    if "estimated_time" in result:

        message += (
            f"\n⏱ Estimated Time:\n"
            f"{result['estimated_time']}\n"
        )


    if "diagnosis" in result:

        message += "\n🔍 Diagnosis\n"

        for item in result["diagnosis"]:

            message += f"• {item}\n"



    if "execution_plan" in result:

        message += "\n🛠 Execution Plan\n"

        for step in result["execution_plan"]:

            message += f"• {step}\n"



    if "deliverables" in result:

        message += "\n📦 Deliverables\n"

        for item in result["deliverables"]:

            message += f"• {item}\n"


    await update.message.reply_text(
        message
    )




def build_bot():

    app = Application.builder().token(
        BOT_TOKEN
    ).build()


    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("scan", scan)
    )

    app.add_handler(
        CommandHandler("jobs", jobs)
    )

    app.add_handler(
        CommandHandler("approve", approve)
    )


    return app
