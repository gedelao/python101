#Input accepts user input and returns that value as a string
# which can be stored in a variable and used later




def say_hello(first_name, last_name):
    print(f'Hello, {first_name} {last_name}  welcome to the introduction to function! ')
    say_hello('Gerardo', 'Delao')
    say_hello('Erin', 'Cranston')
    
#username Generator

def email_gen(first_name, last_name, domain):
    print(f'{first_name[0].lower()}.{last_name.lower()}.com')
    email_gen('Gerardo', 'Delao', 'Spotify')
    email_gen('Erin', 'Cranston', 'Facebook')

#username Generator

def contact_card(first_name, last_name):
    print(f'{first_name[0:3].lower()}_{last_name[0:5].lower()}')
    contact_card('Gerardo', 'Delao')

#New User Contact Information

def new_user(first_name, last_name, domain):
    print(f"Welcome to E Corp, {first_name} {last_name}")
    print("Email: ")
    email_gen("Gerardo", "Delao", "domain")
    print("Username: ")
    contact_card("Gerardo", "Delao")
new_user('Gerardo', 'Delao', 'spotify')


  


