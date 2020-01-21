"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

f = open('src/foo.txt', 'r')
# print (str(f))
for line in f:
    print(line)

f.close()   
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open('src/bar.txt', 'w')
f.write('This is a test\n')
f.write('This is a new file I am wriiting on\n')
f.write('This am writting three lines on it\n')
f.close()