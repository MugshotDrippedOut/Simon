import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class FiniteStateMachine:
    def __init__(self, states, alphabet, transition_table, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def process_input(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  # Invalid symbol encountered
            current_state = self.transition_table[current_state].get(symbol, None)
            if current_state is None:
                return False  # No transition for the symbol
        return current_state in self.accepting_states

# Example 1: Odd number of 1s
states1 = {'S0', 'S1'}
alphabet1 = {'0', '1'}
transition_table1 = {
    'S0': {'0': 'S0', '1': 'S1'},
    'S1': {'0': 'S1', '1': 'S0'},
}
initial_state1 = 'S0'
accepting_states1 = {'S1'}
fsm1 = FiniteStateMachine(states1, alphabet1, transition_table1, initial_state1, accepting_states1)

# Example 2: String starts with 'ab'
states2 = {'A', 'B', 'C'}
alphabet2 = {'a', 'b', 'c'}
transition_table2 = {
    'A': {'a': 'B', 'b': 'C', 'c': 'A'},
    'B': {'a': 'B', 'b': 'B', 'c': 'A'},
    'C': {'a': 'B', 'b': 'C', 'c': 'C'},
}
initial_state2 = 'A'
accepting_states2 = {'B'}
fsm2 = FiniteStateMachine(states2, alphabet2, transition_table2, initial_state2, accepting_states2)

# Example 3: Recognize 'ababab'
states3 = {'S', 'A', 'B'}
alphabet3 = {'a', 'b'}
transition_table3 = {
    'S': {'a': 'A', 'b': 'S'},
    'A': {'a': 'S', 'b': 'B'},
    'B': {'a': 'A', 'b': 'S'},
}
initial_state3 = 'S'
accepting_states3 = {'S'}
fsm3 = FiniteStateMachine(states3, alphabet3, transition_table3, initial_state3, accepting_states3)

# Test the FSMs
input_strings = ["11011", "ababab", "abc"]
fsms = [fsm1, fsm2, fsm3]
for i, fsm in enumerate(fsms):
    input_string = input_strings[i]
    if fsm.process_input(input_string):
        print(f"FSM {i + 1}: The input '{input_string}' is accepted.")
    else:
        print(f"FSM {i + 1}: The input '{input_string}' is not accepted.")

# Bonus: Types of finite state machines
# Types of FSAs include deterministic finite automata (DFA), nondeterministic finite automata (NFA), Mealy machines, and Moore machines. DFAs have a single unique transition for each symbol, while NFAs can have multiple transitions. 
# Mealy machines produce output based on both the current state and input, whereas Moore machines produce output only based on the current state.


def visualize_fsm(fsm, fsm_name):
    G = nx.DiGraph()
    
    for state in fsm.states:
        G.add_node(state, shape='ellipse')
    
    for state, transitions in fsm.transition_table.items():
        for symbol, next_state in transitions.items():
            G.add_edge(state, next_state, label=symbol)
    
    pos = nx.spring_layout(G)
    edge_labels = {(state1, state2): symbol for state1, state2, symbol in G.edges(data='label')}
    node_labels = {state: state for state in G.nodes}
    
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1000)
    nx.draw_networkx_edges(G, pos, width=1, alpha=0.5)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    
    plt.title(f'Finite State Machine: {fsm_name}')
    plt.axis('off')
    plt.show()

# Visualize FSMs
visualize_fsm(fsm1, 'Example 1: Odd number of 1s')
visualize_fsm(fsm2, 'Example 2: String starts with "ab"')
visualize_fsm(fsm3, 'Example 3: Recognize "ababab"')