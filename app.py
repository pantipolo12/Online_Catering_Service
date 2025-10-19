from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'SECRET'


users = {
    "test@email.com": {
        "password": "test123",
        "name": "Test User",
        "role": "customer"
    }
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.get(email)
        if user and user['password'] == password:
            session['user_id'] = email
            session['name'] = user['name']
            session['role'] = user['role']
            flash("Login successful!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invaled enail or passwork.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Simple validation
        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return redirect(url_for('register'))

        if email in users:
            flash("Email already registered.", "warning")
            return redirect(url_for('register'))

        # Register new user (in-memory dictionary for demo)
        users[email] = {
            'password': password,
            'name': name,
            'role': 'customer'  # default role
        }

        flash("Registration successful! Please login.", "success")
        return redirect(url_for('login'))

    # GET request
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('index'))


@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order_history.html')
def order_history():
    return render_template('order_history.html')


@app.route('/cart.html')
def cart():
    return render_template('cart.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
