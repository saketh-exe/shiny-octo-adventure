from postManager import create_post, view_posts, comment_on_post , reply

running  = True

while running:
    print("welcome to The App, what do you want to do?")
    print("1. Create a post")
    print("2. Comment on a post")
    print("3. Reply to a comment")
    print("4. View all posts with comments")
    print("5. Edit a post content")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))
    if choice == 1:
        print()
        create_post()
        print()
    elif choice == 2:
        print()
        comment_on_post()
        print()
    elif choice == 3:
        print()
        reply()
        print()
    elif choice == 4:
        print("---------------------------------------------------")
        view_posts()
        print("---------------------------------------------------")
    elif choice == 5:
        
    elif choice == 6:
        running = False
        print("Exiting the application. Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
