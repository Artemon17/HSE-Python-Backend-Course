from models.comment import Comment
from models.user import User


def filter_comments_by_author(comments: list[Comment], author: User) -> list[Comment]:
    return [com for com in comments if com.author_id == author.id]
