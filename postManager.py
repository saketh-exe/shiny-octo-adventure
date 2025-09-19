import connectDB 
DB , cursor = connectDB.connectDB()

def create_post():
    title  = input("Enter title of the post: ")
    content = input("Enter content of the post: ")
    author_name = input("Enter author name: ")


    cursor.execute(f"""
        insert into POSTS (title,content,author_name) values
                ("{title}","{content}","{author_name}")
    """
    )

    DB.commit()
    print("Posted successfully")

def view_posts():
    cursor.execute("select id,title,author_name from POSTS")
    posts = cursor.fetchall()
    for post in posts:
        print(f"ID: {post[0]}, Title: {post[1]}, Author: {post[2]}") #type: ignore
    selected_post_id = int(input("Enter the ID of the post you want to view: "))
    cursor.execute(f"select * from POSTS where id={selected_post_id}")
    post = cursor.fetchone()
    if post:
        print(f"\nTitle: {post[1]}\n\nContent: {post[2]}\n\nAuthor: {post[3]}\n\n") #type: ignore
        print("Comments:")
    else:
        print("Post not found.")