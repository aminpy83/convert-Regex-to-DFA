operators = {
    '*': 3,
    '+': 3,
    '.': 2,  # concat
    '|': 1,  # union
    '(': 0  # least value
}


def shunting_stack(r: str):
    stack = []
    out = ''
    for i in r:
        if i.isalpha():
            out += i
        elif i == ')':
            while stack and stack[-1] != '(':
                out += stack.pop()
            stack.pop()  # pop the '('
        else:
            while stack and operators[i] < operators[stack[-1]]:
                out += stack.pop()
            stack.append(i)
    while stack:
        out += stack.pop()
    return out
