def get_valid_input(input_string, valid_optoins):
    '''
    This is validation function which we are using in all our methods, and we can just init it here
    to reduce duplication of code
    :param input_string: What we need to enter
    :param valid_optoins: Options which is available
    :return: our iput
    '''
    input_string += "({})".format(", ".join(valid_optoins))
    response = input(input_string)
    return response


class Property:
    '''
    This the most main class for initializing and further work with property
    There are 2 option of property to choose Apartment or House
    '''
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        :return: Displays info about property
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Initializing a property characteristic
        :return:
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter a number of bedrooms: "),
                    baths=input("Enter number of baths: "))

#Converting this method to static
    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    This Class inherit property, because apartment is a sort of property
    """
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')
    #adding additional parameters to the property

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Print information about Apartment, but first print info about property
        :return:
        """
        super().display() #causes parent display method and then display method of this class
        print("APARTMENT DETAILS")
        print('laundry: %s' % self.laundry)
        print('has balcony : %s' % self.balcony)

    def prompt_init():
        '''
        Inputing and adding additional inofrmation to parent_init(dict
        '''
        parent_init = Property.prompt_init() # here we calling parent class init method
        laundry = get_valid_input("What laundry facilitirs does"
                                  "the property have? ",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?",
                                  Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    This is 1 more sort of property, that`s why house inherit property
    """
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Giving information about house characteristic
        :return:
        """
        super().display()
        print('HOUSE DETAILS')
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Adding characteristic to house, and updating dict with new keys and values
        :return:  Updated dict
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How mwny stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Giving information about price of a purchase and taxes
    """
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Printing all information about property, it price and taxes
        :return:
        """
        super().display()
        print(" PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Instead of buying property user can rent it
    """
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Giving full information about
        :return:
        """
        super().display()
        print("RENTAL DETAILS")
        print('rent: {}'.format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Additional information about property rental to object of class Property
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Through agent class you can add property to property list ofr the further use
    """
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        """
        printing all properties for the user
        :return:
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """
        This module add 1 more object of property to list.
        :return:
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
