"""

############  variable ############

# variable : name that refer to the value.
# variablw = variable name + variable value.
# you can decleare any value. 
# there are conditionse to decleare the variables.


### variable name conditions ###


1- can contain both letter and numbers.
2- have to begin with latters or underscore (can not begin with numbers or any other special characters).
3- can use uppercase latters.
4- python are case sensitive.
5- can not use reserved words like (fun , print , if , else , return, ...).





### assigning values to variables ###

1- single assignment:

examples:
__________________________________________________
x = 5
s = 'welcome' 
__________________________________________________

2-multi assignment:

examples:
___________________________________________________
x,y = 3,4         #  x = 3 , y = 4

a = b = c = 1     #  all = 1

___________________________________________________


### variable types ###

1- int             # x = 5
2- string          # s = 'Mohammed'
3- float           # f = 0.5
4- bool            # True , Fales

5- list            # [5,3,4,...]
6- dictionary      # {key1:value1, key2:value2,...}
7- tuples          # (3,4,6,9,7,...)
note: will explain number 5,6 and  in detailes later.





### type() method ### 

you can use type() method to know the type of variables.

example:
________________________________
x = 5
y = 'hello'

print(type(x), type(y))


output:
<class:'int'>
<class:'string'>
________________________________


notes:
you can use semicolon ";" to end the line
example:
_________________________________

x=5 ; y=6

_________________________________



"""