running_total = 0

num_of_friends = 5

Bread = 2000
Beans = 1500 
Meat = 400
Fish = 400
Drinks = 1000

running_total = Bread + Beans + Meat + Fish + Drinks 
print("Total bill:", running_total)

tip = running_total * 0.10
print("Tip amount:", tip)

running_total += tip
print("Total with tip:", running_total)

final_bill = running_total / num_of_friends
print("Bill per person:", final_bill)



