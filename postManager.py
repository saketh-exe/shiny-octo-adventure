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
        print(f"\nTitle: {post[1]}\n\nContent: {post[2]}\n\nAuthor: {post[3]}\n") #type: ignore
        print("Comments:")
        cursor.execute(f"select * from COMMENTS where post_id={selected_post_id} AND parent_id IS NULL")
        comments = cursor.fetchall()
        for comment in comments:
            print(f"Comment ID: {comment[0]}, Content: {comment[3]}, Author: {comment[4]}") #type: ignore
            print("Replies: ")
            display_comment_replies(comment[0]) #type: ignore
            print("-"*50)
    else:
        print("Post not found.")


def comment_on_post():
    cursor.execute("select id,title,author_name from POSTS")
    posts = cursor.fetchall()
    for post in posts:
        print(f"ID: {post[0]}, Title: {post[1]}, Author: {post[2]}") #type: ignore
    selected_post_id = int(input("Enter the ID of the post you want to comment on: "))
    comment_author = input("Enter your name: ")
    comment_content = input("Enter your comment: \n")
    cursor.execute(
    f"""
    INSERT into COMMENTS (post_id, content, author_name) values ("{selected_post_id}","{comment_content}","{comment_author}")
    """
    )
    DB.commit()
    print("Comment added successfully.")

def display_comment_replies(comment_id, level=0): # Recursive
    cursor.execute(f"select * from COMMENTS where parent_id={comment_id}")
    replies = cursor.fetchall()
    for reply in replies:
        print(f"{'  ' * level}Reply ID: {reply[0]}, Content: {reply[3]}, Author: {reply[4]}") #type: ignore
        display_comment_replies(reply[0], level + 1) #type: ignore

def reply():
    print("Select the post you want to comment on:")
    cursor.execute("select id,title,author_name from POSTS")
    posts = cursor.fetchall()

    for post in posts:
        print(f"ID: {post[0]}, Title: {post[1]}, Author: {post[2]}") #type: ignore
    
    selected_post_id = int(input("Enter the ID of the post you want to comment on: "))
    
    cursor.execute(f"select * from COMMENTS where post_id={selected_post_id} AND parent_id IS NULL")
    comments = cursor.fetchall()
    print("select the comment tree you want to view ")
    
    for comment in comments:
        print(f"Comment ID: {comment[0]}, Content: {comment[3]}, Author: {comment[4]}") #type: ignore
    
    selected_comment_id = int(input("Enter the ID of the comment you want to view : "))
    cursor.execute(f"select * from COMMENTS where id={selected_comment_id}")
    comment = cursor.fetchone()
    if comment:
        print(f"\nComment_id: {comment[0]}, Content: {comment[3]}, Author: {comment[4]}") #type: ignore
        display_comment_replies(comment[0]) #type: ignore
        print("-"*50)
        selected_id = int(input("Enter the ID of the comment you want to reply to: "))
        reply_author = input("Enter your name: ")
        reply_content = input("Enter your reply: \n")
        cursor.execute(
            f"""
            INSERT into COMMENTS (post_id, parent_id, content, author_name) values ("{selected_post_id}","{selected_id}","{reply_content}","{reply_author}")
            """
        )
        DB.commit()
        print("Reply added successfully.")
