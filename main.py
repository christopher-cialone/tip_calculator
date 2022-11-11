# print "welcome to the tip-calculator" message
print("Welcome to christopher_cialone's tip-calculator")




# variable meal equals an input as a float with text "enter the total bill"
meal = float(input('Enter the cost of meal $: '))
# variable tip equals an input the user chooses: 10, 15, 12....
tip = int(input('Enter the tip %: '))
# Constant variable added to every transaction - sales tax doesn't change
tax = int(input('Enter the state sales tax %: '))
ppl_splitting = int(input('Enter the number of people paying : '))

# calculations
# tip_amt is equal what the meal cost is multiplied by the number represented tip divided by 100
tip_amt = meal * tip/100
tax_amount = meal * tax/100
total = meal + tax_amount + tip_amt
total_per_person = total/ppl_splitting

print(f"\nYour meal was ${meal:.2f} and your tip was ${tip_amt:.2f}.")
print(f"Your total with tax was ${total:.2f}.\n")
print(f"\nEach person paying will pay ${total_per_person:.2f}.")

# create a function
# if else loop