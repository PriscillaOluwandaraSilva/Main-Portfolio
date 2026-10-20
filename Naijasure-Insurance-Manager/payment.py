
from datetime import datetime

class Payment:
    """
    Handles Payment operations in NaijaSure Insurance System.
    Includes processing, reminders, and penalties.
    """

    def __init__(self, policyholder, product):
        self.policyholder = policyholder
        self.product = product
        self.amount = product.price
        self.timestamp = None
        self.is_paid = False

    def process_payment(self):
        """Process payment for a policyholder's product."""
        if not self.policyholder.is_active:
            print(f"🚫 Payment failed. {self.policyholder.name}'s account is suspended.")
            return False
        if not self.product.is_active:
            print(f"🚫 Payment failed. Product {self.product.name} is suspended.")
            return False

        self.is_paid = True
        self.timestamp = datetime.now()
        print(f"💳 Payment of ₦{self.amount} successful for {self.policyholder.name} "
              f"on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}.")
        return True

    def send_reminder(self):
        """Send payment reminder if unpaid."""
        if not self.is_paid:
            print(f"📩 Reminder: {self.policyholder.name}, your payment for {self.product.name} is pending.")
        else:
            print(f"✅ No reminder needed. {self.policyholder.name} has already paid.")

    def apply_penalty(self, penalty_amount):
        """Apply penalty if payment is overdue."""
        if not self.is_paid:
            self.amount += penalty_amount
            print(f"⚠️ Penalty of ₦{penalty_amount} applied. New total: ₦{self.amount}.")
        else:
            print(f"✅ No penalty. {self.policyholder.name} already paid.")
