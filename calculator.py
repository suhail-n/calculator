from operation.operation import calculate, get_safe_number, get_safe_operator
from helper.helper import repeat

def main():
    # conduct operation
    execute = lambda: calculate(
    # get user input number
        get_safe_number(),
    # get user input number
        get_safe_operator(),
    # get user input number
        get_safe_number()
    )
    # print result
    endless = lambda func: False
    main_loop = repeat(lambda: print("The output is %s " %execute()), endless)
    main_loop()

if __name__ == '__main__':
    main()