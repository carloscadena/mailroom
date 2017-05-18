"""
Solutions for mailroom
"""
import pytest

donor_list = {
    'Carlos': [232, 32.34, 252],
    'Elyanil': [234.23, 2342, 2335],
    'Ely': [23.50, 255],
    'Anna': []
}

def thank_or_report():
    selection = int(input("""Would you like to send a 'Thank you Email' or 'Create a Report'?\n
    Select 1 for 'Thank you Email' or 2 for 'Create a Report'"""))
    if selection == 1:
        send_thank_you()
    elif selection == 2:
        create_report()
    else:
        print('Invalid selection. Please select either 1 or 2.')
        thank_or_report()


@pytest.fixture
def send_thank_you():
    user_input = input("""Enter the donor's full name or to see a list of donors type 'list'.\n
                       Type 'q' to quit.""")
    if user_input == 'list':
        print_donor_names()
    elif user_input == 'q':
        thank_or_report()
    elif user_input in donor_list:
        print('Inside user_input in donor_list clause: ', user_input)
        ask_for_a_donation_amount(user_input)
    else:
        add_name_to_donor_list(user_input)


def add_name_to_donor_list(name):
    donor_list[name] = []
    ask_for_a_donation_amount(name)


def create_email(name, amount):
    print('')


def ask_for_a_donation_amount(name):
    user_donation = input("""Enter donation amount: """)
    if is_valid_donation(float(user_donation)):
        donor_list[name].append(float(user_donation))
    else:
        ask_for_a_donation_amount(name)


def is_valid_donation(amount):
    return amount is float and amount > 0


def create_report():
    print('')


if __name__ == '__main__':
    thank_or_report()
