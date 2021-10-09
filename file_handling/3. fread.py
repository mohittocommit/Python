# a file named "dummy1", will be opened with the reading mode.
file = open('dummy1.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)
file.close()
