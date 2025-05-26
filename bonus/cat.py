
from typing_extensions import override
from animal import Animal
from pet import Pet

class Cat(Animal, Pet):


	def __init__(self):
		Animal.__init__(self, 4)
		Pet.__init__(self)

	@override
	def walk(self):
		return Animal.walk(self)

	@override
	def eat(self):
		return Animal.eat(self)

	@override
	def get_name(self):
		return Pet.get_name(self)

	@override
	def set_name(self, name:str):
		return Pet.set_name(self)

	@override
	def play(self):
		return Pet.play(self)
