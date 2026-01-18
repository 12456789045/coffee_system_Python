class Coffee_Arena:
    def __init__(self):
        self.coffee = None
        self.size = None
        self.cost = 0

    def menu(self):
        print("\n☕ Welcome To Cafe Arena 🍵\n")

        self.menu_items = {
            "1": "Expresso",
            "2": "Latte",
            "3": "Ice_Latte",
            "4": "Cold_Coffee",
            "5": "Black_Coffee",
            "6": "Americano",
        }

        for k, v in self.menu_items.items():
            print(f"{k}. {v}")

        while True:
            choice = input("\nEnter the coffee number: ")
            if choice in self.menu_items:
                self.coffee = self.menu_items[choice]
                break
            else:
                print("❌ Invalid choice! Try again.")

    def quantity(self):
        print("\nSelect Cup Size")

        self.sizes = {"1": "small", "2": "medium", "3": "large"}

        for k, v in self.sizes.items():
            print(f"{k}. {v}")

        while True:
            choice = input("\nEnter cup size number: ")
            if choice in self.sizes:
                self.size = self.sizes[choice]
                break
            else:
                print("❌ Invalid size! Try again.")

    def price(self):
        cost_chart = {
            "Expresso": {"small": 120, "medium": 150, "large": 190},
            "Latte": {"small": 120, "medium": 150, "large": 190},
            "Ice_Latte": {"small": 120, "medium": 150, "large": 190},
            "Cold_Coffee": {"small": 120, "medium": 150, "large": 190},
            "Black_Coffee": {"small": 120, "medium": 150, "large": 190},
            "Americano": {"small": 120, "medium": 150, "large": 190},
        }

        self.cost = cost_chart[self.coffee][self.size]

    def user_data(self):
        self.name = input("\nEnter your name: ")
        self.phone = input("Enter your phone number: ")
        self.address = input("Enter your address: ")

    def bill(self):
        print("\n🧾 Order Summary")
        print("----------------------")
        print(f"Customer : {self.name}")
        print(f"Coffee   : {self.coffee}")
        print(f"Size     : {self.size}")
        print(f"Price    : ₹{self.cost}")
        print("----------------------")
        print("☕ Thank You! Visit Again 😊")


order = Coffee_Arena()
order.menu()
order.quantity()
order.price()
order.user_data()
order.bill()
