'''This is a template for making a letter this will make the letter you have to give the details only'''
letter = '''
Address
Date

Dear Name

Let me begin by thanking you for your past contributions to our Little League baseball team. Your sponsorship aided in the purchase of ten full uniforms and several pieces of baseball equipment for last year's season.

Next month, our company is planning an employee appreciation pancake breakfast honoring retired employees for their past years of service and present employees for their loyalty and dedication in spite of the current difficult economic conditions.

We would like to place an order with your company for 25 pounds of pancake mix and five gallons of maple syrup. We hope you will be able to provide these products in the bulk quantities we require.

As you are a committed corporate sponsor and long-time associate, we hope that you will be able to join us for breakfast on date_of_meeting.

Respectfully yours,

 

Sender_Name'''
name = input('''Enter the name of person whom you want to send this letter\n''')
date = input('''Enter Date\n''')
address = input("Enter address\n")
sender_name = input("Enter sender name\n")
meeting = input("Enter meeting date\n")
letter = letter.replace("Name",name)
letter = letter.replace("Address",address)
letter = letter.replace("Sender_Name",sender_name)
letter = letter.replace("Date",date)
letter = letter.replace("date_of_meeting",meeting)
print(letter)