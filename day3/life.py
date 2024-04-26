# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.


enter = int(input('Enter number of years you have lived: '))

sec_for_year = 60*60*24*365

total_seconds = enter * sec_for_year

print('You have lived for',total_seconds,'seconds...')

