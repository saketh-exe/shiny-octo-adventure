from hashTagEngine import get_top_k_tags, suggest_related_tags, populate_tags

running = True

while running:
    print("=== Hashtag Dashboard ===")
    print("1. Show top hashtags")
    print("2. Get related tag suggestions")
    print("3. Populate tags from existing posts")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        print("="*50)
        k = int(input("How many top hashtags to show? "))
        top_tags = get_top_k_tags(k)
        print(f"Top {k} Hashtags:")
        for i, tag in enumerate(top_tags, 1):
            print(f"{i}. #{tag[0]}: {tag[1]} uses")  # type: ignore
        print("="*50)
        
    elif choice == 2:
        print("="*50)
        tag = input("Enter a hashtag to get suggestions for: ")
        limit = int(input("How many suggestions to show? "))
        suggestions = suggest_related_tags(tag, limit)
        print(f"Related tags for '{tag}':")
        for suggestion in suggestions:
            print(f"  {suggestion}")
        print("="*50)
        
    elif choice == 3:
        print("="*50)
        populate_tags()
        print("Tags populated from existing posts!")
        print("="*50)
        
    elif choice == 4:
        running = False
        print("Exiting the dashboard. Goodbye!")
        
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

