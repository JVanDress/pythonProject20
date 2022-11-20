            #scope with a param same name.
            #local variables in scope have a brief
             #DO NOT USE GLOBAL VARIABLES
message = "a"

def greet(name):
    message = "a"

def send_email(name):
    message = "b"

greet("Josh")
print(message)




