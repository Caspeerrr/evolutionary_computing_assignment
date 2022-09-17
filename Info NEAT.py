"""
NEAT
Input layers (sensors):
- 16 for projectiles; 8x (x,y)
- 2 for distance player to enemy (x,y)
- 2 for the directions the enemy and player are facing

Output layer (which action to take):
- walk left
- walk right
- jump
- shoot
- release from the jump

Connections to pass values from input layer to output layer, to take the action
Weights depend how strong the connection is (these are changed by the EA)

Mutations:
- weight mutations (easily to occur more often)
- structutal mutations
"""