from fontTools.merge.util import first

from customer_type import CustomerType
from giftable import Giftable
from order_item import OrderItem


class Customer:


	def __init__(self, id:int, first_name:str, last_name:str, email:str, delivery_address:str, customer_type:CustomerType, customer_discount, favorite_items_list:list, customer_gift:Giftable):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.delivery_address = delivery_address
		self.customer_type = customer_type
		self.customer_discount = customer_discount
		self.favorite_items_list = favorite_items_list
		self.customer_gift = customer_gift

	def show_customer(self):
		print(f"#{self.id}: {self.first_name} {self.last_name}\n{self.customer_type.value} customer{(', '+str(self.customer_discount)+'$ discount')*(self.customer_type==CustomerType.VIP)}.\n{self.email}\n{self.delivery_address}\n")

	def list_favorites(self):
		print(f"{self.first_name} {self.last_name}'s favorites:")
		for item in self.favorite_items_list:
			print(f"\t#{item.id}: {item.item_name} {item.item_price}$")
		print()

	def add_to_favorites(self, item:OrderItem):
		for fav in self.favorite_items_list:
			if fav.item_name == item.item_name or fav.id == item.id:
				return
		self.favorite_items_list.append(item)

	def remove_from_favorites(self, remove_item:OrderItem):
		if not remove_item in self.favorite_items_list:
			raise ValueError("Tried to remove non-existent item in favorite list")
		self.favorite_items_list.remove(remove_item)

	def take_gift(self, gift:Giftable):
		self.customer_gift = gift
