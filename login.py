from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace with actual database)
users = {
    "user1": {"username": "user1", "password": "password1"},
    "user2": {"username": "user2", "password": "password2"}
}

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome to the Home Page</h1>
        <p>This is the home page of the Coffee Shop website.</p>
        <a href="/login">Login</a> | <a href="/signup">Sign Up</a>
    </body>
    </html>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            # Successful login, redirect to dashboard or homepage
            return redirect(url_for('dashboard'))
        else:
            # Invalid credentials, render login page with error message
            return """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Login</title>
            </head>
            <body>
                <h1>Login</h1>
                <p>Invalid username or password. Please try again.</p>
                <form method="post">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username"><br>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password"><br>
                    <input type="submit" value="Login">
                </form>
            </body>
            </html>
            """
    else:
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login</title>
        </head>
        <body>
            <h1>Login</h1>
            <form method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
        </body>
        </html>
        """

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            # User already exists, render signup page with error message
            return """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Sign Up</title>
            </head>
            <body>
                <h1>Sign Up</h1>
                <p>Username already exists. Please choose another username.</p>
                <form method="post">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username"><br>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password"><br>
                    <input type="submit" value="Sign Up">
                </form>
            </body>
            </html>
            """
        else:
            # Add new user to the database (dummy implementation)
            users[username] = {"username": username, "password": password}
            # Redirect to login page after successful signup
            return redirect(url_for('login'))
    else:
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sign Up</title>
        </head>
        <body>
            <h1>Sign Up</h1>
            <form method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password"><br>
                <input type="submit" value="Sign Up">
            </form>
        </body>
        </html>
        """

@app.route('/dashboard')
def dashboard():
    return "Welcome to the dashboard"

if __name__ == '__main__':
    app.run(debug=True)
