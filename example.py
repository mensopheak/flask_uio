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
app.config['FLASK_UIO_FERNET_SECRET_KEY'] = 'Rr1BVGsaSGZnhYnsqPGUFFJk0wFZJ8LmBD32GEc-KZE='

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

# c1 = Category(id=1, name='Sport')
# c2 = Category(id=2, name='Technology')
# c3 = Category(id=3, name='Culture')
# p1 = Post(title='Sport Post 1', category_id=1, content='Sport Post 1')
# p2 = Post(title='Sport Post 2', category_id=1, content='Sport Post 2')
# t1 = Post(title='Tech Post 1', category_id=2, content='Tech Post 1')
# t2 = Post(title='Tech Post 2', category_id=2, content='Tech Post 2')
# c1 = Post(title='Culture Post 1', category_id=3, content='Culture Post 1')
# c2 = Post(title='Culture Post 2', category_id=3, content='Culture Post 2')

@app.route('/')
def index():
    doc = uio.FomanticDocument('Fomantic Ui')
    title = uio.Element('div', 'ui primary header', inner_text='Welcome To FlaskUIO')
    content = uio.Element('div', 'content', inner_text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Why do we use it It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
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
    f.append_inner(
        username,
        password,
        category,
        post,
        post_date,
        publish_at,
        is_private,
        post_content,
    )
    segment = uio.Element('div', 'ui basic segment', inner_elements=[title, f])
    doc.body.append(segment)
    return Markup(doc.get_html())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
