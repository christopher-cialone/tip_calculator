# tip_calculator
def cialone_python_calculator():
  
  # print message
  print("Welcome to christopher_cialone's tip-calculator")
  # variable meal set to what the user inputs
  meal = float(input('Enter the cost of meal $: ')) 
  # variable tip set to an input of the user choice
  tip = float(input('Enter the tip %: '))
  # variable tax set to an input of the user state sales tax
  tax = float(input('Enter the state sales tax %: '))
  # variable ppl_splitting set to the number of people paying 
  ppl_splitting = int(input('Enter the number of people paying : '))

# calculations
 
  tip_amt = meal * tip/100 
# from % to $ to leave as tip
  tax_amount = meal * tax/100 
#the amount the tax came to
  total = meal + tax_amount + tip_amt 
# adding your cost of meal, and the taxes, and the amount of money left for tip (everything) together, is the total
  total_per_person = total/ppl_splitting # the total bill(including taxes and tip) divided by the number of people. Even-Stevens
  
  print(f"\nYour meal was ${meal:.2f} and your tip was ${tip_amt:.2f}.")
  print(f"Your total with tax was ${total:.2f}.\n")
  print(f"\nEach person paying will pay ${total_per_person:.2f}.")

# 
# this statement is giving the option to the user, whether or not they would like to continue on and calculate more
  the_next_tip = input('Press n to exit or continue on by entering any number ')
  print(the_next_tip)
  for answer in the_next_tip:
      if answer == 'n': # 'n' is the exit from our program
         print('Thanks for stopping by, may the force be with you')
         return  
      else:
          the_next_tip == 'y'
          cialone_python_calculator()
        # or else the function calculates more meals and tips! 
cialone_python_calculator()