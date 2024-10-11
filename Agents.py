from game import Agent 
from game import Directions
from random import choice
from pacman import GameState
import random


class DumbAgent(Agent): 
    def getAction(self, state):  
        print("Location: ", state.getPacmanPosition()) 
        print("Actions available: ", state.getLegalPacmanActions()) 
        if Directions.EAST in state.getLegalPacmanActions(): 
            print("Going East.") 
            return Directions.EAST 
        else: 
            print("Stopping.") 
            return Directions.STOP 
        
class RandomAgent(Agent):
    def getAction(self, state):
        actions = state.getLegalPacmanActions()
        return choice(actions)

class BetterRandomAgent(Agent):
    def getAction(self, state):
        actions = state.getLegalPacmanActions()
        filtered_actions = []

        for action in actions:
            if action != Directions.STOP:
                filtered_actions.append(action)

        if not actions:
            return Directions.STOP

        return random.choice(actions)

class ReflexAgent(Agent):
    def getAction(self, state):
        # Packman location
        print("Packman Location: ", state.getPacmanPosition())
        #ghost location
        print("Ghost Location: ", state.getGhostPositions())
        # direction Packman can move
        legalActions = state.getLegalActions()

        # Remove 'Stop' from the list of legal actions
        if Directions.STOP in legalActions:
            legalActions.remove(Directions.STOP)

        # Check each action to see if it leads to eating a food pellet
        for action in legalActions:
            successorGameState = state.generatePacmanSuccessor(action)
            pacmanPosition = successorGameState.getPacmanPosition()
            foodGrid = successorGameState.getFood()

            # If Pac-Man's new position has food, choose this action
            if foodGrid[pacmanPosition[0]][pacmanPosition[1]]:
                return action

        # If no action leads directly to food, choose randomly from the remaining actions
        return random.choice(legalActions)


