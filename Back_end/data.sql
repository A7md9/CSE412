

-- Inserting data into Librarian Table
INSERT INTO Librarian (ID, Email, Username, Password) VALUES
(1, 'librarian1@email.com', 'lib1', 'password123'),
(2, 'librarian2@email.com', 'lib2', 'password456');

-- Inserting data into Book Table
INSERT INTO Book (ID, Status, Title, Author, ISBN, PublicationDate) VALUES
(1, 'Available', 'Book Title 1', 'Author 1', '123-456-789', '2020-01-01'),
(2, 'Borrowed', 'Book Title 2', 'Author 2', '987-654-321', '2019-05-10');

-- Inserting data into Patron Table
INSERT INTO Patron (ID, Username, Password, ContactInformation) VALUES
(1, 'patron1', 'patpassword123', '123 Street, City'),
(2, 'patron2', 'patpassword456', '456 Avenue, City');

-- Inserting data into Report Table
INSERT INTO Report (ID, Type, GeneratedDate, LibrarianID) VALUES
(1, 'Monthly', '2023-01-01', 1),
(2, 'Yearly', '2023-12-31', 2);

-- Inserting data into Reservation Table
INSERT INTO Reservation (ID, Date, PatronID, LibrarianID) VALUES
(1, '2023-02-15', 1, 1),
(2, '2023-03-20', 2, 2);

-- Inserting data into Transaction Table
INSERT INTO Transaction (ID, BorrowDate, DueDate, ReturnDate, BookID, PatronID) VALUES
(1, '2023-02-01', '2023-02-21', '2023-02-19', 1, 1),
(2, '2023-03-05', '2023-03-25', NULL, 2, 2);

-- Inserting data into Notification Table
INSERT INTO Notification (ID, Type, SentDate, PatronID) VALUES
(1, 'Reminder', '2023-02-19', 1),
(2, 'Overdue', '2023-03-26', 2);

-- Inserting data into Relationships (Many to Many Tables)
INSERT INTO BookReservation (BookID, ReservationID) VALUES
(1, 1),
(2, 2);

INSERT INTO PatronBook (PatronID, BookID) VALUES
(1, 1),
(2, 2);
