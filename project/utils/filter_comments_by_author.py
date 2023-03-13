from models.user import User

def filter_comments_by_author(comments: list, author: User) -> list:
    return [comment for comment in comments if comment.author_id == author.id]
