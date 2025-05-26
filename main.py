from regular_order import RegularOrder
from vip_order import VipOrder
from customer import Customer
from customer_type import CustomerType
from order_item import OrderItem
from payment import Payment
from ball import Ball
from cube import Cube
from datetime import date

def main():
	customers = [Customer(0, "Ben", "Meir", "ben.meir@ecom.co.il", "Raoul Wallenberg St 22, Tel Aviv-Yafo", CustomerType.VIP, 13.0, [], Ball("Blue")),
				 Customer(1, "Asaf", "Amir", "asaf.amir@appschool.co.il", "Opsterland St 4, Ra'anana", CustomerType.REGULAR, None, [], Cube(5)),
				 Customer(2, "Oz", "Oshri", "ozx.oshri@gmail.com", "Herbert Samuel St 54, Hadera", CustomerType.VIP, 2.0, [], Ball("Red"))]
	for customer in customers:
		customer.show_customer()
		customer.customer_gift.open_gift()
		print(f"{type(customer.customer_gift).__name__}\n")
	item_catalogue = [OrderItem(0,"Screws",5),
				 OrderItem(1,"Planks",15),
				 OrderItem(2,"Shingles",30),
				 OrderItem(3,"Rebar",20),
				 OrderItem(4,"Screws",7),
				 OrderItem(5,"Zip-ties",2),
				 OrderItem(6,"Tin Sheets",12),
				 OrderItem(7,"Steel Beam",50),
				 OrderItem(8,"Wood Rafts",6),
				 OrderItem(9,"Forklift",2000)]
	orders = [VipOrder(0, "Roofing Materials",customers[0].delivery_address,item_catalogue[0:3],customers[0],Payment.CREDIT_CARD,date(2026,2,6))]
	try:
		orders.append(VipOrder(1, "Roofing Materials",customers[1].delivery_address,item_catalogue[0:3],customers[1],Payment.CREDIT_CARD,date(2026,2,6)))
	except Exception as e:
		print(f"{type(e).__name__}: {e}\n")
	orders.append(RegularOrder(1, "Roofing Materials", customers[0].delivery_address, item_catalogue[0:3], customers[0], Payment.CREDIT_CARD, date(2026, 3, 6)))
	customers[0].list_favorites()
	orders.append(VipOrder(2, "Fencing Materials", "Tel-Aviv Haagana Train Station", [item_catalogue[1],item_catalogue[4],item_catalogue[6]], customers[0], Payment.CREDIT_CARD, date(2025, 11, 13)))
	customers[0].list_favorites()
	orders.append(RegularOrder(3, "Construction Materials", customers[1].delivery_address, item_catalogue[5:8], customers[1], Payment.CHECK, date(2025, 7, 22)))
	customers[1].list_favorites()
	try:
		customers[1].remove_from_favorites(item_catalogue[4])
	except Exception as e:
		print(f"{type(e).__name__}: {e}\n")
	customers[1].remove_from_favorites(item_catalogue[5])
	customers[1].list_favorites()
	customers[2].list_favorites()
	customers[2].add_to_favorites(item_catalogue[9])
	customers[2].list_favorites()
	orders.append(VipOrder(4, "Logistics Materials", customers[2].delivery_address, item_catalogue[8:], customers[2], Payment.CHECK, date.today()))
	for order in orders:
		print(f"#{order.id} \"{order.name}\": {order.calc_total_price()}$\ndue: {order.order_date.strftime('%d/%m/%Y')}")

if __name__ == '__main__':
	main()