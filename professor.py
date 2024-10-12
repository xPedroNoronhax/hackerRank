import random

def get_level():
    while True:
        try:
            n = int(input("Level: "))  
            if n >= 1 and n <= 3:  
                return n  
        except ValueError:
            pass  


def generate_integer(level):
    if level == 1:
        return random.randint(1,9)
    elif level == 2:
        return random.randint(10,99)
    else :
        return random.randint(100,999)


def main():
    level = get_level()
    correct_answers = 0
    question = 1
    while question <= 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answers = x + y
        trying = 1
        while trying <= 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answers:
                    correct_answers += 1
                    break
                else:
                    print("EEE")
                    trying += 1
                    if trying > 3:
                        print(f"{x} + {y} = {answers}")
                        break
            except ValueError:
                print("EEE")
                trying +=1
                pass
        question += 1
    print(f"Score: {correct_answers}/10")


if __name__ == "__main__":
    main()