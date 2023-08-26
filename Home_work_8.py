from lib import cycle, get_age_declination, generate_message, decorator_time

@decorator_time
def cinema_cashier():
    user_input = cycle()
    declination = get_age_declination(user_input)
    message = generate_message(user_input, declination)
    print(message)
    return message

cinema_cashier()