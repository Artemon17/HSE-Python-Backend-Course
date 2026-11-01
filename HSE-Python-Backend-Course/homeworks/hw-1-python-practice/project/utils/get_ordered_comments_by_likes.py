from models.comment import Comment


def comp(com):
    return com.like_count

def get_ordered_comments_by_likes(comments: list[Comment]) -> list[Comment]:
    return sorted(comments, key=comp, reverse=True)
