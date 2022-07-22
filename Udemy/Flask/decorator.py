import time
# current_time = time.time()
# print(current_time)

# def speed_calc_decorator(function):
#     def wrapper_function():
#         start_time= time.time()
#         function()
#         end_time= time.time()
#         print(f"{function.__name__}: run speed: {end_time- start_time}s")
#     return wrapper_function

# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i

# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i

# fast_function()
# slow_function()

#Python Decorator Function

# def decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function

# @decorator
# def say_hello():
#     print("Hello")

# say_hello()

# def say_bye():
#     print("Bye")

# say_bye()

#Advanced Python decorator function

class User:
    def __init__(self, name):
        self.name= name
        self.is_logged= False


    
def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged:
            function(args[0])
        else:
            raise Exception("The User is not authenticated.")

    return wrapper
        
    
def login(user):
    user.is_logged= True
    print(f'{user.name} is Logged')
    
@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s news blog post.")
    

new_user= User("Kamram")
login(new_user)
create_blog_post(new_user)