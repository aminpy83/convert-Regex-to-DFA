operators = {
    '*': 3,
    '+': 3,
    '.': 2,
    '|': 1,
    '(': 0
}

def shunting_stack(r: str):
    stack = []
    out = []
    for i in r:
        if i.isalpha():
            out.append(i)
        elif stack:
            if operators[i] > operators[stack[-1]]:
                stack.pop()
            stack.append(i)
        else:
            stack.append(i)
