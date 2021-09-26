#####################
### ATBASH CIPHER#######
#####################
#INPUT
input = input()
input = input.upper()

# Dict for Cipher 
test_input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
List_1, List_2 = [],[]
for i in test_input:
	List_1.append(i)
Reverse_List = List_1[::-1]
for j in Reverse_List:
	List_2.append(j)

# ENCODING
dictonary = dict(zip(List_1,List_2))
Fin_list = []
o =""
for p in input:
	for k,l in dictonary.items():
		if p == k:
			o+=l
		elif p =="":
			o+=" "	
Fin_list.append(o)

str1 = ' '.join(str(e) for e in Fin_list)
print("The Encoded string is "+str1)


# DECODING
dictonary_2 = dict(zip(List_2,List_1))
Fin_list_2 = []
o1 = ""
for p1 in str1:
	for k1,l1 in dictonary_2.items():
		if p1 == k1:
			o1+=l1
		elif p1 == "":
			o1+=" "
Fin_list_2.append(o1)

str2 = ' '.join(str(e1) for e1 in Fin_list_2)
print("The Decoded string is "+str2)
