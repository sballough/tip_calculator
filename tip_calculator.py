import sys

meal = float(sys.argv[1])
tip = float(sys.argv[2])
tax = float(sys.argv[3])

tax_value = meal * tax
tip_value = meal * tip
meal_with_tax = meal + tax_value

total = meal_with_tax + tip_value

print "The base cost of your meal was ${0:.2f}." .format (meal)
print "You need to pay a tip of ${0:.2f}" .format (tip_value)
print "You are being taxed ${0:.2f}" .format (tax_value)

print "The grand total of your meal is ${0:.2f}" .format (total)


