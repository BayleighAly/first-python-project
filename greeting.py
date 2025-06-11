def greet(name):
    if name.lower() == "bayleigh":
        return "Hey! I already know you. 😊"
    else:
        return f"Nice to meet you, {name}!"

if __name__ == "__main__":
    user_name = input("What's your name? ")
    print(greet(user_name))
