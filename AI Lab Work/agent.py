# agent.py
# Mesa Agent-Based Modeling - Lab Work Week 7-8
# Reference: https://mesa.readthedocs.io/ and https://github.com/projectmesa/mesa
#
# This file defines the MoneyAgent class.
# Each agent represents a person in a simple economy.
# At every step, an agent gives $1 to a random neighbour if they have money.

import mesa  # Import the Mesa library


class MoneyAgent(mesa.Agent):
    """
    A simple agent that models basic wealth exchange.

    Each agent:
    - Starts with 1 unit of money (wealth)
    - At every step, gives 1 unit to a random other agent (if it has money)
    """

    def __init__(self, model):
        """
        Called when an agent is created.

        Parameters:
        -----------
        model : MoneyModel
            The model instance the agent belongs to.
        """
        super().__init__(model)  # Initialize the base Mesa Agent
        self.wealth = 1          # Every agent starts with 1 unit of money

    def step(self):
        """
        Called at every step/tick of the simulation.

        The agent:
        1. Checks if it has any money
        2. If yes, picks a random other agent
        3. Transfers 1 unit of wealth to that agent
        """
        # If the agent has no money, it does nothing this step
        if self.wealth == 0:
            return

        # Pick a random agent from the model (excluding self)
        other_agents = [a for a in self.model.agents if a is not self]

        if len(other_agents) == 0:
            return  # No one to give money to

        # Randomly select one other agent
        other = self.random.choice(other_agents)

        # Transfer 1 unit of wealth
        other.wealth += 1
        self.wealth -= 1

        # Print what happened (useful for understanding the simulation)
        print(f"Agent {self.unique_id} gave $1 to Agent {other.unique_id}. "
              f"My wealth: {self.wealth}, Their wealth: {other.wealth}")