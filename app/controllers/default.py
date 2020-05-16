from app import app


@app.route("/")
def Index():
    return "Hello World!!"
