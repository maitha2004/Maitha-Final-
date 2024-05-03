#UML

class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, dob, passport_details,
                 manager_id=None):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details
        self.manager_id = manager_id
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def remove_subordinate(self, subordinate):
        if subordinate in self.subordinates:
            self.subordinates.remove(subordinate)
        else:
            print("Subordinate not found")

    def get_subordinates(self):
        return self.subordinates

    def save(self):
        # Code to save employee details to database/file
        pass

    @staticmethod
    def load_all():
        # Code to load all employees from database/file
        pass

    def update(self):
        # Code to update employee details
        pass

    def delete(self):
        # Code to delete employee from database/file
        pass

    def get_info(self):
        return f"Employee: {self.name}, Employee ID: {self.employee_id}, Department: {self.department}, Job Title: {self.job_title}, Salary: {self.basic_salary}, Age: {self.age}, DOB: {self.dob}, Passport Details: {self.passport_details}, Manager ID: {self.manager_id}"


class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    def save(self):
        # Code to save client details to database/file
        pass

    @staticmethod
    def load_all():
        # Code to load all clients from database/file
        pass

    def delete(self):
        # Code to delete client from database/file
        pass

    def update(self):
        # Code to update client details
        pass

    def get_info(self):
        return f"Client: {self.name}, Client ID: {self.client_id}, Address: {self.address}, Contact: {self.contact_details}, Budget: {self.budget}"


class Event:
    def __init__(self, name, event_id, event_type, contact_details, venue=None, theme=None, date=None):
        self.name = name
        self.event_id = event_id
        self.event_type = event_type
        self.contact_details = contact_details
        self.venue = venue
        self.theme = theme
        self.date = date
        self.guests = []

    def assign_venue(self, venue):
        self.venue = venue

    def register_guest(self, guest):
        self.guests.append(guest)

    def get_info(self):
        venue_info = "Not assigned" if not self.venue else self.venue.get_info()
        return f"Event: {self.name}, Type: {self.event_type}, Contact: {self.contact_details}, Venue: {venue_info}"


class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def save(self):
        # Code to save supplier details to database/file
        pass

    @staticmethod
    def load_all():
        # Code to load all suppliers from database/file
        pass

    def delete(self):
        # Code to delete supplier from database/file
        pass

    def update(self):
        # Code to update supplier details
        pass

    def get_info(self):
        return f"Supplier: {self.name}, Address: {self.address}, Contact: {self.contact_details}"


class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def save(self):
        # Code to save guest details to database/file
        pass

    @staticmethod
    def load_all():
        # Code to load all guests from database/file
        pass

    def delete(self):
        # Code to delete guest from database/file
        pass

    def update(self):
        # Code to update guest details
        pass

    def get_info(self):
        return f"Guest: {self.name}, Address: {self.address}, Contact: {self.contact_details}"


class Venue:
    def __init__(self, venue_id, name, address, contact_details, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.min_guests = min_guests
        self.max_guests = max_guests

    def save(self):
        # Code to save venue details to database/file
        pass

    @staticmethod
    def load_all():
        # Code to load all venues from database/file
        pass

    def delete(self):
        # Code to delete venue from database/file
        pass

    def update(self):
        # Code to update venue details
        pass

    def get_info(self):
        return f"Venue: {self.name}, Address: {self.address}, Contact: {self.contact_details}, Min Guests: {self.min_guests}, Max Guests: {self.max_guests}"


# Test case examples
employee1 = Employee("Ahmed Al Fahim", 1, "HR", "Manager", 50000.0, 30, "01-01-1990", "12345678")
supplier1 = Supplier(1, "Al Khaleej LLC", "123 Sheikh Zayed Rd", "info@alkhaleej.com")
venue1 = Venue(1, "Dubai Conference Center", "Dubai World Trade Center", "events@dwtc.com", 100, 500)
event1 = Event("Tech Summit", 1, "Technology", "events@mycompany.com", venue1, "Innovation", "2024-05-05")

event1.assign_venue(venue1)
guest1 = Guest(1, "Fatima Mohammed", "456 Al Maktoum St", "fatima.mohammed@email.com")
event1.register_guest(guest1)

print(employee1.get_info())
print(supplier1.get_info())
print(venue1.get_info())
print(event1.get_info())
print(guest1.get_info())
