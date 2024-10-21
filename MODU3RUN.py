from Policy import Policy
from Prod import Prod
from Pay import Pay
import datetime

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

# Display account details
policyholderA.account_details()
policyholderB.account_details()