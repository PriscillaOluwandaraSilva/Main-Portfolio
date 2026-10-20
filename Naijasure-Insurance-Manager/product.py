
class Product:
    """
    Represents an Insurance Product in NaijaSure Insurance System.
    Handles creation, updating, suspension, and activation.
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_active = True

    def suspend(self):
        """Suspend this product."""
        if not self.is_active:
            print(f"⚠️ Product {self.name} is already suspended.")
        else:
            self.is_active = False
            print(f"🚫 Product {self.name} has been suspended.")

    def activate(self):
        """Reactivate this product."""
        if self.is_active:
            print(f"ℹ️ Product {self.name} is already active.")
        else:
            self.is_active = True
            print(f"✅ Product {self.name} has been reactivated.")

    def update(self, name=None, price=None):
        """Update product name or price."""
        if name:
            print(f"✏️ Product renamed from {self.name} → {name}")
            self.name = name
        if price:
            print(f"💰 Price updated for {self.name}: ₦{self.price} → ₦{price}")
            self.price = price

    def __str__(self):
        status = "Active ✅" if self.is_active else "Suspended 🚫"
        return f"{self.name} | Price: ₦{self.price} | Status: {status}"
