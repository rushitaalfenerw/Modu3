Insurance Policy Management System
This work implements a basic insurance policy management system using Python. The system manages policyholders(Policy), products(Prod), and payments(pay).

Classes and Their Functions:

Policy:
register(): Registers a new policyholder.
suspend(): Suspends a policyholder's account.
reactivate(): Reactivates a suspended policyholder's account.
account_details(): Displays the policyholder's account information.
Prod:
create(): Creates a new policy product.
update(): Updates an existing policy product.
remove(): Removes a policy product.
suspend(): Suspends a policy product.
Pay:
process(): Processes a payment for a policy.
send_reminder(): Sends a payment reminder to a policyholder.
apply_penalty(): Applies a penalty for a late payment.

Usage:

# Create policyholders and products
policyholderA = Policy("Alfene", "Gasabo-Nyarutarama", "0789670564", [])
policyholderB = Policy("Glacia", "Burundi-Bujumbura", "0793457432", [])

productA = Prod("Car Insurance", "puts you in the driver's seat with cover that keeps you moving and protects you and your passengers regardless of your destination.", 100)
productB = Prod("Education Insurance", "ensures that even if you suffer an unexpected disability or death, your children's university education fees will still be covered ", 200)

# Register policyholders and pay for products
policyholderA.register()
policyholderA.policy_products.append(productA)
policyholderB.register()
policyholderB.policy_products.append(productB)

# Process payments
paymentA = Pay(100, datetime.date.today(), policyholderA)
paymentA.process()

paymentB = Pay(200, datetime.date.today(), policyholderB)
paymentB.process()

# Display account information
policyholderA.account_details()
policyholderB.account_details()
