def greet(name, mood):
    if name.lower() =="bayleigh":
        return f"Hey Bayleigh! Im glad you're coding today. 😊"
    elif name.lower() == "kevin":
        return f"Hey Kevin! Back again with that brain power! 😊"
    else:
        if mood.lower() == "tired":
            return f"Hey {name}, I know you're tired, but keep going! You've got this! 💪"
        elif mood.lower() == "happy":
            return f"Nice to meet you, {name}! Keep spreading that joy 🌟"
        else:
            return f"Nice to meet you, {name}. I hope your day gets even better."

if __name__ == "__main__":
    user_name = input("What's your name? ")
    user_mood = input("How are you feeling today? (happy, tired, etc.) ")
    print(greet(user_name, user_mood))