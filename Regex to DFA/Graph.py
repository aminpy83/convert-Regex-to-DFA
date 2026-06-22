from NFA import main
from Parser import shunting_stack
from DFA import nfa_to_dfa
from graphviz import Digraph


def nfa_graph(nfa, name):
    dot = Digraph(comment='NFA', graph_attr={'rankdir': 'LR'})

    already_seen = set()
    queue = [nfa.start]

    state_map = {}

    def state_mapper(state):  # hashing state for graphviz
        if state not in state_map:
            state_map[state] = str(len(state_map))  # dot.node/edge takes str name
        return state_map[state]

    dot.node('start', shape='none', label='')  # creating first entry which has no start state
    dot.edge('start', state_mapper(nfa.start))

    state_index = 0
    while queue:
        current = queue.pop(0)
        if current in already_seen:  # for loops
            continue
        already_seen.add(current)

        status = 'doublecircle' if current.is_final else 'circle'
        dot.node(state_mapper(current), shape=status, label=f'q{state_index}')
        state_index += 1
        for char, next_states in current.transitions.items():
            label = char if char else 'ε'
            for i in next_states:
                dot.edge(state_mapper(current), state_mapper(i), label=label)
                if i not in already_seen:  # adding  states
                    queue.append(i)
    try:
        dot.render(name, view=True, format='png', cleanup=True)
        print(f'Graph saved in {name}.png')
    except Exception as e:
        print('error: ', e)


def dfa_graph(dfa, name):
    dot = Digraph(comment='DFA', graph_attr={'rankdir': 'LR'})
    already_seen = set()
    queue = [dfa.start]
    state_map = {}

    def state_mapper(state):
        if state not in state_map:
            state_map[state] = str(len(state_map))
        return state_map[state]

    dot.node('start', shape='none', label='')  # first state
    dot.edge('start', state_mapper(dfa.start))

    state_index = 0
    while queue:
        current = queue.pop(0)
        if current in already_seen:
            continue
        already_seen.add(current)

        status = 'doublecircle' if current.is_final else 'circle'  # determining final state
        dot.node(state_mapper(current), shape=status, label=f'D{state_index}')
        state_index += 1

        for char, next_state in current.transitions.items():
            dot.edge(state_mapper(current), state_mapper(next_state), label=str(char))
            if next_state not in already_seen:
                queue.append(next_state)
    try:
        dot.render(name, view=True, format='png', cleanup=True)
        print(f'DFA Graph saved in {name}.png')
    except Exception as e:
        print('Error rendering DFA: ', e)


# if __name__ == "__main__":
#     regex = "(a|c)*"
#     alphabet = ['a', 'c']
#
#     print(f"Regex: {regex}")
#     print(f"Postfix: {shunting_stack(regex)}")
#
#     # ۱. تولید و رسم NFA
#     nfa_result = main(regex)
#     nfa_graph(nfa_result, 'nfa_output')
#
#     # ۲. تبدیل به DFA و رسم آن
#     dfa_result = nfa_to_dfa(nfa_result, alphabet)
#     dfa_graph(dfa_result, 'dfa_output')
