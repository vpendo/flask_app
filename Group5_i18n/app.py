from flask import Flask, render_template, request, session, g, redirect, url_for
from flask_babel import Babel, _
from datetime import datetime
import os

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(os.path.dirname(__file__), 'translations')
app.secret_key = 'your_secret_key'

def get_locale():
    # First check if language is set in session
    if 'language' in session:
        return session['language']
    # Then check if language is in request args (for direct language switching)
    if request.args.get('lang'):
        return request.args.get('lang')
    # Finally, try to guess the language from the user accept
    return request.accept_languages.best_match(['en', 'fr', 'rw', 'sw'])

babel = Babel(app, locale_selector=get_locale)

@app.before_request
def before_request():
    g.locale = get_locale()
    g.current_time = datetime.now()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/set_language', methods=['POST'])
def set_language():
    language = request.form.get('language')
    if language in ['en', 'fr', 'rw', 'sw']:
        session['language'] = language
    return redirect(request.referrer or url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) 