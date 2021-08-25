
""""   Add two dictionaries files    """

dict1 = {
    "Hello": 56,
    "at" : 23,
    "test" : 43,
    "this" : 43
    }
dict2 = { 'where' : 4,
     'who' : 5 ,
     'why': 6 ,
     'this' : 20
     }
dict1.update(dict2)
print(dict1)