from typing import Union

per : Union[int , float] = 7.0

grade : Union[str,None] = None

if per >= 80:
    grade = "A+"
elif  per >= 70:
    grade = "A"
elif  per >= 60:
    grade = "B"
elif  per >= 50:
    grade = "C"  
elif  per >= 40:
    grade = "D"   
else:
    grade = "Fail"   
print(f"Dear student  your percentage is{per} now your calculated grade is : \t {grade}")             
