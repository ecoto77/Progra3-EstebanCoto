# -*- coding: cp1252 -*-
#total= item_one+\item_two+\item_three

days=['Monday','Tuesday','Wednesday','Thursday','friday']

word='word'
sentence = "This is a sentence."
paragraph=""" This is a paragraph. it is made up of multiple lines and sentences."""

print days, word, sentence, paragraph


counter=100 # integer
miles=1000.0 # float
name ='John'
a,b,c=1,2,"John"

str='Hello World'

print str
print str[0]
print str[2:5]
print str[2:]
print str*2

list = ['abcd',786,2.23,'john',70.2]
tinylist=[123,'john']

print list   #complete list
print list[0]   # first element of the list
print list[1:3]  # elememts from 2nd to 4th
print list[2:]
print tinylist*2  #prints tiny list twice
print list + tinylist   # concatenated lists

tuple=('abcd', 787, 3.67, ' Esteban', 77.0)
tinytuple=(123, 'Camila')

print tuple    # complete tuple
print tuple[0]   # first element of tuple
print tuple[1:3]   # elements starting from 2nd to 3rd
print tuple[2:]    # starting from 3rd element
print tinytuple*3 # prints tinytuple x3
print tuple+tinytuple  # both tuples

dict={}
dict['one']= " This is one "
dict[2] = " This is two "
tinydict = {'name': 'Camila','code':6475,'dept':'sales'}

print dict['one']   # value for'one' key
print dict[2]       # value for 2 key
print tinydict      # prints complete dictionary
print tinydict.keys()  # prints all the keys
print tinydict.values()   #Prints all the values

#     Data Conversion - Casting

#  int(value)    Value="35"
# str(value)     Value=27
# float(value)   Value="89"
# list(value)    Value"Andres"
# tuple(value)   Value=[1,2,5,6]
# dict(value)    Value="[(1,3),("A",5)]"

a=10
b=20

print a+b , a-b, a*b, b/a, b%a, a**b
print 9//2, 9.0//2.0, -11//3, -11.0//3

#(a ==b) is not true
#(a!=b) is true
#(a<>b) is true. This is similar to !=operator.
#(a>b)is not true
#(a<b)is true
#(a>=b)is not true
#(a<=b) is true

c=a+b
#Assigment Operators
# c+=a is equivalent to c=c+a
#c -= a is equivalent to c = c – a
#c *= a is equivalent to c = c * a
#c /= a is equivalent to c = c / a
#c %= a is equivalent to c = c % a
#c **= a is equivalent to c = c ** a
#c //= a is equivalent to c = c // a
#a++ = Error

#  Decision Making :
var=100
if var <200:
   print " La expresion es menor a 200"
   if var ==150:
    print" Which is 150"
elif var ==100:
   print " Which is 100"
elif var ==50:
   print " Which is 50 "
elif var <50:
   print " El valor de la expresion es menor de 50 "

else: 
   print " No se pudo encontrar una expresion verdadera "

if (var==100) : print " El valor de la expresion es 100"

print " While Loop "

count=0
while count<5:
    print count, " es menos de 5 "
    count = count +1
else:
     print count, " no es menos de 5 "
     


