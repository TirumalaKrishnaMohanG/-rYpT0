# INPUT
input = input("Enter the ciphered :")
x = input.split("-")

# DICTONARY ELEMENTS
List_1 = []
List_2 = []
elements = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
for i in elements:
	List_1.append(i)

count = 0
for i in range(1,27):
	count +=1
	if count >= 1 and count < 10:
		add_C = str('0')+str(count)
		List_2.append(add_C)
	else:
		List_2.append(str(count))

dictonary = dict(zip(List_2,List_1))



# DECODING

Decode_List = []
for i in x:
	for j,k in dictonary.items():
		if i == j:
			Decode_List.append(k)

str1 =''.join(str(e) for e in Decode_List)
print("The Decoded string is :"+str1)
