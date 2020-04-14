import random
import os
os.chdir("workout")
from wo_list import wo_list
from wo_weight import wo_weight
from wo_list import run_list


def wo_picker():
    random.randrange(1,100)
    return random.choices(
        wo_list,
        weights=wo_weight,
        k=random.randrange(8,12)
    )

print("number of workouts today - ", len(wo_picker()))
print(wo_picker())

# print(wo_list)
# print(wo_weight)

#where are we?
# path = os.listdir()
# print(path)