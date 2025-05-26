from datetime import date
from payment import Payment
from order_item import OrderItem
from customer import Customer


class RegularOrder:

	def __init__(self, id:int, name:str, delivery_address:str, item_list:list, order_customer:Customer, payment_type:Payment, order_date:date):
		self.id = id
		self.name = name
		self.delivery_address = delivery_address
		self.item_list = item_list
		self.order_customer = order_customer
		self.order_total_price = self.calc_total_price()
		self.payment_type = payment_type
		self.order_date = order_date
		for item in self.item_list:
			self.order_customer.add_to_favorites(item)

	def calc_total_price(self):
		price_sum = 0
		for item in self.item_list:
			if not type(item) == OrderItem:
				raise TypeError("Non-Item found in list of order items")
			price_sum += item.item_price
		return float(price_sum)