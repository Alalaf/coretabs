from flask import Flask, render_template, request, url_for, redirect
from store import Post, PostStore
app = Flask(__name__)

dummy_posts = [
    Post(id=1,
         photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50',
         name='Sara',
         body='First interesting topic goes here'),
    Post(id=2,
         photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
         name='John',
         body='Second interesting topic goes here'),
]
post_store = PostStore()
post_store.add(dummy_posts[0])
post_store.add(dummy_posts[1])

posts = post_store.get_all()


@app.route('/')
def show_posts():
    return render_template('index.html', posts=posts)


app.current_id = 3


@app.route('/add_post/', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        new_post = Post(id=app.current_id,
                    photo_url=request.form['photo_url'],
                    name=request.form['name'],
                    body=request.form['body'])
        post_store.add(new_post)
        app.current_id += 1
        return redirect(url_for('show_posts'))
    elif request.method == 'GET':
        return render_template('add_post.html')

app.run()