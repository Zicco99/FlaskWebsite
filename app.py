from flask import Flask, render_template, request, redirect


# create the application object
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home')) """
    return render_template('login.html')


""" @app.route('/posts',methods=['GET','POST'])
def posts():
    if request.method=='POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new = BlogPost(title=post_title,content=post_content)
        db.session.add(new)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.title).all()
        return render_template('posts.html', posts=all_posts)
 """


""" @app.route('/page/<string:name>')
def home(name):
    return ''' HomePage
           ''' + name  # return a string """

@app.route('/onlyget', methods=['GET','POST']) #Permetto metodi get e post
def get_req():
    return render_template('home.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True,port=80,host='23.94.219.145')
