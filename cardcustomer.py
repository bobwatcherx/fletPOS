from flet import *
# INSTALL YOU FAKER FOR RANDOM NAME CUSTOMER
from faker import Faker

fake = Faker()

def Cardcustomer(page):

	data = []

	def changeyoucustomer(e):
		con_address.content.controls[0].controls[1].value = e.control.value

		# AND NOW SET FOR ADDRESS
		for x  in data:
			if x['name'] == e.control.value:
				con_address.content.controls[1].controls[1].value = x['address']
		page.update()



	# AND NOW CREATE DROPDOWN FOR RANDOM NAME
	db = Dropdown(
		width=200,
		on_change=changeyoucustomer,
		options=[]
		)
	 # AND NOW CREATE RANDOM NAME 3 NAME
	for i in range(3):
		dic_data= {}
		dic_data['name'] = fake.name()
		dic_data['address'] = fake.address()
		data.append(dic_data)

	 # AND NOW APPEND YOU FAKE DATA TO DROPDOWN
	if len(data) > 0:
		for x in data:
			db.options.append(
				dropdown.Option(x['name'])
				)

	# AND NOW SHOW ADDRESS WHEN YOU SELECT NAME
	con_address = Container(
		content=Column([
			Row([
				Text("Cust name : "),
				# AND HERE FOR NAME
				Text(size=20,weight="bold")
				]),
			Row([
				Text("address : "),
				Text(weight="bold")
				])
			])
		)


	return Card(
		content=Container(
		padding=10,
		content=Column([
			Text("customer data",size=25,weight="bold"),
			db,
			con_address 
			])
			)
		)
