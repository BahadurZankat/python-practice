class A:
    varA="First Base class variable A"

class B:
    varB="Second Base class variable B"


class C(A,B):
    varC="Child class variable C"



c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

#Out Put :-
#Child class variable C
#Second Base class variable B
#First Base class variable A
# Because of Python support multi-ple inheritance class "C" can access the variables from class "A" & "B".