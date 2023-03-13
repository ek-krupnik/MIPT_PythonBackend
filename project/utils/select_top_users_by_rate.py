def select_top_users_by_rate(users, top_size):
    users_sorted = sorted(users, key=lambda users: users.rate, reverse=True)
    return users_sorted[:top_size]
