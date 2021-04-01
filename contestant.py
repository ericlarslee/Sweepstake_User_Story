class Contestant:
    def __init__(self, fname, lname, email, registration_number):
        self.first_name = fname
        self.last_name = lname
        self.email_address = email
        self.registration_number = int(registration_number)

    def notify(self): pass

