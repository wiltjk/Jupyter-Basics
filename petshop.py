#pylint:disable=E0001
# Base class for all Pets
class Pet:
    __petCount = 0                # global counter is protected
    
    # Constructor 
    def __init__ (self, name = "I'm a pet without a name"):
        self.name = name
        Pet.__petCount += 1       # add a pet 
        
        className = self.__class__.__name__
        print (f"*** {className} created -- {Pet.__petCount} pet(s).")
                
    # Destructor 
    def __del__ (self):
        Pet.__petCount -= 1       # remove a pet
        
        className = self.__class__.__name__
        print (f"*** {className} deleted -- {Pet.__petCount} pet(s) left.")
        
    # Return pet count 
    def getPetCount (self):
        # print (f"*** Protected petCount = {Pet.__petCount}")
        return Pet.__petCount   # return protected count
    
    # Return pet voice * override this * 
    def speak (self): 
        return "I have no voice"
        
# Child class Dog
class Dog (Pet): 
    # Return dog voice * overriden *
    def speak (self): 
        return "bark"

# Child class Cat
class Cat (Pet): 
    # Return cat voice * overriden *
    def speak (self): 
        return "meow"
    
# Child class Parrot
class Parrot (Pet): 
    # Return parrot voice * overriden *
    def speak (self): 
        return "I want a cracker"

# Child class Cow   
class Cow (Pet): 
    # Return cow voice * overriden *
    def speak (self): 
        return "moo"


# Test Pets
def testPets ():
    myPet  = Dog ("Rover")
    print (f"\nMy pet's name is {myPet.name} and it says {myPet.speak ()}. I have {myPet.getPetCount ()} pets.\n\n") 
    
    myPet2 =  Cat ("Kitty")
    print (f"\nMy pet's name is {myPet2.name} and it says {myPet2.speak ()}. I have {myPet2.getPetCount ()} pets.\n\n") 
    
    myPet3 =  Parrot ("Polly")
    print (f"\nMy pet's name is {myPet3.name} and it says {myPet3.speak ()}. I have {myPet3.getPetCount ()} pets.\n\n") 
    
    myPet  = Cow ("Bessie")  # Replace dog with cow
    print (f"\nMy pet's name is {myPet.name} and it says {myPet.speak ()}. I have {myPet.getPetCount ()} pets.\n\n") 
    
    
    print (myPet)
    print (myPet2)
    print (myPet3, "\n")
    
    return

# Main
if (__name__ == "__main__"):
    print ("\n\n—BOJ—\n\n")
    testPets ()
    print ("\n\n—EOJ—\n\n")
