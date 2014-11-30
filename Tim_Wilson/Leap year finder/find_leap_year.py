#! /usr/bin/env python3

def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            if x < 0:
                raise ValueError("Input should be greater than 0!")
            return x
        except ValueError as err:
            print("err") 

def is_leap(x):
    if x % 4 == 0 and x % 100 != 0:
        return True
    else:
        return False

def main():
    while True:
        x = get_int("What year: ")
        if is_leap(x):
            print("{0} is a leap year.\n".format(x))
        else:
            print("{0} is not a leap year.\n".format(x))

if __name__ == "__main__":
    main()
