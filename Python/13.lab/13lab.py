store=[]
# Main program loop
while True:
    print("\n====================================")
    print("\n    INVENTORY CONTROL SYSTEM")
    print("\n====================================")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Option 1: View books
    if choice == "1":
        print("\n---  Current Inventory---")
        print("1. Notebook")
        print("2. Pen")
        print("3. Eraser")
        print("4. Ruler")



        print("Select an operation:")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Sort Inventory")
        print("5. Exit")
        
        c=input("enter your choice(1-5):")
        

    # Option 2: Add a new book
    elif choice == "2":
         store.append(input("enter item name to add:"))
         print("[SUCCESS] marker added to inventory")



         

    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")        
    print("5. Exit")
    
    c=input("enter your choice(1-5):")
        






    # # Option 3: View unique categories
    # elif choice == "3":
    #     print("\n--- Unique Library Categories ---")

    #     for category in sorted(library_categories):
    #         print(category)

    #     print("Total genres:", len(library_categories))

    # # Option 4: Add category to wishlist
    # elif choice == "4":
    #     requested_category = input(
    #         "Enter requested category: "
    #     ).strip()

    #     if requested_category:
    #         student_wishlist.add(requested_category)
    #         print("[SUCCESS] Added to wishlist!")
    #     else:
    #         print("[ERROR] Category cannot be empty.")

    # # Option 5: Category gap analysis
    # elif choice == "5":
    #     already_in_stock = (
    #         library_categories & student_wishlist
    #     )

    #     purchase_order_needed = (
    #         student_wishlist - library_categories
    #     )

    #     full_combined_coverage = (
    #         library_categories | student_wishlist
    #     )

    #     print("\n--- Category Gap Analysis ---")
    #     print("1. Already in Stock:", already_in_stock)
    #     print("2. Purchase Order Needed:", purchase_order_needed)
    #     print("3. Full Combined Coverage:", full_combined_coverage)

    # # Option 6: Exit
    # elif choice == "6":
    #     print("Thank you. Goodbye!")
    #     break

    # # Invalid choice
    # else:
    #     print("[INVALID] Enter a number from 1 to 6.")



