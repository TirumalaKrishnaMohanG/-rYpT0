
# INPUT
input = input("Enter the string :").upper()
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

dictonary = dict(zip(List_1,List_2))
# ENCODING

Fin_List = []
for j in input:
	for k,l in dictonary.items():
		if j == k:
			Fin_List.append(l)

str1 ='-'.join(str(e) for e in Fin_List)
print("The Encoded Format is :"+str1)
