from django.contrib.auth.models import User
from django.db import models


# Librarian Model
class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Report Model
class Report(models.Model):
    TYPE_CHOICES = (
        ('daily_activity', 'Daily Activity Report'),
        ('monthly_activity', 'Monthly Activity Report'),
        ('annual_activity', 'Annual Activity Report'),
        ('overdue_books', 'Overdue Books Report'),
        ('popular_books', 'Most Popular Books Report'),
        ('inactive_patrons', 'Inactive Patrons Report'),
        ('book_inventory', 'Book Inventory Report'),
        ('damaged_books', 'Damaged Books Report'),
        ('frequent_borrowers', 'Frequent Borrowers Report'),
        ('financial_statement', 'Financial Statement'),
    )
    """
    Here's a brief explanation of each type:
    daily_activity: A report of all library activity on a particular day.
    monthly_activity: Summarizes all library activity for a given month.
    annual_activity: Provides a summary of all library activity over the course of a year.
    overdue_books: Lists all books that are currently overdue and their borrowers.
    popular_books: Highlights the most borrowed or reserved books in a given time period.
    inactive_patrons: Identifies patrons who haven't borrowed or reserved any books for a specified period.
    book_inventory: Gives a comprehensive list of all books in the library, their status (available, borrowed, reserved), and other details.
    damaged_books: Details books that were returned damaged or are not in good condition.
    frequent_borrowers: Identifies patrons who borrow books frequently.
    financial_statement: A report detailing the library's financial activity, which might include fines collected, expenses, etc.
    """
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    generated_date = models.DateField()
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} - {self.generated_date}"

# Book Model
class Book(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    )
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, unique=True)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

# Patron Model
class Patron(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_information = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

# Reservation Model
class Reservation(models.Model):
    date = models.DateField()
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation on {self.date} by {self.patron.username}"

# Transaction Model
class Transaction(models.Model):
    borrow_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction for {self.book.title} by {self.patron.username}"

# Notification Model
class Notification(models.Model):
    TYPE_CHOICES = (
        ('overdue', 'Overdue Book Reminder'),
        ('reservation_ready', 'Reservation Ready for Pickup'),
        ('reservation_expiring', 'Reservation Expiring Soon'),
        ('book_returned', 'Book Returned Confirmation'),
        ('book_due_soon', 'Book Due Soon Reminder'),
        ('account_activity', 'Recent Account Activity'),
        ('upcoming_event', 'Upcoming Library Event'),
        ('general_announcement', 'General Library Announcement'),
    )

    """
    Here's a brief explanation of each type:
    overdue: Notifies the patron that they have a book that is overdue and needs to be returned.
    reservation_ready: Alerts the patron when a book they reserved is available for pickup.
    reservation_expiring: Notifies the patron that their reservation will expire soon if they don't pick up the reserved book.
    book_returned: Confirmation for the patron when they return a book.
    book_due_soon: Reminder for the patron that their borrowed book is due soon.
    account_activity: Notifies the patron of recent account activity, like if someone changed the account details.
    upcoming_event: Alerts patrons of upcoming library events or programs.
    general_announcement: General library announcements, such as holiday closures or new service offerings.
    """
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    sent_date = models.DateField()
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notification on {self.sent_date} for {self.patron.username}"

# BookReservation Model (Many to Many relationship)
class BookReservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'reservation')

# PatronBook Model (Many to Many relationship)
class PatronBook(models.Model):
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('patron', 'book')
