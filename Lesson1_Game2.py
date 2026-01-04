countryDb = {}
while True:
    print("1. Add Country")
    print("2. Display Countries")
    print("3. Display Capitals")
    print("4. Get Capital")
    print("5. Delete Country")
    print("6. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        country = input("Enter country name: ").upper()
        capital = input("Enter capital name: ").upper()
        countryDb[country] = capital
        print("Country and Capital added successfully.")

    elif choice == 2:
        print(list(countryDb.keys()))

    elif choice == 3:
        print(list(countryDb.values()))

    elif choice == 4:
        country = input("Enter country name: ").upper()
        print(countryDb.get(country))

    elif choice == 5:
        country = input("Enter country name: ").upper()
        del countryDb[country]

    elif choice == 6:
        break

    else:
        print("Invalid choice. Please select a valid option (1-6):")