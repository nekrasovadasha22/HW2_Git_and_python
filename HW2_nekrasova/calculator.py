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
       right_float = float(expression_array[2])
       array_of_operands.append(right_float)

    answer = None

    if expression_array[1] == '+':
        answer = add(array_of_operands)

    elif expression_array[1] == '-':
        answer = substruct(array_of_operands)
       
    elif expression_array[1] == '*':
        answer = multiple(array_of_operands)
    elif expression_array[1] == '/':
        answer = divide(array_of_operands)

    print(answer)


def add(arr_of_operands: list):
    return arr_of_operands[0]+arr_of_operands[1]

def substruct(arr_of_operands: list):
    # substruct
    return arr_of_operands[0]-arr_of_operands[1]


def multiple(arr_of_operands: list):
    answer = arr_of_operands[0] * arr_of_operands[1]
    return answer


def divide(arr_of_operands: list):
    if arr_of_operands[1] != 0:
        answer = arr_of_operands[0]/arr_of_operands[1]
        return answer
    else:
        answer = 'Деление на 0!'
    return answer




current_expression = input()
main(current_expression)

