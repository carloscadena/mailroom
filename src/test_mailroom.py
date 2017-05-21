"""
Tests for mailroom
"""
import pytest

test_names = ['Carlos', 'Elyanil']
test_amount = [100, 200]

parameter_list_for_add_donation = [
    (test_names[0], test_amount[0], True),
    (test_names[1], test_amount[1], True)

]

test_donor_list = {
    'Carlos': [232, 32.34, 252],
    'Elyanil': [234.23, 2342, 2335],
    'Ely': [23.50, 255],
    'Anna': []
}

parameter_list_for_print_donor_list = [
    (test_donor_list, """------->[ Donors |\n------->[ Carlos |\n------->[ Elyanil |\n------->[ Ely |\n------->[ Anna |\n""")

    ]


parameter_list_for_create_email = [
    (test_names[0], test_amount[0], '''
    Dear {},

    Thank you so much for your donation of ${:.2f} dollars!

    Best Regards,

        The Establishment
     '''.format(test_names[0], test_amount[0])),
    (test_names[1], test_amount[1], '''
    Dear {},

    Thank you so much for your donation of ${:.2f} dollars!

    Best Regards,

        The Establishment
     '''.format(test_names[1], test_amount[1]))
]

parameter_list_for_is_valid_donation = [
    ('Hi', False), (100, True), (65.43, True), (-12, False)
]


@pytest.mark.parametrize('name, amount, result', parameter_list_for_add_donation)
def test_add_donation(name, amount, result):
    from mailroom import add_donation
    assert add_donation(name, amount) == result


@pytest.mark.parametrize('name, amount, result', parameter_list_for_create_email)
def test_create_email(name, amount, result):
    from mailroom import create_email
    assert create_email(name, amount) == result


@pytest.mark.parametrize('amount, result', parameter_list_for_is_valid_donation)
def test_is_valid_donation(amount, result):
    from mailroom import is_valid_donation
    assert is_valid_donation(amount) == result


@pytest.mark.parametrize('donor_list, result', parameter_list_for_print_donor_list)
def test_print_donor_name(donor_list, result):
    from mailroom import print_donor_names
    assert print_donor_names(donor_list) == result
