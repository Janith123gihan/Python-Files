marks = 70# marks takes int values from 0 to 100 inclusive
if 75 <= marks <= 100 :
    grade = 'A+'  # here ~ indicates a space character
elif 70 <= marks < 75 :
    grade = 'A'
elif 60 <= marks < 70 :  
    grade = 'B'
elif 50 <= marks < 60 : 
    grade = 'C'
elif 40 <= marks < 50 : 
    grade = 'D+'
elif 35 <= marks < 40 : 
    grade = 'D'
elif 25 <= marks < 35 : 
    grade = 'D-'
else: 
    grade = 'E'
print(marks,grade)

marks = 70 # marks takes int values from 0 to 100 inclusive
if  marks  >=75 :
    grade = 'A+'  # here ~ indicates a space character
elif  marks  >= 70 :
    grade = 'A'
elif  marks >= 60:  
    grade = 'B'
elif 50 <= marks :  
    grade = 'C'
elif 40 <= marks:  
    grade = 'D+'
elif 35 <= marks :  
    grade = 'D'
elif 25 <= marks :  
    grade = 'D-'
else:  
    grade = 'E'
print(marks,grade)

"""output: 70 A
           70 A
  preffered one: I think second one (B) is the better
  one because first one  (A) should check two integer values (ex: elif 70<=marks<75)
  so the second one checks only one integer value so I think second one is the best one"""
