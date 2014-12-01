#! /usr/bin/env python3

import math

EPSILON = 0.001

def get_amount_penny(msg):
    while True:
        try:
            amount_dollar = float(input(msg))
            if amount_dollar < 0:
                raise ValueError("Amount must be no less than 0!")
            amount_penny = int(amount_dollar * 100)
            if abs(amount_dollar * 100 - amount_penny) > EPSILON:
                raise ValueError("Amount should not have fractional penny!")
            return amount_penny
        except ValueError as err:
            print(err)

def get_rate_percent(msg):
    while True:
        try:
            rate_percent = float(input(msg))
            if rate_percent < 0:
                raise ValueError("Interest rate should not be negative!")
            return rate_percent
        except ValueError as err:
            print(err)


def get_term_year(msg):
    while True:
        try:
            term_year = int(input(msg))
            if term_year < 1:
                raise ValueError("Term should be no less than 1 year!")
            return term_year
        except ValueError as err:
            print(err)

def main():
    print("Loan calculator\n")
    amount_penny = get_amount_penny("Amount borrowed: ")
    interest_rate = get_rate_percent("Interest rate: ")
    term_year = get_term_year("Term (years): ")

    amount_penny += int(interest_rate * amount_penny / 100)
    payment_penny = int(math.ceil(amount_penny / (12 * term_year)))
    payment_penny_last = amount_penny - (12 * term_year - 1) * payment_penny

    #print(str(amount_penny))
    #print(str(payment_penny))
    #print(str(payment_penny_last))

    width_pymt_str = max([5, int(math.log(12 * term_year, 10) + 1)])
    width_paid_num_str = int(math.log(payment_penny + 1, 10)) + 1
    width_paid_str = max([7, width_paid_num_str + 1])
    width_balance_num_str = int(math.log(amount_penny, 10)) + 1
    width_balance_str = max([9, width_balance_num_str + 1])

    pymt_str = ["{num:{fill}{align}{width}}".format(num = m, width = width_pymt_str, fill = ' ', align = '^') for m in range(12 * term_year + 1)]
    
    paid = [payment_penny for m in range(12 * term_year + 1)]
    paid[0] = 0
    paid[-1] = payment_penny_last
    paid_num_str = ["{0:{fill}{align}{width}{precision}}".format(m / 100, fill = ' ', align = '>', width = width_paid_num_str, precision = '.2f') for m in paid]
    print(paid_num_str)
    paid_str = ["${0:{fill}{align}{width}}".format(s, fill = ' ', align = '^', width = width_paid_str) for s in paid_num_str]
    #print(paid_str)

    balance = [amount_penny - m * payment_penny for m in range(12 * term_year + 1)]
    balance[-1] = 0
    #print(balance)
    balance_num_str = ["{0:{fill}{align}{width}{precision}}".format(m / 100, fill = ' ', align = '>', width = width_balance_num_str, precision = '.2f') for m in balance]
    print(balance_num_str)
    balance_str = ["${0:{fill}{align}{width}}".format(s, width = width_balance_str, fill = ' ', align = '^') for s in balance_num_str]
    #print(balance_str)

    print((pymt_str))
    for m in range(12 * term_year + 1):
        print(pymt_str[m] + "      " + paid_str[m] + "      " + balance_str[m])
    

if __name__ == "__main__":
    main()
