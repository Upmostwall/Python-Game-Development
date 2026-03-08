set1_input = input("Enter elements for set 1 (comma-separated): ")
set1 = set(x.strip() for x in set1_input.split(",") if x.strip())

set2_input = input("Enter elements for set 2 (comma-separated): ")
set2 = set(x.strip() for x in set2_input.split(",") if x.strip())

print("\nSet 1:", set1)
print("Set 2:", set2)

print("\nSet Operations:")
print("1. Union (|)")
print("2. Intersection (&)")
print("3. Difference (-)")
print("4. Symmetric Difference (^)")

choice = input("\nChoose an operation (1-4): ")

if choice == "1":
    result = set1 | set2
    print("\nUnion: {}".format(result))
elif choice == "2":
    result = set1 & set2
    print("\nIntersection: {}".format(result))
elif choice == "3":                         
    result = set1 - set2
    print("\nDifference (Set 1 - Set 2): {}".format(result))
elif choice == "4":
    result = set1 ^ set2
    print("\nSymmetric Difference: {}".format(result))
else:
    print("Invalid choice!")