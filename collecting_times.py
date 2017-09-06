import time
times = []
how_many_athletes,place = 0,0
while True:
    place +=1
    how_many_athletes = (input("Athlete Count  ---> "))
    try:
        how_many_athletes = int(how_many_athletes)
    except ValueError:
        if how_many_athletes == "save":
            break
        how_many_athletes = int(1)
    if place == 1:
        wtime = time.time() ## this is the winner time, all is relative
    #if how_many_athletes == "":
    #    how_many_athletes = int(1)
    atime = [time.time() - wtime]
    times.append(atime*how_many_athletes)

print(times)
