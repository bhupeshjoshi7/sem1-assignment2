Length_1 = input("enter any Length here")
Length_2 = input("enter any Length here")
Length_3 = input("enter any Length here")

Length_1 =int(Length_1)
Length_2 =int(Length_2)
Length_3 =int(Length_3)

if 'Length_1 + Length_2 > Length_3' and 'Length_2 + Length_3 > Length_1' and 'Length_1 + Length_3 > Length_2' :
    print("Yes")
else :
    print("No")