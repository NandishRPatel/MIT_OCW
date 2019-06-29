
annual_salary = int(input("Enter your starting salary : "))

total_cost = 100000
semi_annual_raise = .07

current_savings = 0
portion_down_payment = .25
r = .04

need = total_cost * portion_down_payment
months = 36
monthly_salary = annual_salary / 12

lower = 0
upper = 1
stopping = 100

portion_saved = (lower + upper) / 2

steps = 0

for i in range(0,36):
	if i != 0 and i % 6 == 0:
		monthly_salary += monthly_salary * semi_annual_raise
	monthly_salary += monthly_salary * (r/12)
	current_savings += monthly_salary

if current_savings - need < stopping: print("CAN'T")
else:
	savings =  current_savings * portion_saved
	while(abs(savings - need) >= stopping):
		steps += 1
		if savings < need: lower = portion_saved
		else: upper = portion_saved
		portion_saved = (lower + upper) / 2
		savings = current_savings * portion_saved
	print(portion_saved)
	print(steps)