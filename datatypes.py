age = 67 #integer
height = 3.5 #float
greeting ="hey hey"#string
python_interesting= True #Boolean

#Data Structures - A single variable holding multiple values
cars = ["Toyota","Ford","Mercedes"] #List -ordered and changeable,it allows future changes when need be-it is identified as list cause of the square brackets

fruits = ("Banana","Orange","Mango")# Tuple -ordered but unchangeable,so allows no future changes -idenified as tuple cause of the normal brackets used

countries={"China","France","Germany","Italy"} #set-unordered and unchangeable,so any of the words can come first

 #Dictionary,used to store information in pairs of keys and values>key is the word and value is the meaning,it uses curly brackets


 student={"name":"Rodah","age":67,"height":3.5}
 print(student)
 print(student["name"])

 #Arrays, it is a way of storing multiple values under one variable name

 marks=[70,80,65,90,75]
 print(marks)

 #uderstanding of indexing is very important python starts counting from zero not one

 #append() ,is used to add elements
 numbers=[10,20,30]
 numbers.append(40)
 print(numbers)

 #insert for adding an element to a specific position
 number=[10,20,40]
 numbers.insert(2,30)
 print (numbers)

 #remove() ,removes an element by its value
 #pop(),removes elements using its index
 #len(numbers),counts elements
 #sum ,calculates total
 #numbers.reverse ,reverses the order
 #numbers.sort(),sorts in ascending order



 #Array operations using loops
 marks=[70,85,60,90,75]

 for marks in marks:
     print(marks)









#Array

print(age)
print(height)
print(cars)
print(countries)


x = 90
y =5

print (x + y)
print (x * y)
print (x - y)
print (x / y)
print (x % y) #Modulus - Returns remainder after division

#Comparison operators,used to compare values and return a boolean

num1 =45
num2=20

print (num1< num2)
print (num1 > num2)
print (num1<= num2)
print (num1>= num2)
print (num1 == num2)#equal to
print (num1 != num2)#not equal to

#Assignment Operators -Assign/store values in variables
number = 80
print(number)

#operator precedence - process of determining how it is carried out like do we add first or assign first

number +=2
number -=2
number %=2
number *=2
print(number)

#logical operators- and ,or ,not

print(100==50 and 60< 80)
print(100==50 or 60< 80)
print(not(100==50 and 60< 80))











