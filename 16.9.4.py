class Client:
    def __init__(self, firstname, lastname, city, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.firstname}'+f' '+f'{ self.lastname}'+f'. '+f'{self.city}'+f'.'

    def init_from_dict(self, client_dict):
        self.firstname = client_dict.get("firstname")
        self.lastname = client_dict.get("lastname")
        self.city = client_dict.get("city")
        self.balance = client_dict.get("balance")

clients=[
    {
        "firstname": "Иван",
        "lastname": "Петров",
        "city": "Москва",
        "balance": 50
    },
    {
        "firstname": "Петр",
        "lastname": "Иванов",
        "city": "Петербург",
        "balance": 150
    },
    {
        "firstname": "Олег",
        "lastname": "Николаев",
        "city": "Донецк",
        "balance": 250
    }
]


for cl in clients:
    cl_obj = Client('firstname', 'lastname', 'city', 'balance')
    cl_obj.init_from_dict(cl)
    print(cl_obj.__str__())



