from Prod import Prod
class Policy:
    def __init__(self, name, address, contact, policy_products):
        self.name = name
        self.address = address
        self.contact = contact
        self.policy_products = policy_products

    def register(self):
        # Implement registration logic here
        print("Policyholder registered successfully.")

    def suspend(self):
        # Implement suspension logic here
        print("Policyholder suspended successfully.")

    def reactivate(self):
        # Implement reactivation logic here
        print("Policyholder reactivated successfully.")

    def account_details(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Contact:", self.contact)
        print("Policy Products:")
        for Prod in self.policy_products:
            print(f"  - Name: {Prod.name}")
            print(f"    - Description: {Prod.description}")
            print(f"    - Premium: {Prod.premium}")

