class DFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class State:  # making transitions and creating states
    def __init__(self, is_final=False):
        self.is_final = is_final  # determining final state
        self.transitions = {}

    def add_transition(self, name, state):
        self.transitions[name] = state


# اپسیلون گذر
def epsilon_closure(states):
    closure = set()
    stack = list()

    for state in states:
        closure.add(state)
        stack.append(state)

    while stack:
        state = stack.pop()
        if None in state.transitions:
            for transition in state.transitions[None]:
                if transition not in closure:
                    closure.add(transition)
                    stack.append(transition)

    return closure


def move(states, symbol):
    result_states = set()

    for state in states:
        if symbol in state.transitions:
            if isinstance(state.transitions[symbol], list):
                result_states.update(state.transitions[symbol])
            else:
                result_states.add(state.transitions[symbol])

    return result_states


def nfa_to_dfa(nfa, alphabet):
    start_closure = epsilon_closure({nfa.start})
    unmarked_states = [start_closure]

    # final states
    is_start_final = any(s.is_final for s in start_closure)
    start_state_dfa = State(is_final=is_start_final)

    dfa_states = {frozenset(start_closure): start_state_dfa}

    while unmarked_states:
        state = unmarked_states.pop()
        for character in alphabet:
            move_result = move(state, character)
            next_closure = epsilon_closure(move_result)

            if not next_closure:
                continue

            next_closure_frozen = frozenset(next_closure)

            if next_closure_frozen not in dfa_states:
                is_next_final = any(s.is_final for s in next_closure)
                dfa_states[next_closure_frozen] = State(is_final=is_next_final)
                unmarked_states.append(next_closure)

            dfa_states[frozenset(state)].add_transition(character, dfa_states[next_closure_frozen])
    final_states_dfa = [dfa_state for dfa_state in dfa_states.values() if dfa_state.is_final]

    return DFA(start=start_state_dfa, end=final_states_dfa)
