
from policyholder import Policyholder
from product import Product
from payment import Payment

def run_demo():
    print("\n🌍 Welcome to NaijaSure Insurance Manager 🌍")
    print("------------------------------------------------")

    # Create Products
    health = Product("Health Cover", 50000)
    life = Product("Life Assurance", 75000)

    # Create Policyholders
    alice = Policyholder("Funmi Johnson", "funmi.johnson@yahoo.com")
    bob = Policyholder("Chinyem Okocha", "chichi.ko@gmail.com")

    # Assign products
    alice.assign_product(health)
    bob.assign_product(life)

    # Process payments
    pay1 = Payment(alice, health)
    pay1.process_payment()

    pay2 = Payment(bob, life)
    pay2.process_payment()

    # Show details
    print(alice)
    print(bob)

if __name__ == "__main__":
    run_demo()