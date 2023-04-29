from flet import *
import random
import string
from cardcustomer import Cardcustomer




def main(page:Page):
	foods = []
	# NOW GET IMAGE FROM YOU foods FOLDER
	# AND SET FOOD NAME WITH RANDOM PRICE 
	image_files = ["burger.jpg","drinks.jpeg","pizza.jpeg"]
	food_names = ["burger","drinks","pizza"]
	food_prices = [5.99,9.88,4.22]

	# AND FOR GRAND TOTAL 
	grand_total = Text("$0",size=30,weight="bold")

	# CREATE CONTAINER FOR LIST FOOD 
	con_food = Row()

	# NOW LOOP AND CREATE DICT
	for i in range(len(food_names)):
		food = {}
		food['name'] = food_names[i]
		food['price'] = food_prices[i]
		food['photo'] = "foods/" + image_files[i]
		foods.append(food)

	# AND NOW APPEND TO CONAINER
	if len(foods) > 0 :
		for x in foods:
			con_food.controls.append(
				Container(
				padding=10,
				content=Column([
					# AND CREATE DRAG FOR YOU DRAG TO CONTAINER
					Draggable(
						# AND I CREATE CONTAINER
						content=Container(
						content=Column([
					Image(src=x['photo'],width=120,height=80),
					Text(x['name']),
					Text(x['price']),

							])
							)
						)

					])
					)
				)

	def changecolor(e):
		# AND IF YOU WILL DRAG TO HERE THEN CHANGE
		# BGCOLOR TO ORANGE
		e.control.content.bgcolor="orange200"
		page.update()

	# NOW I CREATE RANDOM UNIQUE ID FOR DELETE
	def generate_you_id(length):
		char = string.ascii_uppercase + string.ascii_lowercase + string.digits

		# AND GENERATE RANDOM 
		unique_code = ''.join(random.choices(char,k=length))
		return unique_code

	def removedata(e):
		# AND NOW REMOVE IF YOU CLICK ICON BUTTON RED
		for x in drag_area.content.content.controls:
			# NOW FIND UID IN YOU e.cntrol.data
			# IF FOUND THEN REMOVE
			if x.controls[3].value == e.control.data:
				drag_area.content.content.controls.remove(x)
		total = 0
		# AND FOR GRAND TOTAL IS CALCULATE AGAIN
		for x in drag_area.content.content.controls:
			price = float(x.controls[2].value)
			total += price
		grand_total.value = f"${total:.2f}"
		page.update()




	def addtolist(e):
		# GET DATA FROM CONTAINER 
		src = page.get_control(e.src_id)
		uid = generate_you_id(5)
		# AND NOW APPEND YOU FOOD CONTAINER TO HERE
		e.control.content.content.controls.append(
				Column([
			Image(src.content.content.controls[0].src,
			width=80,height=50
				),
			Text(src.content.content.controls[1].value,weight="bold"),
			# AND FOR PRICE
			Text(src.content.content.controls[2].value),
			Text(uid,visible=False),
			IconButton(icon="close",icon_color="red",
				data=uid,
				on_click=removedata
				)

					])

			)
		# AND NOW CALCULATE GRAND TOTAL
		total = 0
		for x in e.control.content.content.controls:
			# GET INDEX OF PRICE
			price = float(x.controls[2].value)
			total +=price
		grand_total.value = f"${total:.2f}"
		page.update()


	def cancelyoudrag(e):
		# AND NOW IF YOU CANCEL FOR DRAG HERE
		# THEN CHANGE AGAIN BGCLOR TO BLUE
		e.control.content.bgcolor="blue200"
		page.update()


	# AND NOW CREATE DRAG_AREA FOR LIST YOU ORDER FOOD
	drag_area = DragTarget(
		content=Container(
			padding=10,
			width=600,
			height=300,
			bgcolor="blue200",
			content=Row(wrap=True,scroll="auto")
			),
		# AND CREATE FUNCTION IF YOU WILL DRAG TO THIS
		# CONTAINER
		# THEN RUN FUNCTION
		on_will_accept=changecolor,
		# AND IF SUCCESS DRAG TO HERE
		on_accept=addtolist,
		# AND IF YOU CANCEL DRAG THEN CHANE TO BLUE BGCLOR
		# AGAIN
		on_leave=cancelyoudrag

		)


	page.add(
	# AND NOW CREATE 2 SECTION ROW
	# FOR CUSTOMER AND FOOD DRAG
	Row([
		Cardcustomer(page),
		Column([
			Card(
			content=Column([
			Text("card order",size=30,weight="bold"),
			con_food

				])
				),
			drag_area,
			# AND FOR CONTAINER GRAND TOTAL
			Container(
			content=Row([
				Text("grand total",size=30),
				grand_total
				])

				)

			],alignment="spaceEvenly")
		])

		)

flet.app(target=main,assets_dir="foods")
