# here are 100 doors, all closed. In a nearby cage are 100 monkeys. The first monkey is let out and runs along the doors opening every one. 
#The second monkey is then let out and runs along the doors closing the 2nd, 4th, 6th,… - all the even-numbered doors. The third monkey is let out. 
#He attends only to the 3rd, 6th, 9th,… doors (every third door, in other words), closing any that is open and opening any that is closed, and so on. 
#After all 100 monkeys have done their work in this way, what state are the doors in after the last pass?

#Answer with the number of open doors.

def EvenOdd(A):
    c = 0
    
    for i in range(1,A+1):
        if i&1 != 1:
            print(i, end = ' ')
            c += 1
    
    return c


A = 100
print(EvenOdd(A))
            
