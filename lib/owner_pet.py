# @classmethod, @property = @obj.getter , @obj.setter. @obj.deleter referred to as pie syntax
# @classmethod allows access to all global class variables using cls 
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] 
    all = []
    # __init__ is the constructor in the class method because creats a object 
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type 
        self.owner = owner
        Pet.all.append(self)

#validate pet_type in __init__? using raise 
    @property
    # @property = get_pet_type
    def pet_type(self):
        # make sure to privatize attribute for each getter
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception
            # makes sure this is a valid pet type and allows it to be used
        self._pet_type = pet_type

    # @property
    # def owner(self):
    #     return self._owner
    
    # @owner.setter
    # def owner(self, owner):
    #     if not (isinstance(owner, Owner) or not owner):
    #         raise Exception
    #     self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]


    def add_pet(self, pet):
        if not isinstance(pet, Pet):
           raise Exception
        pet.owner = self
        # self is what the function is being called on 

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    # lambda = an anonomus funciton used as key 
    # self.pets gives me owners pets and thats why invoked
    # key= lamda provides an anonomyous funciton, used ver well as keys for sorted lists
