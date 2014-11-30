#!/usr/bin/env python3
def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            return x
        except ValueError as err:
            print(err)
    
def convert_temperature(t, flag_F):
    if flag_F:
        return 9 / 5 * t + 32
    else:
        return 5 / 9 * (t - 32)

def main():
    print("Temperature converter\n")
    
    t = get_int("Enter a temperature: ")
        
    char_flag_F = None
    while char_flag_F not in {'f', 'F', 'c', 'C'}:
        char_flag_F = input("Convert to (F)ahrenheit or (C)elsius? ")
    flag_F = True if char_flag_F.lower() == 'f' else False

    t_converted = convert_temperature(t, flag_F)

    if flag_F:
        print("\n{0} C = {1} F".format(t, t_converted))
    else:
        print("\n{0} F = {1} C".format(t, t_converted))

if __name__ == "__main__":
    main()
