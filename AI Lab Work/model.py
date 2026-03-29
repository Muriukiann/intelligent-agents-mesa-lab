# model.py
# Mesa Agent-Based Modeling - Lab Work Week 7-8
# Reference: https://mesa.readthedocs.io/ and https://github.com/projectmesa/mesa
#
# This file defines the MoneyModel class.
# The model creates agents and runs the simulation.

import mesa
from agent import MoneyAgent  # Import our agent from agent.py


class MoneyModel(mesa.Model):
    """
    A simple model that simulates wealth exchange between agents.

    The model:
    - Creates a number of MoneyAgents
    - At every step, each agent gives $1 to a random other agent
    """

    def __init__(self, num_agents):
        """
        Called when the model is created.

        Parameters:
        -----------
        num_agents : int
            The number of agents to create in the simulation.
        """
        super().__init__()  # Initialize the base Mesa Model
        self.num_agents = num_agents

        # Create the agents and add them to the model
        for i in range(self.num_agents):
            agent = MoneyAgent(self)  # Create a new agent
            print(f"Agent {agent.unique_id} created with wealth: {agent.wealth}")

    def step(self):
        """
        Called at every step/tick of the simulation.
        Tells all agents to perform their step() action.
        """
        print("\n--- New Step ---")
        self.agents.shuffle_do("step")  # Randomly shuffle and activate all agents
