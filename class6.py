# from typing import Union

# per : Union[int , float] = 88

# grade : Union[str,None] = None

# if per >= 80:
#     grade = "A+"
# elif  per >= 70:
#     grade = "A"
# elif  per >= 60:
#     grade = "B"
# elif  per >= 50:
#     grade = "C"  
# elif  per >= 40:
#     grade = "D"   
# else:
#     grade = "Fail"   
# print(f"Dear student  your percentage is{per} now your calculated grade is : \t {grade}")             

from typing import Union 
PerType = Union[float , int]

percentages : list[PerType] = [88 , 76, 51, 67,92,80,45]

grades: list[str] = []

for per in percentages : 
    grade:str = ""

    if (per >= 0 )and (per < 33):
        grade = "Fail"
    elif  (per >= 33) and (per < 40):
        grade = "E"
    elif  (per >= 40) and (per < 50) :
        grade = "D"
    elif  (per >= 50) and (per < 60):
        grade = "C"  
    elif  (per >= 60 )and (per < 70):
       grade = "B"   
    elif  (per >= 70 )and (per < 80):
       grade = "A"      
    else :
       grade = "A+"   
    grades.append(grade)   
print(percentages)  
print(grades)  
