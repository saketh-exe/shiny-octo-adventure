import connectDB
from collections import defaultdict
from itertools import combinations
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
    get_related_hashtags(list(tags.keys()))
    DB.commit()

def get_related_hashtags(hashtags:list[str]):
    pairs = list(combinations(sorted(set(hashtags)), 2))
    for tag1, tag2 in pairs:
        cursor.execute(
            """
            INSERT INTO TAGS_CO_OCCURRENCE (tag_name, co_occurring_tag_name, occurrence_count)
            VALUES (%s, %s, 1)
            ON DUPLICATE KEY UPDATE occurrence_count = occurrence_count + 1
            """,
            (tag1, tag2)
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

def suggest_related_tags(tag:str, k:int):
    cursor.execute(""" 
        SELECT t2.tag_name, c.occurrence_count, t1.usage_count FROM TAGS_CO_OCCURRENCE c
        JOIN TAGS t1 ON c.tag_name = t1.tag_name
        JOIN TAGS t2 ON c.co_occurring_tag_name = t2.tag_name
        WHERE c.tag_name = %s
        AND ((c.occurrence_count/t1.usage_count) >= 0.3)
        ORDER BY c.occurrence_count DESC LIMIT %s
""", (tag, k))
    return cursor.fetchall()
