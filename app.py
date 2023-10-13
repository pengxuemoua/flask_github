from flask import Flask, render_template, request  # NOT the same as requests 
from github_api import get_github_user 

app = Flask(__name__)

@app.route('/') # '/' is the home page; this is a route handler
def homepage():
    return render_template('index.html')

@app.route('/get_user') # route handler will handle requests to the get_user path in the url
def get_user_info():
    # get user info from github, and display on new page
    print('form data is', request.args) # the form data is in variable "request.args"
    username = request.args.get('username') # will allow you to use the username, will return None if no username
    
    user_info, error_message = get_github_user(username)
    if error_message:
        return render_template('errors.html', error=error_message)
    else:  
        return render_template('github.html', github_info=user_info) # route handler must return something, or None

if __name__ == '__main__':
    app.run()