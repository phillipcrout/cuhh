placements = []
number,place = 0,0
while number != "save":
    place +=1
    number = input("Athlete place = "+str(place)+" ---> ")
    placements.append(number)
print(placements)
