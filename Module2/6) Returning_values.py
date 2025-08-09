#How to return a value in a Function
def area_triangle(base , height):
    return base*height/2
area_a=area_triangle (5,8)
area_b=area_triangle (7,21)
sum = area_a + area_b
print("The area of triangle is :" + str(sum))

#___________________________________________________________________

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
 
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

#___________________________________________________________________

area_a = area_triangle(2, 3)  
area_b = area_triangle(4, 1)  
total = area_a + area_b
print(total)

#___________________________________________________________________

#"The Principle of code reuse"

name = "Kay"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))
name = "Cameron"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

#___________________________________________________________________

def lucky_number(name):
    number = len(name)*3
    print("Hello " + name + ".Your lucky number is " + str(number))

lucky_number ("Abrish")
lucky_number ("Zunaisha")

#___________________________________________________________________

def total_marks(name):
    number = len(name)*4
    print("Hey " + name + ".Your Total marks in English is :" + str(number))
    

total_marks ("Eman")
#___________________________________________________________________

name = "Leo"
number = len(name) * 7
print("Hello " + name + ". Your lucky number is " + str(number))

name = "Isabella"
number = len(name) * 7
print("Hello " + name + ". Your lucky number is " + str(number))

#___________________________________________________________________




