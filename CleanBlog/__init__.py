from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

from CleanBlog import routes