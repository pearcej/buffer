"""
Writing outside the bounds of a block of allocated memory can corrupt data, crash the program,
or cause the execution of malicious code. C++ is particularly vulnerable to buffer overflows.

modified from http://cis1.towson.edu/~cssecinj/modules/cs0/buffer-overflow-cs0-c/
"""

buffer=[0]*5 # allocates array with 5 0s in it
importantData = 100
print("importantData before buffer overfow: " + str(importantData))
for i in range(0, 6): # Note: Change the 6 to 5 to see this run
    buffer[i]=7
    print(i, end=' ')
print("")
print("importantData after buffer overfow: " + str(importantData))

