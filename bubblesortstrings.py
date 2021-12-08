def bubbleSort(stringlist):
    stringlist.sort() # sort the list alphabetically first. This will ensure final output is alphabetical
    for i in range(len(stringlist)): # for each value in range matching the length of the list. This acts as primary loop to iterate through the list
        for x in range(0, len(stringlist)-i-1): # for each value between 0 and the length of the list, minus the current iteration, minus 1 to keep within index
            if len(stringlist[x]) > len(stringlist[x + 1]) : # if the length of the string we are checking is GREATER than the length of the NEXT string in the list
                stringlist[x], stringlist[x + 1] = stringlist[x + 1], stringlist[x] # swap those values
    print ("The sorted list is:")
    for i in range(len(stringlist)): # for each value in range matching the length the of the list. This acts as primary loop to iterate through the list
        print ("% s" % stringlist[i]) # print the value in the list at that position that matches the iteration of this loop

# Test code - Output intent: Sorted alphabetically AND by length of string.
stringlist = ["Charles", "Tess", "Matt", "Chelsea", "Lindsay", "Lindsey", "Veronica", "Javier", "Kakashi"]
bubbleSort(stringlist)

# Sample output
# The sorted list is:
# Matt
# Tess
# Javier
# Charles
# Chelsea
# Kakashi
# Lindsay
# Lindsey
# Veronica