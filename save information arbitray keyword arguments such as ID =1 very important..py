#When we use double asterks to a function such
#as save_user(id.=1, name="John", age=22) we can pass several
#arguments to our dictionary.

def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)

def save_arguments(**arguments):
    print(arguments)
save_arguments(Id=2, api_names="Websites", Economics="Global", Data="Where does company do business at")




