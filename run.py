from app import create_app

app = create_app()


# TEMPORARY: confirms the server runs. Remove once app/routes/ blueprints exist.
@app.route("/")
def hello():
    return "Hello, Captain's Mail"


if __name__ == "__main__":
    # host="0.0.0.0" lets phones on the same network reach the dev server
    app.run(host="0.0.0.0", port=5000, debug=True)
