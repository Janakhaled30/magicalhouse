n=input("enter ur name :")
e=input("enter ur email :")
p=input("enter ur phone_number:")
class magicalcontact:
    def __init__(self,name,email,phone_number):
        self.__name= name
        self.__email= email
        self._phone_number= phone_number

    def get_name(self):   
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def set_email(self,email):
        self.__email= email

    def get_phone_number(self):
        return self._phone_number
    
    def set_phone_number(self,phone_number):
        self.phone__number= phone_number

    def describe(self):
        print(f"Name:{self.__name},Email:{self.__email},Phone number:{self.phone__number}")



wand_core=input("Enter ur core  :")
wand_wood=input("Enter ur wood :")
wand_length=input("Enter ur length:")
house= input("Enter the house(Gryffindor,Hufflepuff,Ravenclaw,Slytherin):")

class WizardOrWitch(magicalcontact):
    def __init__(self,name,email,phone_number,wand_core,wand_length,wand_wood):
        super().__init__(name,email,phone_number)
        houses=["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
        if houses not in houses:
            print("value error")
        self.__houses= houses
        self.wand={
        "core":wand_core,
        "wood":wand_wood,
        "length":wand_length
        }
    def get_wand(self):
        return f"{self._wand['length']},{self._wand['wood']},{self._wand['core']}"    
    def get_house(self):
        return self.__houses
    def describe(self):
        print(f"house :{self.__houses} ,Wand:{self._wand['length']} ,{self._wand['wood']} , {self._wand['core']}")

species=str(input("enter The species of the magical creature:"))
is_tame=bool(input("is the creature tame?"))
class MagicalCreature(magicalcontact):
    def __init__(self,name,email,phone_number,species,is_tame):
        super().__init__(name,email,phone_number)
        self.__species = species
        self.__is_tame = is_tame
    def get_species(self):
         return self.__species
    def is_tame(self):
        return self.__is_tame
    def describe(self):
        print(f"species:{self.__species},Tame:{self.__is_tame}")
    
class MagicalContactBook():
    def __init__(self):
        self.__contacts = []

    def add_contact(self, contact):
        self.__contacts.append(contact)

    def list_contacts(self):
        for contact in self.__contacts:
            contact.describe()

    def find_contact(self, name):
        for contact in self.__contacts:
            if contact.get_name == name:
                contact.describe()
                return contact
        return None
