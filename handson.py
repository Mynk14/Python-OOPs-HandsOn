class Library:
    fine_amount = 10
    total_students = 0

    def __init__(self, first, last, fine, standard):
        self.first = first
        self.last = last
        self.standard = standard
        self.fine = fine
        Library.total_students +=1

    def full_name(self):
        print '{} {}'.format(self.first, self.last),

    def fine(self, days):
        self.fine = self.fine_amount * days
        print self.fine

    @classmethod
    def raise_fine(cls, amount):
        cls.fine_amount = cls.fine_amount + amount

    @staticmethod
    def is_lib_open(day):
        if day == "Saturday" or day == "Sunday":
            return False
        return True


class Teachers(Library):
    fine_amount = 5

    def __init__(self, first, last, fine, books=None):
        self.first = first
        self.last = last
        self.fine = fine
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_books(self, book):
        if book in self.books:
            print 'Already Present'
        else:
            self.books.append(book)

    def remove_books(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print book + ' Not Present'


class FinalYears(Library):
    fine_amount = 15
    standard = 12

    def __init__(self, first, last, fine, no_of_books):
        self.first = first
        self.last = last
        self.no_of_books = no_of_books
        self.fine = fine


s1 = Library("Shiv", "Raj", 0, 5)
s2 = Library("Anurag", "Bisht", 0, 8)

print s2.full_name()
print Library.full_name(s1),


print Library.total_students

print s1.__dict__
Library.fine(s1, 5)
print s1.__dict__


s1.fine_amount = 5
print s1.fine_amount
print s2.fine_amount
print Library.fine_amount

Library.raise_fine(2)
print s1.fine_amount
print s2.fine_amount
print Library.fine_amount

print Library.is_lib_open("Monday")
print Library.is_lib_open("Saturday")

f1 = FinalYears("Joy", "Mathews", 0, 2)
print f1.fine_amount
print f1.__dict__

t1 = Teachers("Manoj", "Kumar", 0, ["Python basics", "C in depth"])
print t1.__dict__

t1.add_books("learning OOPs in Python")
print t1.books

t1.remove_books("JAVA for everyone")
print t1.books

t1.remove_books("C in depth")
print t1.books

print isinstance(s1, Library)
print isinstance(t1, Teachers)
print isinstance(t1, Library)
print isinstance(t1, FinalYears)

print issubclass(Teachers, Library)
print issubclass(FinalYears, Library)