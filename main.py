import random
import os
os.chdir("/home/wes/git/workout")
from wo_list import wo_list
#from wo_weight import wo_weight
from wo_list import run_list
from wo_list import wo_weight
from datetime import date

def wo_picker():
    wos = random.choices(
        wo_list,
        weights=wo_weight,
        k=(20)
    )
    if random.randrange(1,100) > 90:
        wos.append(random.choice(run_list))
    return wos

#make file with workout
with open('WOD.txt', 'w') as filehandle:
    filehandle.write(str(date.today()))
    filehandle.write('\n')
    filehandle.write("Number of workouts today - ")
    filehandle.write(str(len(wo_picker())))
    filehandle.write('\n')
    filehandle.write('#############################################\n')
    for item in wo_picker():
        filehandle.write('%s\n' % item)
        filehandle.write('\n')

print("number of workouts today - ", len(wo_picker()))
print(wo_picker())

