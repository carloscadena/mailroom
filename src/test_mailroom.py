"""
Tests for mailroom
"""
import pytest

test_names = ['Carlos', 'Elyanil', 'Serpentor', 'Liono', 'Snarf']
test_amount = [100.00, 200, 1000.00, 670.00, 3000.00]

parameter_list_for_add_donation = [
    (test_names[0], test_amount[0], True),
    (test_names[1], test_amount[1], True),
    (test_names[2], test_amount[2], True),
    (test_names[3], test_amount[3], True),
    (test_names[4], test_amount[4], True)

]

test_donor_list = {
    'Carlos': [232, 32.34, 252],
    'Elyanil': [234.23, 2342, 2335],
    'Ely': [23.50, 255],
    'Anna': [0.00, 0, 0.00]
}

test_donor_list_2 = {
    'Ted': [232, 32.34, 252, 500, 212.00, 768.00],
    'Mel': [234.23, 2342, 2335, 81.78, 84.90],
    'Fiona': [23.50, 255, 10000.00],
    'Anne': [0.00, 0, 0.00]
}

test_donor_list_3 = {
    'Ned': [212, 37.34, 242, 800, 216.00, 734.50],
    'Melly': [224.23, 2142, 2435, 81.78, 84.40],
    'Francis': [23.50, 255, 10000.00],
    'Andy': [123.50, 892.89, 0.01, 78.98, 67]
}

test_donor_list_4 = {
    'Maude': [230.89, 373.34, 312.00, 89.10, 75.00, 78.50],
    'Armin': [314.23, 1132, 3353, 91.88, 86.45],
    'Edna': [31.70, 346, 10560.00],
    'Willie': [217.41, 371.99, 0.59, 78.34, 67.87]
}

parameter_list_for_prepare_donor_list_for_report = [
    (test_donor_list, {
        'Carlos': [516.34, 3, 172.11333333333334],
        'Elyanil': [4911.23, 3, 1637.0766666666666],
        'Ely': [278.5, 2, 139.25],
        'Anna': [0.0, 3, 0.0]}),
    (test_donor_list_2, {
        'Ted': [1996.3400000000001, 6, 332.72333333333336],
        'Mel': [5077.909999999999, 5, 1015.5819999999998],
        'Fiona': [10278.5, 3, 3426.1666666666665],
        'Anne': [0.0, 3, 0.0]}),
    (test_donor_list_3, {
        'Ned': [2241.84, 6, 373.64000000000004],
        'Melly': [4967.409999999999, 5, 993.4819999999997],
        'Francis': [10278.5, 3, 3426.1666666666665],
        'Andy': [1162.3799999999999, 5, 232.47599999999997]}),
    (test_donor_list_4, {
        'Maude': [1158.83, 6, 193.13833333333332],
        'Armin': [4977.5599999999995, 5, 995.512],
        'Edna': [10937.7, 3, 3645.9],
        'Willie': [736.2, 5, 147.24]

    })
]

