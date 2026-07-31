def check_payment(func):
    def wrapper(status):
        if status.lower() == "completed":
            print("Payment Completed")
        elif status.lower() == "pending":
            print("Payment Pending")
        elif status.lower() == "failed":
            print("Payment Failed")
        else:
            print("Invalid Payment Status")

        return func(status)
    return wrapper


@check_payment
def payment_status(status):
    print("Payment status checked successfully.")


payment_status("completed")
print()

payment_status("pending")
print()

payment_status("failed")