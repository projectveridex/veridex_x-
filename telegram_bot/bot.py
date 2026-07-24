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
    await update.message.reply_text(dashboard())


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("🔍 Scanning...")

    run_veridex()

    jobs = get_last_scan()

    await update.message.reply_text(
        f"✅ Found {len(jobs)} opportunities.\nUse /jobs"
    )


async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):

    jobs = get_last_scan()

    if not jobs:

        await update.message.reply_text(
            "No scan yet."
        )

        return

    message = "📋 Jobs\n\n"

    for i, job in enumerate(jobs, start=1):

        message += f"{i}. {job.title} ({job.source})\n"

    message += "\nUse /approve <number>"

    await update.message.reply_text(message)


async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:

        await update.message.reply_text(
            "Usage: /approve 1"
        )

        return

    index = int(context.args[0]) - 1

    queue = get_approval_queue()

    approved = queue.approve(index)

    if approved is None:

        await update.message.reply_text(
            "Invalid selection."
        )

        return

    result = execute(approved)

    await update.message.reply_text(
        f"""✅ APPROVED

Job:
{approved['opportunity'].title}

Workflow:
{result['job_type']}

Status:
{result['status']}
"""
    )


def build_bot():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(CommandHandler("jobs", jobs))
    app.add_handler(CommandHandler("approve", approve))

    return app
