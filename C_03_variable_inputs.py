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



budget = num_checker("please enter your budget:")

print(f"your budget is {budget}")