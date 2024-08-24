import random as rd
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
print(rd.choice(friends))

# Option 2
random_idx = rd.randint(0, len(friends))
print(friends[random_idx])