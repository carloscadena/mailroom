import sys
"""
Solutions for mailroom
"""

donor_list = {
    'Carlos': [232, 32.34, 252],
    'Elyanil': [234.23, 2342, 2335],
    'Ely': [23.50, 255],
    'Anna': [0.00, 0, 0.00]
}

PROMPTS = {
    'thank_or_report': """\n
    Would you like to send a 'Thank you Email' or 'Create a Report'?

    Select 1 for 'Thank you Email' or 2 for 'Create a Report'
    ('q' to exit.):""",
    'send_thank_you': """\n
    Enter the donor's full name or to see a list of donors type 'list'
    ('q' to restart): """,
    'ask_for_a_donation_amount': """Enter donation amount: """,

    }
PROMPTS_WRONG_INPUT = {
    'thank_or_report': """Invalid selection. Please select either 1 or 2.
    (q to exit.)""",
    'ask_for_a_donation_amount': 'Enter a (positive) number. Please: '

}


def thank_or_report(prompt=PROMPTS['thank_or_report']):
    selection = input_handler(PROMPTS['thank_or_report'])
    if selection == '1':
        send_thank_you()
    elif selection == '2':
        print(create_report(donor_list))
    elif selection == 'q':
        sys.exit()
    else:
        thank_or_report(PROMPTS_WRONG_INPUT['thank_or_report'])


def send_thank_you():  # pragma: no cover
    user_input = input_handler(PROMPTS['send_thank_you'])
    if user_input == 'list':
        if '------->[ Donors |\n' not in print_donor_names(donor_list):
            send_thank_you()
        print(print_donor_names(donor_list))
    elif user_input == 'q':
        thank_or_report()
    elif user_input in donor_list:
        ask_for_a_donation_amount(user_input)
    else:
        if add_name_to_donor_list(user_input):
            ask_for_a_donation_amount(user_input)


def print_donor_names(donor_list):
    """
    print donor names to command line
    """
    if not isinstance(donor_list, dict):
        return 'Input value is not a dictionary.'
    if len(donor_list.keys()) > 0:
        roster = """------->[ Donors |\n"""
        for donor in donor_list.keys():
            roster += """------->[ {} |\n""".format(donor)
        return roster
    else:
        return 'The donor list is empty.'


def add_name_to_donor_list(name):
    """
    adds new donor to list of donors
    """

    donor_list[name] = [0.00, 0, 0.00]

    # returns 'True' to indicate that the name has been added to the list
    return True



def create_email(name, amount):
    """
    create email thanking the donor
    """
    if isinstance(name, str) and isinstance(amount, float) or isinstance(amount, int):
        return '''
    Dear {},

    Thank you so much for your donation of ${:.2f} dollars!

    Best Regards,

        The Establishment
     '''.format(name, amount)

    return """One of the input values provided is invalid."""


def ask_for_a_donation_amount(name, prompt=PROMPTS['ask_for_a_donation_amount']):  # pragma: no cover
    """
    prompts for donor's donation amount
    """
    user_donation = input_handler(prompt)
    checks_donation(name, user_donation)


def checks_donation(name, amount):  # pragma: no cover
    """
    checks the donation amount
    """
    if is_valid_donation(amount):
        add_donation(name, amount)
        send_email(name, float(amount))
        return True
    else:
        ask_for_a_donation_amount(name, PROMPTS_WRONG_INPUT['ask_for_a_donation_amount'])
        return False


def add_donation(name, amount):
    """
    add donation to donation_list
    """
    if name not in donor_list:
        add_name_to_donor_list(name)
    donor_list[name].append(float(amount))
    return True


def is_valid_donation(amount):
    """
    checks to see if amount is a number
    """
    try:
        float(amount)
        return float(amount) > 0
    except ValueError:
        return False


def input_handler(prompt):  # pragma: no cover
    """
    responsible for handling input
    """
    user_response = input(prompt)
    return user_response


def create_report(donor_list):
    """
    creates the report
    """
    calculations = prepare_donor_list_for_report(donor_list)

    sorted_calculations = sort_by_donation_amount(calculations)

    table = creates_table_for_report(sorted_calculations)
    return table


def prepare_donor_list_for_report(a_donor_list):
    """
    Calculates total amount contributions, number of contributions,
    and avg. donation amount for each donor
    """
    contributions_calculations = {}
    for donor in a_donor_list:
        if len(a_donor_list[donor]) != 0:
            contributions_calculations[donor] = [
                sum(a_donor_list[donor]),
                len(a_donor_list[donor]),
                sum(a_donor_list[donor])/len(a_donor_list[donor])]
        else:
            contributions_calculations[donor] = [
                sum(a_donor_list[donor]),
                len(a_donor_list[donor]),
                sum(a_donor_list[donor])]

    return contributions_calculations


def sort_by_donation_amount(contributions):
    contributions = sorted(
        contributions.items(),
        key=lambda x: x[1], reverse=True)
    return contributions


def creates_table_for_report(contributions):
    table = ('='*10).join(
        [' Name ', ' Total Amount ', ' # of Contributions ', ' Avg. Donation Amount'])
    table += '\n'
    table += ('-'*len(table))
    table += '\n'

    for donor in contributions:
        if len(str(donor[1][0])) > 6:
            table += '{00:18}'.format(donor[0])
            table += '${00:.2f}'.format((donor[1][0]))
            table += '{00:24}'.format((donor[1][1]))
            table += '{0:25}'.format('')
            table += '${00:.2f}'.format((donor[1][2]))
        elif len(str(donor[1][0])) <= 3:
            table += '{00:18}'.format(donor[0])
            table += '${00:.2f}'.format((donor[1][0]))
            table += '{00:27}'.format((donor[1][1]))
            table += '{0:25}'.format('')
            table += '${00:.2f}'.format((donor[1][2]))
        else:
            table += '{00:18}'.format(donor[0])
            table += '${00:.2f}'.format((donor[1][0]))
            table += '{00:25}'.format((donor[1][1]))
            table += '{0:25}'.format('')
            table += '${00:.2f}'.format((donor[1][2]))
        table += '\n'
    return table


def send_email(name, amount):  # pragma: no cover
    """
    prints the email to the console
    """

    print(create_email(name, sum(donor_list[name])))
    thank_or_report()


if __name__ == '__main__':
    thank_or_report()
