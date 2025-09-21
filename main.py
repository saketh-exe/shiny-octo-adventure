from postManager import create_post, view_posts, comment_on_post , reply , edit_post

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
        print("="*50)
        create_post()
        print("="*50)
    elif choice == 2:
        print("="*50)
        comment_on_post()
        print("="*50)
    elif choice == 3:
        print("="*50)
        reply()
        print("="*50)
    elif choice == 4:
        print("="*50)
        view_posts()
        print("="*50)
    elif choice == 5:
        print("="*50)
        edit_post()
        print("="*50)
    elif choice == 6:
        running = False
        print("Exiting the application. Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
