import csv, httpx


def save_to_csv(users: list):
    with open('users.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['id', 'name', 'email'])

        writer.writeheader()
        writer.writerows(users)


def fetch_users():
    URL = 'https://jsonplaceholder.typicode.com/users'

    res = httpx.get(URL)
    res.raise_for_status()

    return [
        {'id': user['id'],
         'name': user['name'],
         'email': user['email']}
        for user in res.json()
    ]
