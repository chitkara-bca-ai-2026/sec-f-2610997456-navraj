books = [
    ("python programming", "guido van rossum", 1991, "programming"),
    ("artificial intelligence", "stuart russell", 2020, "ai"),
    ("data structures", "mark allen weiss", 2013, "computer science")
]

library_categories = {"programming", "ai", "computer science"}
student_wishlist = {"ai", "cloud", "cybersecurity"}

while True:
    print("\n========== university library ==========")
    print("1. view all books")
    print("2. add a new book")
    print("3. view categories")
    print("4. add category to wishlist")
    print("5. category gap analysis")
    print("6. exit")
    print("========================================")

    choice = input("select an option (1-6): ")

    if choice == "1":
        print("\n---------- available books ----------")

        for i, book in enumerate(books, start=1):
            title, author, year, category = book

            print(f"\nbook {i}")
            print(f"title    : {title}")
            print(f"author   : {author}")
            print(f"year     : {year}")
            print(f"category : {category}")

        print("\n-------------------------------------")
        print("total books:", len(books))

    elif choice == "2":
        print("\n---------- add new book ----------")

        title = input("enter book title: ").strip().lower()
        author = input("enter author name: ").strip().lower()
        year_input = input("enter publication year: ").strip()
        category = input("enter category: ").strip().lower()

        if title and author and year_input and category:
            try:
                year = int(year_input)

                new_book = (title, author, year, category)
                books.append(new_book)
                library_categories.add(category)

                print("\n[success] book added successfully!")

            except ValueError:
                print("[error] year must be a valid number.")
        else:
            print("[error] all fields are required.")

    elif choice == "3":
        print("\n---------- library categories ----------")

        for i, category in enumerate(sorted(library_categories), start=1):
            print(f"{i}. {category}")

        print("----------------------------------------")
        print("total categories:", len(library_categories))

    elif choice == "4":
        print("\n---------- student wishlist ----------")

        requested_category = input(
            "enter requested category: "
        ).strip().lower()

        if requested_category:
            if requested_category in student_wishlist:
                print("[info] category already exists in wishlist.")
            else:
                student_wishlist.add(requested_category)
                print("[success] category added to wishlist!")
        else:
            print("[error] category cannot be empty.")

    elif choice == "5":
        already_in_stock = library_categories & student_wishlist
        purchase_order_needed = student_wishlist - library_categories
        full_combined_coverage = library_categories | student_wishlist

        print("\n========== category gap report ==========")

        print("\n1. categories already in stock:")
        if already_in_stock:
            for category in sorted(already_in_stock):
                print("   -", category)
        else:
            print("   no matching categories found.")

        print("\n2. categories to purchase:")
        if purchase_order_needed:
            for category in sorted(purchase_order_needed):
                print("   -", category)
        else:
            print("   no additional categories required.")

        print("\n3. all combined categories:")
        for category in sorted(full_combined_coverage):
            print("   -", category)

        print("-----------------------------------------")
        print("categories in stock:", len(library_categories))
        print("wishlist categories:", len(student_wishlist))
        print("=========================================")

    elif choice == "6":
        print("\nthank you for using the university library system.")
        print("goodbye!")
        break

    else:
        print("\n[error] invalid choice. please select from 1 to 6.")