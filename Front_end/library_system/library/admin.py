from django.contrib import admin
from .models import Librarian, Patron, Report, Book, Reservation, Transaction, Notification


# Register the models
admin.site.register(Librarian)
admin.site.register(Patron)
admin.site.register(Report)
admin.site.register(Book)
admin.site.register(Reservation)
admin.site.register(Transaction)
admin.site.register(Notification)
