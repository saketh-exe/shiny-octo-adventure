import connectDB

DB, cursor = connectDB.connectDB()


def fetch_comments(post_id: int):
    cursor.execute(
        "SELECT id, parent_id, content, author_name FROM COMMENTS WHERE post_id = %s",
        (post_id,),
    )
    rows = cursor.fetchall()
    return [
        {"id": r[0], "parent_id": r[1], "content": r[2], "author": r[3]} # type: ignore
        for r in rows
    ]


def build_comment_tree(comments, parent_id=None):
    tree = []
    for c in comments:
        if c["parent_id"] == parent_id:
            c["children"] = build_comment_tree(comments, c["id"])
            tree.append(c)
    return tree


def calculate_depth(comment):
    if not comment.get("children"):
        return 1
    return 1 + max(calculate_depth(child) for child in comment["children"])


def count_total_replies(comment):
    if not comment.get("children"):
        return 0
    return len(comment["children"]) + sum(
        count_total_replies(c) for c in comment["children"]
    )


def find_viral_chain(comment, path=None):
    if path is None:
        path = []
    path = path + [comment["id"]]

    if not comment.get("children"):
        return path

    longest = path
    for child in comment["children"]:
        chain = find_viral_chain(child, path)
        if len(chain) > len(longest):
            longest = chain
    return longest


def analyze_post_comments(post_id: int):
    """
    Analyze all top-level comments for a post:
    - Depth
    - Total replies
    - Viral chain
    """
    comments = fetch_comments(post_id)
    tree = build_comment_tree(comments)

    results = []
    for root_comment in tree:
        depth = calculate_depth(root_comment)
        replies = count_total_replies(root_comment)
        viral_chain = find_viral_chain(root_comment)

        results.append(
            {
                "comment_id": root_comment["id"],
                "content": root_comment["content"],
                "author": root_comment["author"],
                "depth": depth,
                "total_replies": replies,
                "viral_chain": viral_chain,
            }
        )
    return results
