

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if isinstance(friend_name, str):
        return(f"Hello, {friend_name}!")
    else:
        return("Please enter a string")
