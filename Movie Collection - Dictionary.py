#Q10. Movie Collection - Dictionary

movies = {}

while True:
    print("\nOptions:")
    print("1. Add movie")
    print("2. Update rating")
    print("3. Display movies")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter movie name: ")
        rating = float(input("Enter movie rating (out of 10): "))
        movies[name] = rating
    elif choice == "2":
        name = input("Enter movie name: ")
        new_rating = float(input("Enter new rating (out of 10): "))
        if name in movies:
            movies[name] = new_rating
    elif choice == "3":
        for name, rating in movies.items():
            print(f"{name}: {rating}/10")
    elif choice == "4":
        break

