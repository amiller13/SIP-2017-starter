import random

#array that holds the name of everyone in the class
names = ['Amanda', 'Rishika', 'Avni', 'Anissa', 'Chloe', 'Jennifer',
'Tierra', 'Stefanie', 'Sydney', 'Anna', 'Annabelle', 'Tianna', 'Jessenia', 'Stephanie', 'Christina',
'Ashley', 'Aileen', 'Aneil', 'Aurpita', 'Karina']

#picks the first random name
current = random.choice(names)
#sets the previous name to an empty string
previous = ""
#boolean variable that allows the program to run forever
classtime = True


while(classtime):
    if(input()== "a"):
        #checks to make sure a new name is being picked
        if(current != previous):
            print(current)
            #sets the name printed to the prvious name
            previous = current
            #picks a new name
            current = random.choice(names)
        else:
            #if it picks the same name twice, pick a new name
            current = random.choice(names)
