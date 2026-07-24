from payments.payment_config import PAYMENT_METHODS


def payment_message():

    message = "💳 VERIDEX PAYMENT METHODS\n\n"

    for name, info in PAYMENT_METHODS.items():

        message += (
            f"{name}\n"
            f"Network: {info['network']}\n"
            f"Address:\n"
            f"{info['address']}\n\n"
        )

    return message
