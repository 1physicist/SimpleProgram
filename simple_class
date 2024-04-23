class Person():
    defaultname = "none" # class attributes => default value
    defaultcity = "unknown"
    # Constructor -- self is used if a value is passed to the object. parameters are object attributes. example: age and name
    def __init__(self,birthday,name = defaultname,city = defaultcity): 
        # object attributes
        self.birthday = birthday
        self.name = name
        self.city = city

    # methods
    def PersonCalculateAge(self):
        age = 2023 - self.birthday
        return age

# object
P1 = Person(1997, "1thedk","istanbul")
P2 = Person(2000, city ="ankara") # city is ankara and name is default value "none"
P3 = Person(2001, "onethedk")
# accessing object attributes
print(f"Person1 birthday is", P1.birthday,
      f"Person1 age is", P1.PersonCalculateAge(),
      f"Person1 name is", P1.name,
      f"Person1 live in", P1.city,
      )
print(f"Person2 birthday is", P2.birthday,
      f"Person2 age is", P2.PersonCalculateAge(),
      f"Person2 name is", P2.name,
      f"Person2 live in", P2.city,
      )
print(f"Person3 birthday is", P3.birthday,
      f"Person3 age is", P3.PersonCalculateAge(),
      f"Person3 name is", P3.name,
      f"Person3 live in", P3.city,
      )
