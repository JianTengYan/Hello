percent_float = float(input("What is your percentage?"))

if 90 <= percent_float < 100:
	print("You Received an A")
elif 80 <= percent_float < 90:
	print("You Received an B")
elif 70 <= percent_float < 80:
	print("You Received an C")
elif 60 <= percent_float < 70:
	print("You Received an D")
else:
	print("Oopps, Not Good")
