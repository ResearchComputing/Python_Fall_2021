#Read in the rate, compounding count, and principal
filename = 'interest_info.txt'
file = open(filename, 'r')
rate_str = file.readline() # Interest rate
comp_str = file.readline() # Number of times compounded annually
p_str    = file.readline() # The principal amount
file.close()

# Convert from string to floats
rate = float(rate_str)
comp = float(comp_str)
p    = float(p_str)

# Query the user + convert strting to float
t_str = input("How many years since you made the deposit?\n>> ")
t = float(t_str)

amount = p*( (1.0+rate/comp )**(comp*t)   )

#See formatting numbers.py
astr =  "{:.2f}".format(amount)
print("Your current balance is: $"+astr+".")


