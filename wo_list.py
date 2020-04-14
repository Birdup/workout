import pandas as pd 


#read CSV
colnames = ['Workout', 'WOC']
data = pd.read_csv("Workouts.csv", names=colnames)

#Change them to lists and remove headers
wo_list = data.Workout.tolist()
wo_list.remove("Workout")
wo_weight = data.WOC.tolist()
wo_weight.remove("WOC")

#Converting weights to ints
for i in range(0, len(wo_weight)): 
    wo_weight[i] = int(wo_weight[i])


#print(wo_list[22])
#print(wo_weight[22])
# print(wo_list)

# wo_list = ["20 pushups",
# "15 pushups",
# "25 pushups",
# "25 dips",
# "20 dips",
# "15 dips",
# "150 jump ropes",
# "100 jump ropes",
# "75 jump ropes"
# ]

run_list = [
"103 Riverlake Drive",
"104 Riverlake Drive",
"105 Riverlake Drive",
"106 Riverlake Drive",
"107 Riverlake Drive",
"108 Riverlake Drive",
"117 Riverlake Drive",
"118 Riverlake Drive",
"119 Riverlake Drive",
"121 Riverlake Drive",
"123 Riverlake Drive",
"122 Riverlake Drive",
"125 Riverlake Drive",
"124 Riverlake Drive",
"127 Riverlake Drive",
"129 Riverlake Drive",
"128 Riverlake Drive",
"204 Lake CT",
"206 Lake CT",
"205 Lake CT",
"203 Lake CT",
"201 Lake CT",
"303 Hilltop Ln",
"305 Hilltop Ln",
"306 Hilltop Ln",
"304 Hilltop Ln",
"417 Riverlake Court",
"415 Riverlake Court",
"413 Riverlake Court",
"411 Riverlake Court",
"409 Riverlake Court",
"407 Riverlake Court",
"405 Riverlake Court",
"403 Riverlake Court",
"401 Riverlake Court",
"402 Riverlake Court",
"404 Riverlake Court",
"406 Riverlake Court",
"408 Riverlake Court",
"410 Riverlake Court",
"412 Riverlake Court",
"414 Riverlake Court",
"416 Riverlake Court",
"418 Riverlake Court",
"421 Riverlake Court",
"423 Riverlake Court",
"425 Riverlake Court",
"427 Riverlake Court",
"429 Riverlake Court",
"431 Riverlake Court",
"433 Riverlake Court",
"435 Riverlake Court",
"437 Riverlake Court",
"439 Riverlake Court",
"424 Riverlake Court",
"426 Riverlake Court",
"428 Riverlake Court",
"430 Riverlake Court",
"501 Lakeside Lane",
"503 Lakeside Lane",
"504 Lakeside Lane",
"505 Lakeside Lane",
"506 Lakeside Lane",
"507 Lakeside Lane",
"508 Lakeside Lane",
"509 Lakeside Lane",
"510 Lakeside Lane",
"511 Lakeside Lane",
"512 Lakeside Lane",
"513 Lakeside Lane",
"514 Lakeside Lane",
"515 Lakeside Lane",
"516 Lakeside Lane",
"517 Lakeside Lane",
"518 Lakeside Lane",
"519 Lakeside Lane",
"520 Lakeside Lane",
"521 Lakeside Lane",
"522 Lakeside Lane",
"523 Lakeside Lane",
"524 Lakeside Lane",
"525 Lakeside Lane",
"526 Lakeside Lane",
"528 Lakeside Lane",
"603 River Overlook",
"604 River Overlook",
"605 River Overlook",
"606 River Overlook",
"608 River Overlook",
"703 Oak Valley Lane",
"707 Jett Road",
"708 Jett Road",
"709 Jett Road",
"710 Jett Road",
"711 Jett Road",
"712 Jett Road",
"713 Jett Road",
"714 Jett Road",
"715 Jett Road",
"716 Jett Road",
"718 Jett Road",
"719 Jett Road",
"720 Jett Road",
"721 Jett Road",
"722 Jett Road",
"723 Jett Road",
"724 Jett Road",
"725 Jett Road",
"726 Jett Road",
"727 Jett Road",
"728 Jett Road",
"730 Jett Road",
]
