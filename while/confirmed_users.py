unconfirmed_users = ['alice','brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)

for confirmed_user in sorted(confirmed_users):
    print(confirmed_user.title())