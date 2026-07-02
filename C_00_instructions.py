def string_check(question, valid_answers =('yes', 'no'),
                 num_letters=1):
    """checks that the user enters the full word
    or 'n' letter/s of a word fom a list of responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:
            if response == item:
                return item

            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_answers}")

def make_statement(statement, decoration):
    """add decoration at the start and end of text"""
    return f"{decoration * 3} {statement} {decoration * 3}"


def instructions():
    print(make_statement("instructions", "ℹ️"))

    print('''
    please enter your budget, the cost of each item, and the weight of each item,
    then you will be given the best item you could buy''')