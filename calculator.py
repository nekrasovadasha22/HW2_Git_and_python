def main(expression: str):
    expression_array = expression.split(' ')
    array_of_operands = []

    try:
        left_int = int(expression_array[0])
        array_of_operands.append(left_int)
    except:
       left_float = float(expression_array[0])
       array_of_operands.append(left_float)


    try:
        right_int = int(expression_array[2])
        array_of_operands.append(right_int)
    except:
       left_float = float(expression_array[2])
       array_of_operands.append(left_float)

    answer = None

    if expression_array[1] == '+':
        # answer = add(array_of_operands)
        pass
    elif expression_array[1] == '-':
        # answer = substruct(array_of_operands)
        pass
    elif expression_array[1] == '*':
        # answer = multiple(array_of_operands)
        pass
    elif expression_array[1] == '/':
        answer = divide(array_of_operands)

    print(answer)


def add(arr_of_operands: list):
    pass


def substruct(arr_of_operands: list):
    pass


def multiple(arr_of_operands: list):
    pass


def divide(arr_of_operands: list):
    if expression_array[2] != 0:
        ans = expression_array[0]/expression_array[2]
            return ans
    else:
        return print ('Деление на 0')




current_expression = input()
main(current_expression)

