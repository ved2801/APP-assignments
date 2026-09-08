#ONLINE PAYMENT BY STRATEGY METHOD:

class Payment:
    
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PayPal:
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


print("=== Online Shopping Payment ===")

amount = int(input("Enter amount: ₹"))

print("\nSelect Payment Method:")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")

choice = int(input("Enter your choice: "))
match choice:

    case 1:
        strategy = CreditCard()
        payment = Payment(strategy)
        payment.make_payment(amount)

    case 2:
        strategy = UPI()
        payment = Payment(strategy)
        payment.make_payment(amount)

    case 3:
        strategy = PayPal()
        payment = Payment(strategy)
        payment.make_payment(amount)

    case _:
        print("Invalid payment method")
        exit()
