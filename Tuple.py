#Packing
address = ("211", "Woolaston Avenue", "Ontario", 'Canada', '5673456' )
for x in address:
    print(x, end=' ')

#Unpacking
house_num, apartmentName, city, country, pincode = address
print("\nHouse Number:", house_num)
print("Apartment Name:", apartmentName)
print("State:", city)
print("Country:", country)
print("Pincode:", pincode)

#Tuple Without Brackets
canadianSymbol  = "Red", "White", "Maple Leaf"
print(canadianSymbol)

#Nested Tuple
sample = ("white", [4, 3, 7], [1, 6, 3])
print(sample[2][1])
print(sample[1][2])

#Slicing
program = ('C','A','N','A','D','A')
print(program[0:6])
print(program[:])
print(program[:])

#Reassigning Tuple
program = ('M','A','P','L','E',' ','L','E','A','F')
print(program)

#Change Tuple Values
program = (4, 2, 3, [6,7])