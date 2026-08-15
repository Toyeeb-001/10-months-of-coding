num_of_friends = 4
running_total = 0

appetizers = 42.15   
main_courses = 57.34
desserts = 28.50     
drinks = 64.21

subtotal_cost = appetizers + main_courses + desserts + drinks
running_total += subtotal_cost
print(f"Total bill so far: {running_total}")

tip = running_total * 0.25
print(f"Tip amount: {tip}")


running_total += tip
print(f"Total with tip: {running_total}")

final_bill = running_total / num_of_friends
print(f"Bill per person: {final_bill}")

