class mad_libs:
        
    def __init__(self,adjective, animal, place,_object, verb, creature, another_place,food):
        self.adjective=adjective
        self.animal=animal
        self.place=place
        self._object=_object
        self.verb=verb
        self.creature=creature
        self.another_place=another_place
        self.food=food

    def story(self):
 
        print(f'''One day, a {self.adjective} {animal} was walking through the {self.place}.
             It saw a {self.adjective} {self._object} and decided to {self.verb} it. Suddenly, a {self.creature} appeared and started {self.verb}! The {self.animal} got scared and ran to {self.another_place}, where it met a {self.adjective} friend. Together, they had a great time and enjoyed a delicious {self.food}''')



def print_statement():
    print('''One day, a [adjective] [animal] was walking through the [place].It saw a [adjective] [object] and decided to [verb] it. Suddenly, a [creature] appeared    and started [verb-ing]! The [animal] got scared and ran to [another place], where it   met a [adjective] friend. Together, they had a great time and enjoyed a delicious[food].''')

print_statement()
print(" ")
adjective=input("enter the adjective : ")
animal=input("enter the animal : ")
place=input("enter the place : ")
_object=input("enter the object : ")
verb=input("enter the verb : ")
creature=input("enter the creature : ")
another_place=input("enter the another-place : ")
food=input("enter the food : ")

stry=mad_libs(adjective,animal,place,_object,verb,creature,another_place,food)
stry.story()