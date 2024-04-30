##Clases##


class MyEmptyPerson:
    pass

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"
        self.__name = name ##Private

        

    def get_name(self): ## Un getter
        return self.__name
    
    
    
    def walk(self):
        print(f"{self.full_name} esta caminando")

my_person= Person("Oscar", "Pereyra")
print(my_person.full_name)
my_person.walk()