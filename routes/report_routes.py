import main

main.app.get('/')


def home():
    return {"message": "Api connected"}
