# Flask-UIO (dev)

Flask-UIO is a package for building user interface as object.

The package currently is based on 'flask', 'Flask-WTF', 'requests', 'cryptography', 'Flask-SQLAlchemy'.



### Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip install flask-uio
```



### Example

```python
from flask import Flask, Markup
from flask_sqlalchemy import SQLAlchemy
import flask_uio as uio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI_DICT'] = {
    'test': 'sqlite:///test.db',
}

# caution generate your own fernet key and store in your secret place
app.config['FLASK_UIO_FERNET_SECRET_KEY'] = 'generate fernet key'

flask_uio = uio.FlaskUIO(app)
db = SQLAlchemy(app)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"
    
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    content = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"Post(id={self.id}, title='{self.title}', category_id={self.category_id}, content='{self.content}')"

@app.route('/')
def index():
    doc = uio.FomanticDocument('Fomantic Ui')
    title = uio.Element('div', 'ui primary header', inner_text='Welcome To FlaskUIO')
    content = uio.Element('div', 'content', inner_text="Flask-UIO is a package for building user interface as object.")
    card = uio.Element('div', 'ui fluid card')
    card.append_inner(content)
    doc.body.append(title, card)
    return Markup(doc.get_html())

@app.route('/form')
def form():
    doc = uio.FomanticDocument('Fomantic Ui')
    title = uio.Element('div', 'ui primary header', inner_text='FlaskUIO Form')
    f = uio.Form()
    username = uio.TextField('username', required=True)
    password = uio.TextField('password', required=True, input_type='password')
    post_content = uio.TextAreaSummernoteField('Content')
    category = uio.QueryDropDownField(
        'category',
        True,
        dbname='test',
        field_id='id',
        field_name='name',
        from_table='category',
    )
    post = uio.QueryDropDownField(
        'post',
        True,
        dbname='test',
        field_id='id',
        field_name='title',
        from_table='post',
        where=f'category_id = {category.data if category.data else 0}',
        parents=[category]
    )
    post_date = uio.DateField('post_date', required=True)
    publish_at = uio.DateTimeField('publish_at', required=True)
    is_private = uio.CheckBoxField('is_private')
    submit = uio.Element('input', 'ui primary button', attrs=[('type', 'submit'), ('value', 'Submit')])
    f.append_inner(
        username,
        password,
        category,
        post,
        post_date,
        publish_at,
        is_private,
        post_content,
        submit,
    )
    segment = uio.Element('div', 'ui segment', inner_elements=[title, f])
    container = uio.Element('div', 'ui container', inner_elements=[segment])
    doc.body.append(container)
    if f.validate_on_submit():
        f.flash_success()
    
    username.data = username.data
    password.data = password.data
    category.data = category.data
    post.data = post.data
    post_content.data = post_content.data
    post_date.data = post_date.data
    publish_at.data = publish_at.data
    is_private.data = is_private.data
    
    return Markup(doc.get_html())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```



### To Generate Fernet Key

```python
>>> from flask_uio import Token
>>> Token.key
>>> Token.key()
'-UfLR0ZH4kJ0Q4BJ-giUWOz76qJ4U_ZRIzsH67tnucA='
```



### Default Config

```
FLASK_UIO_FOMANTIC_STATIC_FOLDER: None
FLASK_UIO_FOMANTIC_CSS_FILENAME: None
FLASK_UIO_FOMANTIC_JS_FILENAME: None
FLASK_UIO_DATE_DISPLAY_FORMAT: 'None'
FLASK_UIO_DATE_FORMAT: '%Y-%m-%d'
FLASK_UIO_DATETIME_FORMAT: '%Y-%m-%d %H:%M:%S.%f'
FLASK_UIO_DATE_DISPLAY_FORMAT: '%d-%b-%Y'
FLASK_UIO_DATETIME_DISPLAY_FORMAT: '%d-%b-%Y, %I:%M %p'
FLASK_UIO_DATE_JS_FORMAT: 'dd-MMM-yyyy'
FLASK_UIO_DATETIME_JS_FORMAT: 'dd-MMM-yyyy, hh:mm a'
FLASK_UIO_MAX_CONTENT_LENGTH: 10 * 1024 * 1024
FLASK_UIO_UPLOAD_EXTENSIONS: ['.jpeg', '.jpg', '.png', '.gif', '.pdf', '.xlsx', 'xls', '.csv']
FLASK_UIO_UPLOAD_PATH: None
FLASK_UIO_API_SERVER: 'http://0.0.0.0:5000'
FLASK_UIO_FERNET_SECRET_KEY: None
SQLALCHEMY_DATABASE_URI_DICT: None
```



### Roadmap:

- Build kind of widget/component based on [Fomantic-UI](https://fomantic-ui.com/), a community fork of Semantic-UI
- Test coverage
- Add support for more CSS frameworks





