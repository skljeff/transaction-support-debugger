
def build_reply(transaction_id: str, status: str, reason: str, next_action: str) -> str:
    return f"""Hi there,

Thanks for reaching out. I checked transaction {transaction_id} and its current status is: {status}.

Reason: {reason}

Next step: {next_action}

If you have any questions, please reply to this message and we’ll be happy to help.

Kind regards,
Support Team
"""

transactions = {
    "TX1001": {
        "status": "Initiated",
        "reason": "The transfer has just been created.",
        "next_action": "No action needed. Please wait."
    },
    "TX1002": {
        "status": "Compliance Check",
        "reason": "Additional documents are required for compliance review.",
        "next_action": "Ask the customer to upload an invoice or proof of payment."
    },
    "TX1003": {
        "status": "Bank Processing",
        "reason": "The bank is currently processing the transfer.",
        "next_action": "Inform the customer to wait 1–2 business days."
    },
    "TX1004": {
        "status": "Completed",
        "reason": "The transfer has been completed successfully.",
        "next_action": "No action needed."
    },
    "TX1005": {
        "status": "Failed",
        "reason": "The bank rejected the transfer due to incorrect details.",
        "next_action": "Ask the customer to confirm their bank details."
    }
}

transaction_id = input("Enter transaction ID: ")

if transaction_id in transactions:
    tx = transactions[transaction_id]
    print("\nTransaction ID:", transaction_id)
    print("Status:", tx["status"])
    print("Reason:", tx["reason"])
    print("Next action:", tx["next_action"])
    reply = build_reply(transaction_id, tx["status"], tx["reason"], tx["next_action"])
    print("\n--- Reply Draft (Copy & Paste) ---")
    print(reply)

else:
    print("Transaction ID not found.")

