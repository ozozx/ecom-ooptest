from typing_extensions import override
from datetime import date
from customer_type import CustomerType
from regular_order import RegularOrder
from customer import Customer
from payment import Payment

class VipOrder(RegularOrder):


	def __init__(self, id:int, name:str, delivery_address:str, item_list:list, order_customer:Customer, payment_type:Payment, order_date:date):
		super().__init__(id, name, delivery_address, item_list, order_customer, payment_type, order_date)
		self.order_total_price = self.calc_total_price()

	@override
	def calc_total_price(self):
		if not self.order_customer.customer_type == CustomerType.VIP:
			raise TypeError("Tried to initialize VIP order with non-VIP customer")
		price = super().calc_total_price()
		if not self.order_customer.customer_discount == None:
			price-=self.order_customer.customer_discount
		return price