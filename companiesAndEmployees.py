# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.

class Employee:

    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date


# Create a Company type that employees can work for. A company should have a business name, address, and industry type.

class Company:

    def __init__(self, name, address, industry_type):
        self.name = name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()


# Create two companies, and 5 people who want to work for them.

GloboGym = Company("Globo Gym", "Gainz St.", "Fitness")
RiotGames = Company("Riot Games", "West Los Angeles", "Entertainment")

Bob = Employee("Bob Lee Swagger", "Marine", "4/20/2020")
Jimmy = Employee("Jimmy John", "Chef", "4/20/2020")
Johnny = Employee("Johnny John", "Cashier", "4/21/2020")
Billy = Employee("Billy Bob", "Professional Athlete", "4/21/2020")
Jane = Employee("Jane Doe", "")

