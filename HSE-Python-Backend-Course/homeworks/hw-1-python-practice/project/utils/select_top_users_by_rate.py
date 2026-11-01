from models.user import User


# ну я же не лох какой-то, хотелось подрезать немножечка списочек
def quicksort_of_top(a, top_size, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo >= hi or top_size <= 0:
        return a[lo:hi + 1][:top_size]
    pivot = a[(lo + hi) // 2].rate
    i, j = lo, hi
    while i <= j:
        while a[i].rate > pivot: i += 1
        while a[j].rate < pivot: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if top_size < (j - lo + 1):
        return quicksort_of_top(a, top_size, lo, j)
    else:
        return sorted(a[lo:hi+1], key=lambda us: us.rate, reverse=True)[:top_size]

def select_top_users_by_rate(users: list[User], top_size: int) -> list[User]:
    return quicksort_of_top(users, top_size)