parameter_list_for_print_donor_list = [
    (test_donor_list, """------->[ Donors |
------->[ Carlos |
------->[ Elyanil |
------->[ Ely |
------->[ Anna |"""),
    ({}, 'The donor list is empty.'),
    (test_donor_list_2, """------->[ Donors |
------->[ Ted |
------->[ Mel |
------->[ Fiona |
------->[ Anne |"""),
    ([], 'Input value is not a dictionary'),
    (128314923479823142314, 'Input value is not a dictionary.'),
    ((' ',), 'Input value is not a dictionary.')

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
     '''.format(test_names[1], test_amount[1])), ([], 'Money', """One of the input values provided is invalid."""),
     ([], {}, """One of the input values provided is invalid."""),
     ([], {}, """One of the input values provided is invalid."""),
     ({}, [], """One of the input values provided is invalid.""")
]

parameter_list_for_is_valid_donation = [
    ('Hi', False), (100, True), (65.43, True), (-12, False), (150000, True)
]

parameter_list_for_add_name_to_donor_list = [
    ('Brian', True),
    ('Peter', True),
    ('Big Bird', True),
    ('Papa Bear', True),
    ('Justin Trudeau', True),
    ('Justin Bieber', True)
]

parameter_list_for_sort_by_donation = [
    (test_donor_list, [
        ('Elyanil', [4911.23, 3, 1637.0766666666666]),
        ('Carlos', [516.34, 3, 172.11333333333334]),
        ('Ely', [278.5, 2, 139.25]),
        ('Anna', [0.0, 3, 0.0])]),
    (test_donor_list_2, [
        ('Fiona', [10278.5, 3, 3426.1666666666665]),
        ('Mel', [5077.909999999999, 5, 1015.5819999999998]),
        ('Ted', [1996.3400000000001, 6, 332.72333333333336]),
        ('Anne', [0.0, 3, 0.0])]),
    (test_donor_list_3, [
        ('Francis', [10278.5, 3, 3426.1666666666665]),
        ('Melly', [4967.409999999999, 5, 993.4819999999997]),
        ('Ned', [2241.84, 6, 373.64000000000004]),
        ('Andy', [1162.3799999999999, 5, 232.47599999999997])]),
    (test_donor_list_4, [
        ('Edna', [10937.7, 3, 3645.9]),
        ('Armin', [4977.5599999999995, 5, 995.512]),
        ('Maude', [1158.83, 6, 193.13833333333332]),
        ('Willie', [736.2, 5, 147.24])])
        ]

parameter_list_for_creates_table_for_report = [
    (test_donor_list, """ Name ========== Total Amount ========== # of Contributions ========== Avg. Donation Amount
--------------------------------------------------------------------------------------------
Elyanil           $4911.23                       3                         $1637.08
Carlos            $516.34                        3                         $172.11
Ely               $278.50                        2                         $139.25
Anna              $0.00                          3                         $0.00\n"""),
    (test_donor_list_2, """ Name ========== Total Amount ========== # of Contributions ========== Avg. Donation Amount
--------------------------------------------------------------------------------------------
Fiona             $10278.50                       3                         $3426.17
Mel               $5077.91                       5                         $1015.58
Ted               $1996.34                       6                         $332.72
Anne              $0.00                          3                         $0.00\n"""),
    (test_donor_list_3, """ Name ========== Total Amount ========== # of Contributions ========== Avg. Donation Amount
--------------------------------------------------------------------------------------------
Francis           $10278.50                       3                         $3426.17
Melly             $4967.41                       5                         $993.48
Ned               $2241.84                       6                         $373.64
Andy              $1162.38                       5                         $232.48\n"""),
    (test_donor_list_4, """ Name ========== Total Amount ========== # of Contributions ========== Avg. Donation Amount
--------------------------------------------------------------------------------------------
Edna              $10937.70                       3                         $3645.90
Armin             $4977.56                       5                         $995.51
Maude             $1158.83                       6                         $193.14
Willie            $736.20                        5                         $147.24\n""")
]


@pytest.mark.parametrize('name, amount, result', parameter_list_for_add_donation)
def test_add_donation(name, amount, result):
    """
    tests the add_donation function
    """
    from mailroom import add_donation
    assert add_donation(name, amount) == result


@pytest.mark.parametrize('name, amount, result', parameter_list_for_create_email)
def test_create_email(name, amount, result):
    """
    tests the create_email function
    """
    from mailroom import create_email
    assert create_email(name, amount) == result


@pytest.mark.parametrize('amount, result', parameter_list_for_is_valid_donation)
def test_is_valid_donation(amount, result):
    """
    tests the is_valid_donation function
    """
    from mailroom import is_valid_donation
    assert is_valid_donation(amount) == result


@pytest.mark.parametrize('donor_list, result', parameter_list_for_print_donor_list)
def test_print_donor_name(donor_list, result):
    """
    tests the print_donor_name function
    """
    from mailroom import print_donor_names
    result = print_donor_names(donor_list)
    assert print_donor_names(donor_list) == result


@pytest.mark.parametrize('donor_name, result', parameter_list_for_add_name_to_donor_list)
def test_add_name_to_donor_list(donor_name, result):
    """
    tests the add_name_to_donor_list function
    """
    from mailroom import add_name_to_donor_list
    assert add_name_to_donor_list(donor_name) == result


@pytest.mark.parametrize('donor_list, result', parameter_list_for_prepare_donor_list_for_report)
def test_prepare_for_donor_list(donor_list, result):
    """
    tests the prepare_donor_list_for_report function
    """
    from mailroom import prepare_donor_list_for_report
    assert prepare_donor_list_for_report(donor_list) == result


@pytest.mark.parametrize('donor_list, result', parameter_list_for_sort_by_donation)
def test_sort_by_donation_amount(donor_list, result):
    """
    tests the sort_by_donation_amount function
    """
    from mailroom import sort_by_donation_amount, prepare_donor_list_for_report
    prepared_donor_list = prepare_donor_list_for_report(donor_list)
    assert sort_by_donation_amount(prepared_donor_list) == result


@pytest.mark.parametrize('donor_list, result', parameter_list_for_creates_table_for_report)
def test_creates_table_for_report(donor_list, result):
    """
    tests the creates_table_for_report function
    """
    from mailroom import creates_table_for_report, sort_by_donation_amount, prepare_donor_list_for_report
    assert creates_table_for_report(sort_by_donation_amount(prepare_donor_list_for_report(donor_list))) == result


@pytest.mark.parametrize('donor_list, result', parameter_list_for_creates_table_for_report)
def test_create_report(donor_list, result):
    """
    test the create_report function
    uses the same parameter list as the test_creates_table_for_report function
    """
    from mailroom import create_report
    assert create_report(donor_list) == result
