Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Name: Anant Robinson
Group Member: Alex Sanders
# Evergreen Login: robana07
                     sanale04@evergreen.edu
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3 (Creating Dictionaries)
### Create a dictionary associated with these awesome bands and their legendary lead singers. Freddy Mercury and Queen, Kurt Cobain and Nirvana, Mark Knopfler and Dire Straits. By the end, it should look like this:
Lead Singers = {'Freddy Mercury' : 'Queen', 'Kurt Cobain' : 'Nirvana', 'Mark Knopfler' : 'Dire Straits'}


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

Lead_Singers = {}
Lead_Singers['Freddy Mercury'] = 'Queen'
Lead_Singers['Kurt Cobain'] = 'Nirvana'
Lead_Singers['Mark Knopfler'] = 'Dire Straits'
print Lead_Singers


###
### Problem 4 (Assertions)
### Let's set these legendary singers to equal to 1. Now let's add Justin Bieber and have him equal to 0. Assert a statement that returns a value that is less than 1 that will say "Not a legendary singer, but a whiny little bitch" Print out each of the singers and the statement should either be that, or "Bloody amazing, have my babies?"

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

Lead_Singers['Freddy Mercury'] = 1
Lead_Singers['Kurt Cobain'] = 1
Lead_Singers['Mark Knopfler'] = 1
Lead_Singers['Justin Bieber'] = 0

if Lead_Singer[] < 1:
        print "blah blah blah.  This artist isn't as good as you belive."
else:
        print "Bieber is the best!"

###Not an assertion, because assertions don't work like that.

###
### Problem 5
### Write a code that will put the list of problem 3 in Alphabetical order using if, elif and else. 


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

print "I'm not sure if that's possible"

###
### Problem 6
### Write Python code creating one of each type of data structure, using the correct kind of grouping symbol (square brackets, curly braces, parentheses, and curly braces with colons inside). 

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

print "I am confused but okay"
Dictionary = {}
Dictionary['Tuple key'] = (2, 3)
Dictionary['List key'] = ('Value', 'Another value', 'You get it')
Dictionary['Dict inside dict'] = {"Dingus" : 3 , "Dongus" : 9 , "Dungus" : 18}
print Dictionary

###
### Problem 7
###Now let's add more bands and singers and include them in the dictionary. Billie Joe Armstrong and Greenday, Matthew Bellamy and Muse, Jimi Hendrix and Band of Gypsys, John Lennon and The Beattles. Come up with a way to find out if the singers are currently alive and at the end, print out alive and dead. So it should be:
Print Alive
Print Dead

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

more_dudes = {"Billie Joe Armstrong" : "a" , "Matthew Bellamy" : "d" , "Jimi Hendrix" : "d" , "John Lennon" : "d"}

def mortality(x):
        if more_dudes[x] == "a":
                print "Alive"
        else:
                print "Dead"


###
### Collaboration
###
