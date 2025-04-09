import axelrod as axl

def StartTurnament(players, turns = 200, repetitions = 10):
    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions)
    results = tournament.play()
    results.ranked_names
    return results

def StartMatch(player1, player2, _turns = 200):
    match = axl.Match((player1, player2), turns=_turns)
    match.play()
    return match
    
def ShowPlot(results):
    plot = axl.Plot(results)
    p = plot.boxplot()
    p.show()

C, D = axl.Action.C, axl.Action.D

class Switcher(axl.Player):
    """
        If it was defected in the last 5 rounds 2 times, then it will defect, otherwise it will cooperate.
    """
    name = "Switcher"
    classifier = {
        "memory_depth": 5,
        "stochastic": False,
        "long_run_time": False, 
        "inspects_source": False, 
        "manipulates_source": False,
        "manipulates_state": False, 
    }

    @staticmethod
    def strategy(opponent: axl.Player) -> axl.Action:
        if D in opponent.history[-5:]:
            if opponent.history[-5:].count(D) >= 2:
                return D
        return C
    
class Propability(axl.Player):
    """
        Gethers the propability of the opponent's actions and then decides based on that.
    """
    name = "Propability"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": False,
        "long_run_time": False, 
        "inspects_source": False, 
        "manipulates_source": False,
        "manipulates_state": False, 
    }

    @staticmethod
    def strategy(opponent: axl.Player) -> axl.Action:
        
        myLen = len(opponent.history)
        if myLen == 0:
            return C
        propability = opponent.history[-myLen:].count(D) / myLen
        if propability > 0.5:
            return D
        return C

class TwoBack(axl.Player):
    """
        If the opponent defected id the before previous round, then it will defect, otherwise it will cooperate.
    """
    name = "TwoBack"
    classifier = {
        "memory_depth": 2,
        "stochastic": False,
        "long_run_time": False, 
        "inspects_source": False, 
        "manipulates_source": False,
        "manipulates_state": False, 
    }

    @staticmethod
    def strategy(opponent: axl.Player) -> axl.Action:
        if len(opponent.history) < 2:
            return C
        if opponent.history[-2] == D:
            return D
        return C
    
    
class Comentator(axl.Player):
    """
        It will prints its comments on the game. Comments based on the feels.
    """
    name = "Comentator"
    classifier = {
        "memory_depth": 0,
        "stochastic": False,
        "long_run_time": False, 
        "inspects_source": False, 
        "manipulates_source": False,
        "manipulates_state": False, 
    }

    @staticmethod
    def strategy(opponent: axl.Player) -> axl.Action:
        myLen = len(opponent.history)
        if myLen == 0:
            return C
        if opponent.history[-5:].count(D) == 0:
            print("Nice, nice...")
            return C
        if opponent.history[-3:] == [C, C, C]:
            print("We are on the same page...")
            return C
        if opponent.history[-3:] == [D, D, D]:
            print("You are just a bad person...")
            return D
        if opponent.history[-3:] == [C, C, D]:
            print("You are unpredictable...")
            return D
        if opponent.history[-3:] == [D, D, C]:
            print("You are unpredictable...")
            return D
        if opponent.history[-5:] == [D, D, D, D, D]:
            print("REALLY? Bro, come on...")
            return D
        return C
    
    
    

if __name__ == "__main__":
        
    players = [axl.Cooperator(), axl.Defector(), axl.Grudger()]
    players.append(axl.Random())
    players.append(axl.TitFor2Tats())
    players.append(axl.Alternator())
    players.append(axl.OmegaTFT())
    players.append(axl.MathConstantHunter())
    players.append(axl.SpitefulTitForTat())
    players.append(Switcher())
    players.append(Propability())
    players.append(TwoBack())
    #players.append(Comentator())
    
    
    results = StartTurnament(players)
    ShowPlot(results)
    
    #match = StartMatch(axl.Random(), Comentator(), 6)
    #print(match.final_score() )
    
    
    input("Press Enter to exit...")