import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

# Server (c9) - https://community.c9.io/t/cant-preview-in-aws-c9/23340/4
if __name__ == '__main__':
    app.debug = True
    app.run(host=os.environ['IP'], port=os.environ['PORT'])
    