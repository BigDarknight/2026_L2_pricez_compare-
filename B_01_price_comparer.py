import pandas

def not_blank(question):
    """checks that user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response

        print("sorry this cant be blank. please try again. \n")

def num_checker(question):
    """checks that the response is a float / integer more than zero"""

    error = "Oops - please enter a number more than zero"

    while True:

        response = input(question).lower()


        try:
            # change the response to an integer and check that it's more than zero
            response = float(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def instructions():
    print("ℹ️ℹ️ℹ️ instructions ℹ️ℹ️ℹ️")

    print('''

    please enter your budget, the cost of each item, and the weight of each item,
    then you will be given the best item you could buy with your budget. 
    ''')

def string_check(question, valid_ans_list, num_letters):
    """checks that the user enters the full word
    or 'n' letter/s of a word fom a list of responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:
            if response == item:
                return item

            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_ans_list}")

def currency(x):
    """formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)

# main routine

#lists for pandas
all_items = []
all_amounts = []
all_units = []
all_prices = []
all_prices_per = []

price_clac_dict = {
    "item": all_items,
    "amount": all_amounts,
    "unit": all_units,
    "price": all_prices,
    "priceper": all_prices_per
}


# Heading (don't use statement generator)
print("💵💵💵price compare tool💵💵💵")

# instructions

want_instructions = string_check("do you want instructions?",
                                  ('yes', 'no'),  1)


if want_instructions == "yes":
    print(instructions())

budget = num_checker("please enter your budget:")
budget_money = f"${budget:.2f}"

print(f"your budget is {budget}")

# Loop for inputs
while True:
    #ask user for the name of the item (and check it's not blank)
    print()
    item = not_blank("name of item: ")

    # if name is exit code, break out of loop
    if item == "xxx":
        break
    #get unit (blank is each)
    unit = string_check("please enter your unit:",
                        ['grams','kilograms', 'mills','liters',''  ], 1)
    # get amount of product
    amount = num_checker("please enter the weight/volume/amount of the item:")
    # get price of product
    cost_input = num_checker("please enter the cost of the item:")
    # convert cost to correct formating
    cost = f"${cost_input:.2f}"

    print("unit: ", unit)

    # get price per unit and convert to currency format.
    if unit == 'grams' or unit == 'mills':
        print("amount: ", amount)
        amount_divided = amount / 1000
        cost_per_raw = cost_input /  amount_divided
        vari = "true"
    else:
        cost_per_raw = cost_input / amount
        vari = "false"
    # cost_per = f"${cost_per_raw:.2f}"

    all_items.append(item)
    all_amounts.append(amount)
    all_units.append(unit)
    all_prices.append(cost)
    all_prices_per.append(cost_per_raw)

#create table
price_compare_frame = pandas.DataFrame(price_clac_dict)
#remove unneeded index
price_compare_table = price_compare_frame.to_string(index=False)

print("if you put in your unit as grams or mills then your price per will "
      "be given in kilograms or liters  ")

best = min(all_prices_per)

print(price_compare_table)

print(f"the best item you can buy costs {best} per unit")





