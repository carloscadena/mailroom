# mailroom

#Mail Room Madness

* Donor List as Key/Value Pair

###Function Definitions

##def thank\_or_report
	* function prompts the user to choose from 2 menu options:
```if option == 1 :```
         ```call send_thank_you function```
    ```if option == 2 :```
     	 ```call create_report function```  
##def send_thank_you


```
while in_thank_you:
	prompts user for full name or list 
	if input == 'list':
		print_donor_names():
	elif input in donor_list():
	    ask_for_a_donation_amount(input)
	elif input == 'q':
		in_thank_you = false
		thank_or_report()
	else:
		add_name_to_donor_list(input)
```



	
##def add_name_to_donor_list(name)
```
  ask_for_donation_amount(name)
```

##def create_email(name)
```
print('Thank you, {} for your donation of ${}'.format(name,donation[name][len(donation[name]-1)]))
create formatted string resembling an email thanking the donor along with donation amount
thank_or_report()
```

##def ask_for_donation_amount(name)
```
donation = input('Enter dollar amount: ')
if is_valid_donation(donation):
	donor_list[name] = donation
else:
	print('Enter the exact dollar amount: ')
	ask_for_donation_amount(name)

##def is_valid_donation(input)

return (input is float or input is int) and input > 0
```

##def create_report():
```
logic that formats the donor list information: 
donor name, total_donated, number_of_donations, average donation amount
thank_or_report()
```
