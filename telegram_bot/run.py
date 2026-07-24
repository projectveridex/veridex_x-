"""
VERIDEX X
Telegram Runner
"""

from telegram_bot.bot import build_bot


def main():

    app = build_bot()

    app.run_polling()
