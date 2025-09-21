import connectDB
from collections import defaultdict
DB , cursor = connectDB.connectDB()

def get_tags_from_content(content:str):
    tags = defaultdict(int)
    words = content.split()
    for word in words:
        if word.startswith("#") and len(word) > 1:
            tag = word[1:].lower()
            tags[tag] += 1
    for tag, count in tags.items():
        cursor.execute(
            """
            INSERT INTO TAGS (tag_name, usage_count)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE usage_count = usage_count + VALUES(usage_count)
            """,
            (tag, count)
        )
    DB.commit()

def get_top_k_tags(k:int):
    cursor.execute("""
        SELECT tag_name,usage_count FROM TAGS ORDER BY usage_count DESC LIMIT %s
        """, (k,))
    return cursor.fetchall()

def populate_tags(): # To populate tags from existing posts in DB
    cursor.execute("SELECT content FROM POSTS")
    posts = cursor.fetchall()
    for post in posts:
        get_tags_from_content(post[0]) #type: ignore