
# INPUT

input = input("Enter the string: ")

# CASE TRANSFORM

print("The Transformed Case for Lowercase is : "+input.lower())
print("The Transformed Case for Uppercase is : "+input.upper())
print("The Transformed Case for Capitalize is : "+input.capitalize())

# Looping for Alterante Case
List = []
Test = len(input)
for i in range(Test):
#	print(i,":",input[i])
	if i%2 == 1:
		Testing_1 = input[i].upper()
		List.append(Testing_1)
	else:
		Testing_1 = input[i].lower()
		List.append(Testing_1)

str1 = ''.join(e for e in List)
print("The Transformed Case for Alternating Case is : "+str1)
print("The Transformed Case for Inverse Case is : "+input.swapcase())
print("The Reverse Case is : "+input[::-1])
