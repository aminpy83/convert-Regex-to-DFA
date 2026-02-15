operators = {
    '*': 3,
    '+': 3,
    '.': 2,  # concat
    '|': 1,  # union
    '(': 0  # least value
}


def show_dots(s: str):
    new = ''
    if not s:
        print('empty string')
        return 0

    for i in range(len(s)-1):
        if s[i] in [')', '*', s[i] if s[i].isalnum() else '+'] and (s[i + 1].isalnum() or s[i + 1] == '('):
            new += s[i] +'.'
        else:
            new += s[i]
    new += s[-1]
    return new


def shunting_stack(r: str):
    r = show_dots(r)
    print(r)
    stack = []
    out = ''
    for i in r:
        if i.isalnum():
            out += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                out += stack.pop()
            stack.pop()      # for '('
        else:
            while stack and operators[i] <= operators[stack[-1]]:
                out += stack.pop()
            stack.append(i)
    while stack:
        out += stack.pop()
    return out

# print(shunting_stack('(a*b)'))