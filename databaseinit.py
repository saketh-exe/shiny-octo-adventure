import connectDB 

DB, cursor = connectDB.connectDB()

def init_db():

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS POSTS(
            id INT AUTO_INCREMENT PRIMARY KEY, 
            title VARCHAR(255) NOT NULL, 
            content TEXT NOT NULL,
            author_name VARCHAR(200) NOT NULL
        )
        """
    )
    

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS COMMENTS (
                   
            id INT AUTO_INCREMENT PRIMARY KEY,
            post_id INT NOT NULL,
            parent_id INT NULL,
            content TEXT NOT NULL,
            author_name VARCHAR(100) NOT NULL,
            FOREIGN KEY (post_id) REFERENCES POSTS(id) ON DELETE CASCADE,
            FOREIGN KEY (parent_id) REFERENCES COMMENTS(id) ON DELETE CASCADE,
            INDEX idx_post_id (post_id),
            INDEX idx_parent_id (parent_id)
                   
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS TAGS (
        tag_name VARCHAR(100) NOT NULL PRIMARY KEY,
        usage_count INT NOT NULL DEFAULT 1
        )

"""
    )
    
    print("Database tables created successfully!")
    DB.commit()

init_db()