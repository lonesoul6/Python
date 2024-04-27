# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'

print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
hello_value = d['k1'][0]['nest_key'][1][0]
print(hello_value)

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

value = d['k1'][2]['k2'][1]['tough'][2][0]

print(value)

