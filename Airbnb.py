class Rental:
    def __init__(self, title, location, price_per_night, capacity, available=True):
        self.title = title
        self.location = location
        self.price_per_night = price_per_night
        self.capacity = capacity
        self.available = available

    def __str__(self):
        return f"{self.title} located in {self.location}, Price per night: ${self.price_per_night}, Capacity: {self.capacity} guests"

    def book(self):
        if self.available:
            print(f"Booking {self.title}...")
            self.available = False
        else:
            print(f"Sorry, {self.title} is already booked.")

    def cancel_booking(self):
        if not self.available:
            print(f"Cancelling booking for {self.title}...")
            self.available = True
        else:
            print(f"No booking found for {self.title}.")

if __name__ == "__main__":
    rental1 = Rental("Cozy apartment in the city center", "City center", 100, 4)
    print(rental1)

    rental1.book()
    rental1.book()
    rental1.cancel_booking()
    rental1.book()
