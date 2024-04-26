# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120

hour = input('Enter hours: ')
hours = int(hour)
rate = input('Enter rate per hour: ')
rates= int(rate)

earn = hours * rates
weekly_earning = 7 * earn

print('Your weekly earning is:',weekly_earning)
