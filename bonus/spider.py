
from typing_extensions import override
from animal import Animal

class Spider(Animal):


	def __init__(self):
		super().__init__(8)

	@override
	def walk(self):
		pass

	@override
	def eat(self):
		pass
