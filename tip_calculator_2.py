

meal = raw_input("What was the price of the meal before tax?")
tax = raw_input("What was the tax?")
tip = raw_input("What is the tip?")

m = float (meal)
ta = float (tax)
ti = float (tip)

tax_value = m * ta
meal_with_tax = m * (1 + ta)
tip_value = ti * m

total = meal_with_tax + tip_value

print "The base cost of you meal was $%.2f" % meal_with_tax
print "The tax rate is %.2f" % ta
print "You need to pay $%.2f for tax" % tax_value
print "You should leave $%.2f for a tip" % tip_value
print "The grand total of your meal is $%.2f" % total