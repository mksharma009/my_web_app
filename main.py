from fastapi import FastAPI, HTTPException

users = dict(manish=18, eeshu=19, deepesh=20, jyoti=21)

app = FastAPI()

@app.get('/users')
def get_users():
    return list(users.keys())

@app.get('/users/{user_id}')
def get_user_info(user_id):
    if user_id in users:
        return f'The age of {user_id} is {users[user_id]}'
    raise HTTPException(status_code = 404,
                        detail = 'User not found')
