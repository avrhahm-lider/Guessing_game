import random
secret = random.randint(0,500)
count = 0
def user_input():
    try:
        user = int(input("enter your guess: "))
        if 500 < user or user < 0:
            print("The number is not between 500-0.")
            return user_input()
        return user
    except ValueError:
        print("Error: invalid input please enter correct")
        return user_input()


def guess(user_input1,secret1):
    if user_input1 == secret1:
        return [True,"You succeeded!!!"]
    elif user_input1 > secret1:
        return [False, " low"]
    else:
        return [False, " high"]
if __name__ == "__main__":
    while True:
        count += 1
        user_guess =user_input()
        status = guess(user_guess,secret)
        if status[0]:
            print(status[1])
            print(f"guess: {count}" )
            break
        print(status[1])

