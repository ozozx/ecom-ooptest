from abc import *

class Animal(ABC):


	@abstractmethod
	def __init__(self, legs:int):
		self.legs = legs

	@abstractmethod
	def walk(self):
		pass

	@abstractmethod
	def eat(self):
		pass
