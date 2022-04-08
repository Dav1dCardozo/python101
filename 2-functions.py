#NAME GREETING
def greet(first_name, last_name):
    print(f"Top of the morning to you, {first_name} {last_name}")



greet("David", "Cardozo")
greet("Eric", "Cartman")

# EMAIL GENERATOR
def email_gen(first_name, last_name, domain):
     print(first_name[0] + "." + last_name[0:5] + domain + ".com")


email_gen("Eric","Cartman","@starkindustries")

#USERNAME 
def user_name(first_name, last_name):
    print(first_name[0:3] + "_" + last_name[0:5])


user_name("Eric","Cartman")

