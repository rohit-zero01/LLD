class Movie:
    def __init__(self, movie_name, total_seats, ticket_price):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self):
        num_tickets = int(input("Enter the no. of tickets you want to book:"))
        if self.total_seats - self.booked_seats >= num_tickets:
            self.booked_seats += num_tickets
            print(f"Your ticket for the movie {self.movie_name} is booked successfully \nTotal amount to pay = {self.ticket_price * num_tickets}")
        else:
            print(f"Sorry, not enough seats available")

    def show_status(self):
        print(f"Movie Name: {self.movie_name} \ntotal seats: {self.total_seats} \nseats booked: {self.booked_seats} \nseats available: {self.total_seats - self.booked_seats}")

M1 = Movie("Avengers", 100, 150, 0)
M1.show_status()
M1.book_ticket()
M1.show_status()
