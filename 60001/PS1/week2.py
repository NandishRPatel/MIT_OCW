
annual_salary = int(input("Enter your annual salary : "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal : "))
total_cost = int(input("Enter the cost of your dream home : "))

current_savings = 0
portion_down_payment = 0.25
r = 0.04

need = total_cost * portion_down_payment
months = 0
monthly_salary = annual_salary / 12
flag = True

while(flag):
	if(current_savings - need >= 0):
		flag = False
	else:
		months += 1
		current_savings += current_savings * (r / 12)  + (monthly_salary * portion_saved)
		#print(current_savings)
		

print("Number of months :",months)
