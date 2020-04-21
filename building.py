from datetime import datetime

# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.

# Properties
# designer - It will hold your name.
# date_constructed - This will hold the exact time the building was created.
# owner - This will store the same of the person who owns the building.
# address
# stories


class Building:


    def __init__(self, address, stories):
        self.designer = "Chase"
        self.date_constructed = "TBD"
        self.owner = "TBD"
        self.address = address
        self.stories = stories

# Methods

# Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

    def construct(self):
        self.date_constructed = datetime.now()

# Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

    def purchase(self, purchaser_name):
        self.owner = purchaser_name

    
    def output(self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.")

# Constructor
# Define your __init__ method to accept two arguments

# address
# stories
# Once defined this way, you can send those values as parameters when you create each instance

# Creating Your Buildings
# 1. Create 5 building instances

eight_hundred_eighth = Building("800 8th Street", 12)
one_hundred_first = Building("100 1st Street", 11)
two_hundred_second = Building("200 2nd Street", 22)
three_hundred_third = Building("300 3rd Street", 33)
four_hundred_fourth = Building("400 4th Street", 44)

# 2. Have each one get purchased by a real estate magnate

eight_hundred_eighth.purchase("Team Rockensock")
one_hundred_first.purchase("Best Real Estate Advisors")
two_hundred_second.purchase("Crye-Leike Realtors")
three_hundred_third.purchase("We Buy Houses Putnam")
four_hundred_fourth.purchase("Post and Company Real Estate")

# 3. After purchased, construct each one

eight_hundred_eighth.construct()
one_hundred_first.construct()
two_hundred_second.construct()
three_hundred_third.construct()
four_hundred_fourth.construct()

# 4. Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example...800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.

eight_hundred_eighth.output()
one_hundred_first.output()
two_hundred_second.output()
three_hundred_third.output()
four_hundred_fourth.output()
