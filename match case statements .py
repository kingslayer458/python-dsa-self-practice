#match-case statement (switch): an alternative to using many 'elif' statements
# execute some code if a value matches a 'case'
#benefits: cleaner and syntax is more readable

#def day_of_week(day):
    #if day ==1:
       #return "Monday"
    #elif day == 2:
        #return "Tuesday"
    #elif day == 3:
        #return "Wednesday"
    #elif day == 4:
        #return "Thursday"
    #elif day == 5:
        #return "Friday"
    #elif day == 6:
        #return "Saturday"
    #elif day == 7:
        #return "Sunday"
    #else:
        #return "Invalid day"

#print(day_of_week(1))   


#switch case

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "tuesday"
        case 3:
            return "wednesday"
        case 4:
            return "thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
    
        case _:
            return "Invalid day"

print(day_of_week(1))
print(day_of_week(3))      


def is_weekend(day):
    match day:
        case "sat"|"sun":
            return True
        case "mon"|"tue"|"wed"|"thurs"|"fri":
            return False
        case _:
            return False
        
print(is_weekend("sat"))       
