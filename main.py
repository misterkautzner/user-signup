from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET','POST'])
def index():
    username_err_msg = ''
    password_err_msg = ''
    v_password_err_msg = ''
    email_err_msg = ''
    
    if request.method == 'POST':
 
        username = request.form['username']
        password = request.form['password']
        v_password = request.form['v-password']
        email = request.form['email']

        print('username = ', username)


        # Validate username
        if username == '':
            username_err_msg = 'You must enter a username.'
        elif len(username) < 3 or len(username) > 20:
            username_err_msg = 'Usernames must be between 3 and 20 characters in length.'
        elif ' ' in username:
            username_err_msg = 'Usernames must not contain spaces.'

        # Validate password
        if password == '':
            password_err_msg = 'You must enter a password.'
        elif len(password) < 3 or len(password) > 20:
            password_err_msg = 'Passwords must be between 3 and 20 characters in length.'
        elif ' ' in password:
            password_err_msg = 'Passwords must not contain spaces.'

        # Validate validate-password
        if v_password == '' and password != '':
            v_password_err_msg = 'You must verify the password you entered above.'
        if v_password != password:
            v_password_err_msg = 'This does not much the password you entered above.'

        # Validate email
        if email:
            if len(email) < 3 or len(email) > 20:
                email_err_msg = 'Email adresses must be between 3 and 20 characters.'
            if ' ' in email:
                email_err_msg = 'Email addresses must not contain spaces.'
            if '@' not in email:
                email_err_msg = 'Email addresses must contain a "@".'
            if '.' not in email:
                email_err_msg = 'Email addresses must contain a "."'

        # if no errors, then they must have entered everything correctly
        if username_err_msg == '' and password_err_msg == '' and v_password_err_msg == '' and email_err_msg == '':
            return render_template('welcome.html', username = username)
 
        # if errors, render with username and email intact
        else:
            return render_template('user-signup.html', username = username, email = email, username_err_msg = username_err_msg, password_err_msg = password_err_msg, v_password_err_msg = v_password_err_msg, email_err_msg = email_err_msg)

    return render_template('user-signup.html', username_err_msg = username_err_msg, password_err_msg = password_err_msg, v_password_err_msg = v_password_err_msg, email_err_msg = email_err_msg)

app.run()