from math import sqrt
from time import sleep
from os import system
system('cls')
def find_value_int(prompt):
    try:
        Value=int(input(prompt+"\n"))
        return Value
    except:
        print("\nTry Again. That is not a number.\n")
        return find_value_int(prompt)
def reduce_to_int(value):
    if int(value)==value:
        return(int(value))
    else:
        return(value)
def num_to_string(num):
    if num>=0:
        return("+"+str(num))
    else:
        return(str(num))
print("Circle equations are printed in the format:\n\n"+"-"*15+\
"\n|"+" "*13+"|\n| 2  2"+" "*8+"|\n|\
x +y +ax+by=c|\n|"+" "*13+"|\n"+"-"*15+"\n")
sleep(3)
a=find_value_int("A:")
sleep(1)
b=find_value_int("B:")
sleep(1)
c=find_value_int("C:")
sleep(5)
a_str=num_to_string(a)
b_str=num_to_string(b)
x_val=reduce_to_int(-a/2)
y_val=reduce_to_int(-b/2)
rad=reduce_to_int(sqrt((a**2+b**2)/4+c))
system("cls")
print(" "*11+"2  2\nEquation: x +y %sx%sy=%s"%(a_str,b_str,c))
print("Centre: (%s,%s).\nRadius: %s units."%(x_val,y_val,rad))