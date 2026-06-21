class DFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class State:  # making transitions and creating states
    def __init__(self, is_final=False):
        self.is_final = is_final  # determining final state
        self.transitions = {}

    def add_transition(self, name, state):
        if name not in self.transitions:
            self.transitions[name] = state  # every particular input -> particular destination
        self.transitions[name].append(state)


def epsilon_closure(states):
    closure = set()
    stack = list()

    for state in states:
        closure.add(state)
        stack.append(state)

    while stack:
        state = stack.pop()
        if None in state.transitions:
            closure.add(state.transitions[None])