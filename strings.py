# assignment operator = 
#dog = "nelson" # assigning value "nelson" to the variable 'dog' # doesn't work because the string uses single quotes
#string containing single quotes needs double quotes
#introduction = "nelson's name is nelson"
# strings with both need triple quotes
#introduction = """nelson's name is "nelson"!"""
# characters can be "escaped" using backslash
#introduction = "my dog's name is \"nelson\""

# multi-line strings
# use triple quotes to use newlines
#long_introduction = """


#my dog's name is "nelson"

user_details = "password: helloworld!123"
print(user_details[5])

first_name = "David"
last_name = "Cardozo"

greeting = "Welcome to E Corp, " + first_name + " " + last_name
print(greeting)


email = "Email: " + first_name[0] + "." + last_name + "@ecorp.com"
print(email)

user_name = "Username: " + first_name[0:3] + "_" + last_name[0:5]
print(user_name)