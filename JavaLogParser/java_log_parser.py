#Program:       Java Log Praser and Report Generator
#Author:        James Jenkins

import datetime;

nullpointercount = 0;
causedby = 0;
dberror = 0;

f = open('large_example_console.log', 'r');

print("Searching for Java Errors...\n");

for line in f:
    if str.__contains__(line,"NullPointerException"):
        #print(line)
        nullpointercount += 1
    if str.__contains__(line,"Caused by:"):
        #print(line)
        causedby += 1
    if str.__contains__(line,"db.jdbc.exception"):
        #print(line)
        dberror += 1

print('Total Null Pointer Exceptions: ')
print(nullpointercount)
print('Total Caused By Errors: ')
print(causedby)
print('Total JDBC Exceptions: ')
print(dberror)


f.close();
