# Name: Anant Robinson
# Evergreen Login: robana07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###
ages = {'Nicholas' : '28' , 'Mary' : '21' , 'Ulises' : '14'}

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"
print ages

# ... write your code and comments here (and remove this line)


###
### Problem 4
###
def date_of_birth(age):
    dob = 2013 - age
    print "She was born in " + str(dob) + "."
    
#What would you put in this line to call the function date_of_birth to find out
#Mary's birth year?



# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

age = 21
# ... write your code and comments here (and remove this line)
date_of_birth(ages['Mary'])

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

# It allows you to check a valid input. It can sort out values you don't want.

def AreYouABro(names):
    assert (names >= 1), "Not a Bro"
    return (names == 1), "Bro"


Nicholas = 1
Paul = 
Kim_Kardashian = 0
print AreYouABro(Nicholas)


###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

mygroupage = {'Anant' : '20', "Alex": '21'}

###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

# ... write your code and comments here (and remove this line)

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").