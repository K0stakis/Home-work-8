import time
def cycle():
    max_attempts = 3
    attempts = 0
    while True:
        user_input = input('Enter your real age: ')
        if user_input.isdigit():
            user_input = int(user_input)
        if 3 <= user_input <= 122:
            break
        else:
            print('Wrong! Enter the NUMBER!')
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Remaining attempts: {remaining_attempts}")
        if attempts == max_attempts:
            print("Exceeded maximum attempts")
            exit()
    return user_input


def get_age_declination(user_input):
    if user_input % 10 == 1 and user_input != 11:
        declination = " рік "
    elif 2 <= user_input % 10 <= 4 and (user_input < 10 or user_input > 20):
        declination = " роки "
    else:
        declination = " років "
    return declination


def generate_message(user_input, declination):
    if '7' in str(user_input):
        return f"Вам {user_input} {declination}, вам пощастить"
    elif user_input < 7:
        return f"Тобі ж {user_input} {declination}! Де твої батьки?"
    elif 6 <= user_input < 16:
        return f"Тобі лише {user_input} {declination}, а це е фільм для дорослих!"
    elif user_input > 65:
        return f"Вам {user_input} {declination}? Покажіть пенсійне посвідчення!"
    else:
        return f"Незважаючи на те, що вам {user_input} {declination}, білетів всеодно нема!"

# 1) Наришіть декоратор, який вимірює час виконання функції



def decorator_time(func):
    def wrapper(*args, **kwargs):
        start_func = time.time()
        res = func(*args, **kwargs)
        finish_func = time.time()
        result = finish_func - start_func
        print(result)
        return res

    return wrapper

