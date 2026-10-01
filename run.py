from flask_login import current_user

from app import create_app

app = create_app()


# TEMPORARY: confirms the server runs. Remove once app/routes/ blueprints exist.
@app.route("/")
def hello():
    if current_user.is_authenticated:
        return (
            f"Hello, Captain's Mail. Signed in as {current_user.username}. "
            '<a href="/logout">Sign out</a>'
        )
    return 'Hello, Captain\'s Mail. <a href="/login">Sign in</a>'


if __name__ == "__main__":
    # host="0.0.0.0" lets phones on the same network reach the dev server
    app.run(host="0.0.0.0", port=5000, debug=True)
