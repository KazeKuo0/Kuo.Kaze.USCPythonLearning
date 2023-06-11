#Create variables
item1Name = "Apple"
item1Cost = 0.55
item1Quantity = 2

item2Name = "Pie"
item2Cost = 8.90
item2Quantity = 1

tax = 7.5

#Multiply cost by quantity to get total cost for item
item1TotalCost = item1Cost * item1Quantity
item2TotalCost = item2Cost * item2Quantity

#Sum the costs together
totalCost = item1TotalCost + item2TotalCost

#Add tax
costAfterTax = totalCost + totalCost * tax * 0.01

#Print output
print("Item 1: " + item1Name)
print("Cost: $" + str(item1Cost))
print("Number Purchased: " + str(item1Quantity))
print("")
print("Item 1: " + item2Name)
print("Cost: $" + str(item2Cost))
print("Number Purchased: " + str(item2Quantity))
print("")
print("Tax: " + str(tax) + "%")
print("Total Cost: $" + str(costAfterTax))
