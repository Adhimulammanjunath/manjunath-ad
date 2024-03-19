'''''''''''
# ! or
# t = 0
# for val in set1,set2:
# C=C+1
# if





# ! Eg:3
def profile(name, age, place):
    print(name, age, place)
profile("sid", 20,"cbe")

        



# n! Eg:3
# def proflie(name, age,piace):
  #  txt="my name is{}. iam {} year old.iam form{}."
    # print(txt.format(name, age, place))
    # profile("sid, 29,"cbe")




# ! Eg:4
# ? function with return statement

# def f1():
# z = 8
# f1()
# print(z) # error --. Cannot use outside the function


def f1(a, b):
    c = a*b
    return c
print(f1(6, 8))
obj =f1(6,8)

def gracemark():
 print(obj=4)
 print(obj+4)
 gracemark()






def f1(a, b):
    c = a*b
    return c
# print(f1(6, 8))
obj = f1(6,8)
obj = f1(4, 6)






def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)




def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)





# 123
# def palindrome(n):
# string = str(n)
# rev = str(n)[::-1]
# if string==rev:
 #  print(n,"palindrome")
  # else:
 #  print("not palindrome")
# a = int(input("Enter the value: "))
# palindrome(a)
 



# * postional args
# Eg:1
#def profile(name,  phone ,mark):
# txt =" my name is {}. my phone number is {}.i got{} marks."
 # print(txt.format(name,phone,mark))
#  profile(txt.format(name, phone,mark))

 # proflie(9878776767,"sidhu",97) #  unexpected output





# todo ---> Exception of keyword args function
# def profile(name, phone, mark):
 # txt ="my name is{]. my phone numder is {}. i got {} marks."
 # print(txt. format(name, phone, mark))

  # profile(name="sid", 123445567, mark=98) # error -> positional arsg follow keyword
  # profile(123445567, name="sid", mark=98, phone=1234556678)

  # * default args
  # ! Eg:1
#  def profile(name,phone, place="kadapa"):
# txt = " my name is {}. my phone number is {}. i am from{]".
# pring(txt.format(name, phone,place))
 # else:
profile("sid",8767676767,"guntur")






    # ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:Problem Statement Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal




# * Keyword args
# ! Eg:1
#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(name="Usman",mark=100,phone=96668686)



# Eg:-1
#? The position of parameter have to be same as position as argument



def profile(name,phone,mark):
    txt= "my name is {}. my phone number is{}.i got {}marks."
    print(txt.format(name,phone,mark))
profile(9177951268,"asif", 98) # unexpected output




# * Keyword args
# ! Eg:-1
# To overcome the disadvantage of position args,we use keywords args
# It is the process of initialising the parameters with the args while calling the
# function


def profile(name,pho):
'''''''''''

# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("Shashank",9876543210)






("You are not eligible to Signup")
file("Shashank",9876543210)
