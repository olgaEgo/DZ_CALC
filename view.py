def result_data(data):
    print(f'Результат вычислений: {data}')


def first_input() -> str:
    fst_inp = input('Первый ввод: ')
    return fst_inp


def input_num() -> float:
    num = float(input('Введите следующее число: '))
    return num


def input_oper():
    oper = input('Введите операцию (+, -, *, /, =): ')
    return oper
