import networkx as nx
import matplotlib.pyplot as plt

class KonecnyAutomat:
    def __init__(self, states, alphabet, transition_function, initial_state, accepting_states):
        self.states = states 
        self.alphabet = alphabet  
        self.transition_function = transition_function 
        self.current_state = initial_state 
        self.accepting_states = accepting_states  

    def reset(self):
        self.current_state = self.initial_state

    def process_input(self, input_string):
        for symbol in input_string:
            if (self.current_state, symbol) in self.transition_function:
                self.current_state = self.transition_function[(self.current_state, symbol)]
            else:
                return False
        return self.current_state in self.accepting_states

# Automat detekující lichý počet '0':
states = {'q0', 'q1'}
alphabet = {'0', '1'}
transition_function = {
    ('q0', '0'): 'q1', 
    ('q1', '0'): 'q0', 
    ('q0', '1'): 'q0', 
    ('q1', '1'): 'q1'
}
initial_state = 'q0'
accepting_states = {'q1'}

automat1 = KonecnyAutomat(states, alphabet, transition_function, initial_state, accepting_states)

# Automat akceptující slova končící na '01':
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transition_function = {
    ('q0', '0'): 'q1', 
    ('q0', '1'): 'q0', 
    ('q1', '0'): 'q1', 
    ('q1', '1'): 'q2', 
    ('q2', '0'): 'q1', 
    ('q2', '1'): 'q0'
}
initial_state = 'q0'
accepting_states = {'q2'}

automat2 = KonecnyAutomat(states, alphabet, transition_function, initial_state, accepting_states)

# Automat akceptující slova obsahující podřetězec '010':
states = {'q0', 'q1', 'q2', 'q3'}
alphabet = {'0', '1'}
transition_function = {
    ('q0', '0'): 'q1', 
    ('q0', '1'): 'q0', 
    ('q1', '0'): 'q1', 
    ('q1', '1'): 'q2', 
    ('q2', '0'): 'q3', 
    ('q2', '1'): 'q2', 
    ('q3', '0'): 'q3', 
    ('q3', '1'): 'q3'
    }
initial_state = 'q0'
accepting_states = {'q3'}

automat3 = KonecnyAutomat(states, alphabet, transition_function, initial_state, accepting_states)

input_string = "010101"

print("Automat 1:")
print(automat1.process_input(input_string))

print("Automat 2:")
print(automat2.process_input(input_string))

print("Automat 3:")
print(automat3.process_input(input_string))

# Funkce pro vizualizaci konečného automatu
def show_automat(automat, title="Konečný automat"):
    G = nx.DiGraph()

    for state in automat.states:
        G.add_node(state)

    for (from_state, symbol), to_state in automat.transition_function.items():
        G.add_edge(from_state, to_state, label=symbol)

    pos = nx.spring_layout(G, seed=42)  # Rozložení grafu

    edge_labels = nx.get_edge_attributes(G, 'label')

    nx.draw_networkx_nodes(G, pos, node_size=500, node_color="green", alpha=1)
    nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.3", arrowsize=15, width=1.5, edge_color="black")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(title)
    plt.axis('off')
    plt.show()


show_automat(automat1, "Automat detekující lichý počet '0'")

show_automat(automat2, "Automat akceptující slova končící na '01'")

show_automat(automat3, "Automat akceptující slova obsahující podřetězec '010'")