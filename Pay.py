class Pay:
    def __init__(self, amount, date, policyholder):
        self.amount = amount
        self.date = date
        self.policyholder = policyholder

    def process(self):
        # Implement payment processing logic here
        print("Payment processed successfully.")

    def send_reminder(self):
        # Implement reminder logic here
        print("Payment reminder sent successfully.")

    def apply_penalty(self):
        # Implement penalty logic here
        print("Payment penalty applied successfully.")