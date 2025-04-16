#1
users = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@gmail.com'},
    {'name': 'Bob', 'age': 35, 'email': 'bob@gmail.com'},
    {'name': 'Charlie', 'age': 45, 'email': 'charlie@gmail.com'},
]

def process_user(user):
    return {
        'name': user['name'],
        'age': int(user['age']),
        'email': user['email'].lower()
    }
    
print(users)

#2

(Vector3){-10.0f, 1.0f, 10.0f}, 2.0f, 2.0f, 2.0f, WHITE)