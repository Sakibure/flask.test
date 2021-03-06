from flask import Flask, render_template
from markupsafe import escape


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Index page'

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/user/<username>')
    def show_user_profile(username):
        # Show the user profile for that user
        return 'User %s' % escape(username)

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # Show the post with the given id, the id is an integer
        return 'Post %d' % post_id

    @app.route('/path/<path:subpath>')
    def show_subpath(subpath):
        # Show the subpath after /path/
        return 'Subpath %s' % escape(subpath)

    @app.route('/news', methods=['GET'])
    def show_news():
        return "Today’s news is ..."

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=5000)
