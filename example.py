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
    doc = uio.Document('Fomantic Ui')
    title = uio.Element('div', 'ui primary header', inner_text='Welcome To FlaskUIO')
    content = uio.Element('div', 'content', inner_text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Why do we use it It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
    card = uio.Element('div', 'ui fluid card')
    card.append_inner(content)
    icon = uio.Icon(css_class='large home icon')
    link_icon = uio.LinkIcon('large google red icon', 'http://google.com', '_blank')
    segment = uio.Element('div', 'ui basic segment', inner_elements=[title, card, icon, link_icon])
    doc.body.append(segment)
    return Markup(doc.get_html())

@app.route('/table', methods=['GET', 'POST'])
def load_table():
    doc = uio.Document('Fomantic Ui')
    table = uio.Table(
        title='Post',
        reload_route=uio.Route('load_table'),
        detail_route=uio.Route('load_table'),
        new_route=uio.Route('load_table'),
        delete_route=uio.Route('load_table'),
        edit_route=uio.Route('load_table'),
        colitems=[
            uio.TableColItem('id', Post.id, is_key=True),
            uio.TableColItem('title', Post.title),
            uio.TableColItem('content', Post.content),
            uio.TableColItem('category_name', Category.name),
        ],
        allow_paginate=True,
        allow_search=True,
        allow_sort=True,
    )
    data = (
        Post
        .query
        .join(Category, Category.id == Post.category_id)
        .with_entities(
            Post.id,
            Post.title,
            Post.content,
            Category.name.label('category_name')
        )
        .filter(*table.filter)
        .order_by(*table.order_by)
        .paginate(**table.paginate)
    )
    table.refresh(data)
    content = uio.Segment(table, opt_css_class='basic')
    doc.body.append(content)
    return Markup(doc.get_html())

@app.route('/segment')
def segment():
    doc = uio.Document('Fomantic Ui')
    content = uio.Segment(
        uio.Segments(
            uio.Segment(uio.Element('p', inner_text='Top Attached'), opt_css_class='top attached very padded'),
            uio.Segment(uio.Element('p', inner_text='Attached'), opt_css_class='attached very padded'),
            uio.Segment(opt_css_class='attached loading very padded left aligned'),
            uio.Segment(uio.Element('p', inner_text='Bottom Attached'), opt_css_class='bottom attached very padded'),
        ),
        uio.Segment(uio.Text('Massive', opt_css_class='inverted red massive'), opt_css_class='inverted'),
        uio.A(
            uio.Segment(uio.Text('Google', opt_css_class='green massive')),
            url='http://google.com',
            target='_blank'
        ),
        opt_css_class='basic'
    )
    doc.body.append(content)
    return Markup(doc.get_html())

@app.route('/form', methods=["GET", "POST"])
def form():
    doc = uio.Document('Fomantic Ui')
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
    submit = uio.Button('Submit', btn_type='button', color='blue')
    modal = uio.ConfirmModal('Confirmation Modal', 'Are you sure to proceed this form?', calling_id=submit.id, icon=uio.Icon('delete icon'))
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
    segment = uio.Element('div', 'ui segment', inner_elements=[title, f, modal])
    container = uio.Container(segment)
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
    
