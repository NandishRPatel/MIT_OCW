
annual_salary = int(input("Enter your annual salary : "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal : "))
total_cost = int(input("Enter the cost of your dream home : "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal : "))


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
		current_savings += current_savings * (r / 12)  + (monthly_salary * portion_saved)
		months += 1
		if(months % 6 == 0):
			monthly_salary += monthly_salary * semi_annual_raise 
		#print(current_savings)

print("Number of months :",months)

