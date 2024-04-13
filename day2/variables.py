import inspect
# Get the local variables in the caller's scope
""" local_vars = inspect.currentframe().f_back.f_locals.items()
    # Get the global variables
global_vars = globals().items()
    
print("Local Variables:")
for name, value in local_vars:
        print(f"{name} = {value}")

print("\nGlobal Variables:")
for name, value in global_vars:
        print(f"{name} = {value}") """

var_name = 'Hari';
print(var_name)
print(type(var_name))
first_name = 'Hariharan';
print(first_name)
print(len(first_name))
print(type(first_name))
last_name = 'Dakshnamurthy';
print(last_name)
print(len(last_name))
print(type(last_name))
full_name = first_name + last_name;
print(full_name)
print(len(first_name)!=len(last_name))
print(type(full_name))
country = 'India';
print(country)
print(type(country))
city = 'Karur';
print(city)
print(type(city))
age = 24;
print(age)
print(type(age))
year = 2024;
print(year)
print(type(year))
isMarried = False
print(isMarried)
print(type(isMarried))
is_light_on = False
print(is_light_on)
print(type(is_light_on))
is_true = True
print(is_true)
print(type(is_true))


#print_all_variables()
