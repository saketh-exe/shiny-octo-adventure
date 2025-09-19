from postManager import create_post, view_posts
import connectDB 
DB , cursor = connectDB.connectDB()


running  = True

while running:
    print("welcome to The App, what do you want to do?")
    print("1. Create a post")
    print("2. Comment on a post")
    print("3. Reply to a comment")
    print("4. View all posts with comments")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        print()
        create_post()
        print()
    elif choice == 2:
        continue
    elif choice == 3:
        continue
    elif choice == 4:
        print("---------------------------------------------------")
        view_posts()
        print("---------------------------------------------------")
    elif choice == 5:
        running = False
        print("Exiting the application. Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
