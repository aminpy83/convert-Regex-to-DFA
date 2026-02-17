from Parser import shunting_stack


class NFA:  # machine just has a start and final states
    def __init__(self, start, final):
        self.start = start
        self.final = final


class State:  # making transitions and creating states
    def __init__(self, is_final=False):
        self.is_final = is_final  # determining final state
        self.transitions = {}

    def add_transition(self, name, state):
        if name not in self.transitions:
            self.transitions[name] = []
        self.transitions[name].append(state)


def creator(s):  # basic nfa with 2 states
    start_state = State()
    final_state = State(is_final=True)
    start_state.add_transition(s, final_state)

    return NFA(start_state, final_state)


def connector(q1, q2):  # connect 2 nfa to each other with q1
    q1.final.is_final = False
    q1.final.add_transition(None, q2.start)  # using None for اپسیلون گذر

    return NFA(q1.start, q2.final)


def union(q1, q2):
    q1.final.is_final = False
    q2.final.is_final = False

    new_start = State()
    new_final = State(is_final=True)
    new_start.add_transition(None, q1.start)
    new_start.add_transition(None, q2.start)

    q1.final.add_transition(None, new_final)
    q2.final.add_transition(None, new_final)

    return NFA(new_start, new_final)


def star(q1):
    new_start = State()
    new_final = State(is_final=True)
    q1.final.is_final = False

    new_start.add_transition(None, new_final)  # * ==> 0
    new_start.add_transition(None, q1.start)

    q1.final.add_transition(None, q1.start)
    q1.final.add_transition(None, new_final)

    return NFA(new_start, new_final)


# gathers all parts together
def main(string):
    stack = []
    s = shunting_stack(string)  # converting string to postfix
    for i in s:
        if i.isalnum():
            stack.append(creator(i))

        elif i == '.':
            right = stack.pop()
            left = stack.pop()
            new = connector(left, right)
            stack.append(new)

        elif i == '|':
            right = stack.pop()
            left = stack.pop()
            stack.append(union(left, right))

        elif i == '*':
            loop = stack.pop()
            stack.append(star(loop))

    return stack.pop()
