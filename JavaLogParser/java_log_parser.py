#Program:       Java Log Praser and Report Generator
#Author:        James Jenkins

import datetime;

nullpointer_errors = 0;
causedby_errors = 0;
db_errors = 0;
object_no_longer_valid_errors = 0;
invalid_data_errors = 0;
timeout_errors = 0;
general_failure_errors = 0;
severe_errors = 0;
errors = 0;
warnings = 0;

f = open('large_example_console.log', 'r');

print("Searching for Java Errors...\n");

for line in f:
    if str.__contains__(line,"NullPointerException"):
        #print(line)
        nullpointer_errors += 1
    if str.__contains__(line,"Caused by:"):
        #print(line)..
        causedby_errors += 1
    if str.__contains__(line,"jdbc.exceptions"):
        #print(line)
        db_errors += 1
    if str.__contains__(line,"object no longer valid"):
        #print(line)
        object_no_longer_valid_errors += 1
    if str.__contains__(line,"invalid"):
        #print(line)
        invalid_data_errors += 1
    if str.__contains__(line,"SocketTimeoutException"):
        #print(line)
        timeout_errors += 1
    if str.__contains__(line,"fail:"):
        #print(line)
        general_failure_errors += 1
    if str.__contains__(line,"SEVERE:"):
        #print(line)
        severe_errors += 1
    if str.__contains__(line,"ERROR:"):
        #print(line)
        errors += 1
    if str.__contains__(line,"WARN:"):
        #print(line)
        warnings += 1

print('\nTotal Null Pointer Exceptions: ')
print(nullpointer_errors)
print('\nTotal Caused By Errors: ')
print(causedby_errors)
print('\nTotal JDBC Exceptions: ')
print(db_errors)
print('\nTotal Object Errors: ')
print(object_no_longer_valid_errors)
print('\nInvalid Data Errors: ')
print(invalid_data_errors)
print('\nConnection Timeout Errors: ')
print(timeout_errors)
print('\nGeneral Failure Errors: ')
print(timeout_errors)
print('\nTotal SEVERE Exceptions: ')
print(severe_errors)
print('\nTotal ERROR Exceptions: ')
print(errors)
print('\nTotal WARN Exceptions: ')
print(warnings)

f.close();
