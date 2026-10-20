
from datetime import datetime

class Policyholder:
    """
    Represents a Policyholder in NaijaSure Insurance System.
    Handles registration, suspension, reactivation, and product assignments.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.is_active = True
        self.products = []
        self.created_at = datetime.now()

    def suspend(self):
        """Suspend the policyholder account."""
        if not self.is_active:
            print(f"⚠️ {self.name}'s account is already suspended.")
        else:
            self.is_active = False
            print(f"🚫 Policyholder {self.name} has been suspended.")

    def reactivate(self):
        """Reactivate the policyholder account."""
        if self.is_active:
            print(f"ℹ️ {self.name}'s account is already active.")
        else:
            self.is_active = True
            print(f"✅ Policyholder {self.name} has been reactivated.")

    def assign_product(self, product):
        """Assign a product to the policyholder."""
        if product not in self.products:
            self.products.append(product)
            print(f"📄 {self.name} has been assigned product: {product.name}")
        else:
            print(f"⚠️ {self.name} already has {product.name}.")

    def __str__(self):
        status = "Active ✅" if self.is_active else "Suspended 🚫"
        product_list = "\n   - ".join([f"{p.name} | ₦{p.price}" for p in self.products]) or "None"
        return (f"\n👤 Policyholder: {self.name} ({self.email})\n"
                f"   Status: {status}\n"
                f"   Registered: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"   Products:\n   - {product_list}\n")