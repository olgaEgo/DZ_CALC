
def not_str(fst_inp):
    for i in range(0, len(fst_inp)):
        if not fst_inp[i:i+1].isdigit():
            if not (fst_inp[i:i+1] == '.') or fst_inp[i:i+1] == ',':
                return False
        else:
            return True


def operation(a, oper, b) -> int:
    global res
    if oper in ['+', '-', '*', '/', '=']:
        if oper == '+':
            res = a + b
        elif oper == '-':
            res = a - b
        elif oper == '*':
            res = a * b
        elif oper == '/':
            try:
                res = a / b
            except ZeroDivisionError:
                res = a
                print(f'Делить на "0" нельзя')
        print(res)
    else:
        print(f'Ошибка ввода')

    return res


def result(operat):
    if not operat == '=':
        return operat


def calc_str(inp_str):
    eval(inp_str)


