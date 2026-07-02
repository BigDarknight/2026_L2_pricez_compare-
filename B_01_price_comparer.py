def not_blank(question):
    """checks that user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response

        print("sorry this cant be blank. please try again. \n")

def num_checker(question, num_type="float", exit_code=None):
    """checks that the response is a float / integer more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."

    else:
        error = "Please enter an integer more than 0."

    while True:

        response = input(question)

        # check for exit code and return it if entered
        if response == exit_code:
            return response

        # check datatype is correct and that
        # number is more than zero
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

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

def yes_no(question):
    """checks user response to question is yes or no/y or n then returns yes or no"""
    while True:
        response = input(question).lower()
        #user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes (y) or no (n) \n")

def string_check(question, valid_ans_list):
    """checks that the user enters the full word
    or first letter of a word fom a list of responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:
            if response == item:
                return item

            elif response == item[0]:
                return item

        print(f"please choose an option from {valid_ans_list}")

# Heading (don't use statement generator)
print("💵💵💵price compare tool💵💵💵")

# instructions

want_instructions = yes_no("do you want instructions?")

if want_instructions == "yes":
    instructions()

budget = num_checker("please enter your budget:")

print(f"your budget is {budget}")

# Loop!
while True:
    #ask user for their name (and check it's not blank)
    print()
    item = not_blank("name of item: ")

    # if name is exit code, break out of loop
    if item == "xxx":
        break
    #get unit (blank is each)
    unit = string_check("please enter your unit:",
                        ['grams','kilograms', 'mills','liters',''  ])

    amount = num_checker("please enter the weight/volume/amount of the item:")

    cost = num_checker("please enter the cost of the item:".sum)

