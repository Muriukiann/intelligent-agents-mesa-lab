# run.py
# Mesa Agent-Based Modeling - Lab Work Week 7-8
# Reference: https://mesa.readthedocs.io/ and https://github.com/projectmesa/mesa
#
# This file runs the simulation.
# It creates the model and steps through it a number of times.

from model import MoneyModel  # Import our model from model.py


# ---- Simulation Settings ----
NUM_AGENTS = 5   # Number of agents in the simulation
NUM_STEPS = 3    # Number of steps/rounds to run


# ---- Run the Simulation ----
print("=" * 40)
print("   MONEY MODEL SIMULATION STARTING")
print("=" * 40)

# Create the model with 5 agents
model = MoneyModel(NUM_AGENTS)

# Run the simulation for a number of steps
for step in range(NUM_STEPS):
    print(f"\n====== STEP {step + 1} ======")
    model.step()

# ---- Show Final Results ----
print("\n" + "=" * 40)
print("   FINAL WEALTH OF EACH AGENT")
print("=" * 40)
for agent in model.agents:
    print(f"Agent {agent.unique_id} final wealth: {agent.wealth}")

print("\nSimulation complete!")
