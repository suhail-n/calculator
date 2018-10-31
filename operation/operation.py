from helper.helper import maybe, repeat

OPERATORS = ('*', '/', '+', '-')

is_num = lambda n: isinstance(n, int)
get_number = lambda: int(input('Enter an integer: '))
get_safe_number = repeat(maybe(get_number), is_num)

is_operator = lambda O: O in OPERATORS
get_operator = lambda: str(input('Enter an operator (+, -, /, *): '))
get_safe_operator = repeat(maybe(get_operator), is_operator)


calculate = lambda num1, o, num2: \
    num1 + num2 if o == '+' \
    else num1 - num2 if o == '-' \
    else num1 * num2 if o == '*' \
    else num1 / num2 if o == '/' \
    else None