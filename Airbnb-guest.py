class Airbnb:
    def __init__(self, guest_name, rental, start_date, end_date):
        self.guest_name = guest_name
        self.rental = rental
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Booking for {self.rental.title} by {self.guest_name}, From: {self.start_date} To: {self.end_date}"

if __name__ == "__main__":
    rental1 = Rental("Cozy apartment in the city center", "City center", 100, 4)
    airbnb_booking = Airbnb("John Doe", rental1, "2024-04-20", "2024-04-25")
    print(airbnb_booking)
