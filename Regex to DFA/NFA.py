from parser import shunting_stack


class NFA:  # just has start and final states
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


def main(string):
    stack = []
    s = shunting_stack(string)
    for i in s:
        if i.isalpha():
            stack.append(creator(i))
        elif i == '.':
            right = stack.pop()
            left = stack.pop()

            new = connector(left, right)
            stack.append(new)

    return stack.pop()


infix = "ab"
nfa_final = main(infix)
print(f"NFA constructed from {infix}")
print(f"Start State: {nfa_final.start}")
print(f"Final State: {nfa_final.final}")
