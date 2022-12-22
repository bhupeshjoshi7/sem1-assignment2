
input = "Python is a case sensitive language"

print("Length of the input string is",len(input))

Reverse_order = input[35::-1]
print( "the reverse order is'", Reverse_order ,"'")

phrase = input[10:27]
print('''the sliced string is "''', phrase,'''"''')

New_input = input.replace("a case sensitive","object oriented")
print('''Updated string is "''',New_input,'''"''')

index_of_a = input.find("a")
print("The index of 'a' is",index_of_a)

updated_input = input.replace(" ","")
print("The new string is :",updated_input,"'")