class NFA:          # just has start and final states
    def __init__(self, start, final):
        self.start = start
        self.final = final

class State:        # making transitions and creating states
    def __init__(self, is_final=False):
        self.is_final = is_final    # determining final state
        self.transitions = {}

    def add_transition(self, name, state):
        if name not in self.transitions:
            self.transitions[name] = []
        self.transitions[name].append(state)

def creator(s):       # basic nfa with 2 states
    start_state = State()
    final_state = State(is_final=True)
    start_state.add_transition(s, final_state)
    return NFA(start_state, final_state)

def connector(q1, q2):
    q1.final.is_final = False
    q1.final.add_transition(None, q2.start)
    return NFA (q1.start, q2.final)