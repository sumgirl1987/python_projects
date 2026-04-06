class Address:
    def __init__(self, zipcode, city, street, house, apartment):
        self.zipcode = zipcode
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return (f"{self.zipcode}, {self.city}, {self.street}, {self.house}, "
                f"{self.apartment}")
