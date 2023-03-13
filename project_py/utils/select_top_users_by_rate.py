def select_top_users_by_rate(users: list, top_size: int) -> list:
    users_sorted = sorted(users, key=lambda users: users.rate, reverse=True)
    return users_sorted[:top_size]
