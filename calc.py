#This is our python program
import Add as a
import subtr as s
import multiply as m
print("MENU")
print("1. ADD")
print("2. Subtract")
print("3. Multiply")

choice=int(input("Make a choice"))

if choice==1:
	a.ADD()
elif choice==2:
	s.subtract()
elif choice==3:
	m.Multiply()



