from flask import Flask, Markup
from flask.helpers import url_for
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

def get_card(title):
    inner_text = f'''
    <div class="content">
        <div class="header">{title}</div>
    </div>
    '''
    return uio.Element('div', _class='ui fluid card', inner_text=inner_text)


@app.route('/sidebar')
def load_sidebar():
    sidebar = uio.SideBar()
    sidebar.sidebar_menu.append(
        uio.Image(url_for('static', filename='vlogo.png'), _class='ui small centered image'),
        uio.MenuHeaderItem('Brand Name'),
        uio.MenuItem('Admin', 'admin'),
        uio.MenuItem('CRM', 'crm'),
        uio.MenuItem('CUS', 'cus'),
    )
    system_dd = uio.Dropdown('System', _class='ui dropdown item')
    system_dd.append(
        uio.DropdownMenu(
            uio.DropdownMenuItem('Module', url='module', icon=uio.Icon('tools icon'))
        )
    )
    sidebar.nav_menu.append(
        uio.MenuHeaderItem('FlaskUIO'),
        system_dd,
        uio.MenuItem('Resource'),
        uio.RightMenu(
            uio.MenuItem('User Name', 'account', uio.Icon('user icon')),
            uio.MenuItem('Logout', 'logout', uio.Icon('sign out alternate icon'))    
        ),
    )
    doc = uio.Document('Fomantic Ui - Sidebar')
    doc.body.append(sidebar)
    return Markup(doc.get_html())

@app.route('/menu')
def load_menu():
    menu1 = uio.Menu(
        uio.MenuHeaderItem('FlaskUIO'),
        uio.MenuItem('About Us', 'about_us'),
        uio.MenuItem('Jobs', 'job'),
        uio.MenuItem('Locations', 'locations'),
        _class='ui primary inverted large menu custom',
    )
    menu2 = uio.Menu(
        uio.MenuActiveItem('Home', 'home'),
        uio.MenuItem('Message', 'message'),
        uio.MenuItem('Friend', 'friend'),
        uio.RightMenu(
            uio.MenuItem('Men Sopheak', 'account', uio.Icon('user icon')),
            uio.MenuItem('Logout', 'logout', uio.Icon('sign out alternate icon'))    
        ),
        _class='ui secondary menu',
    )
    display_options = uio.DropdownMenu(
        uio.DropdownMenuItem('Text Size', _class='header'),
        uio.DropdownMenuItem('Small', 'small'),
        uio.DropdownMenuItem('Medium', 'medium'),
        uio.DropdownMenuItem('Large', 'large'),
    )
    menu3 = uio.Menu(
        uio.MenuActiveItem('Account', 'account'),
        uio.MenuItem('Settings', 'setting'),
        uio.Dropdown('Display Options', display_options, _class='ui dropdown item'),
        _class='ui vertical menu'
    )
    
    segment = uio.Segment(menu2, menu3, _class='ui basic segment')
    doc = uio.Document('Fomantic Ui - Menu')
    doc.body.append(menu1, segment)
    return Markup(doc.get_html())

@app.route('/grid')
def load_grid():
    grid1 = uio.Grid()
    grid1.append(uio.GridColumn(nb_wide=4).append(get_card('4 wide column')))
    grid1.append(uio.GridColumn(nb_wide=4).append(get_card('4 wide column')))
    grid1.append(uio.GridColumn(nb_wide=4).append(get_card('4 wide column')))
    grid1.append(uio.GridColumn(nb_wide=4).append(get_card('4 wide column')))
    
    grid2 = uio.Grid()
    grid2.append(uio.GridColumn(get_card('4 wide column'), nb_wide=4))
    grid2.append(uio.GridColumn(get_card('4 wide column'), nb_wide=4))
    grid2.append(uio.GridColumn(get_card('4 wide column'), nb_wide=4))
    grid2.append(uio.GridColumn(get_card('4 wide column'), nb_wide=4))
    grid2.append(uio.GridColumn(get_card('2 wide column'), nb_wide=2))
    grid2.append(uio.GridColumn(get_card('8 wide column'), nb_wide=8))
    grid2.append(uio.GridColumn(get_card('6 wide column'), nb_wide=6))
    
    grid3 = uio.Grid(nb_col=4)
    grid3.append(
        uio.GridRow(
            uio.GridColumn(get_card('column')),
            uio.GridColumn(get_card('column')),
            uio.GridColumn(get_card('column')),
        )
    )
    grid3.append(uio.GridColumn(get_card('column')))
    grid3.append(uio.GridColumn(get_card('column')))
    grid3.append(uio.GridColumn(get_card('column')))
    grid3.append(uio.GridColumn(get_card('column')))
    
    segment = uio.Segment(grid1, grid2, grid3, _class='ui basic segment')
    doc = uio.Document('Fomantic Ui - Grid')
    doc.body.append(segment)
    return Markup(doc.get_html())

@app.route('/segment')
def segment():
    doc = uio.Document('Fomantic Ui')
    content = uio.Segment(
        uio.Segments(
            uio.Segment(uio.Element('p', inner_text='Top Attached'), _class='ui top attached very padded segment'),
            uio.Segment(uio.Element('p', inner_text='Attached'), _class='ui attached very padded segment'),
            uio.Segment(_class='ui attached loading very padded left aligned segment'),
            uio.Segment(uio.Element('p', inner_text='Bottom Attached'), _class='ui bottom attached very padded segment'),
        ),
        uio.Segment(uio.Text('Massive', _class='ui inverted red massive text'), _class='ui inverted segment'),
        _class='ui basic segment'
    )
    doc.body.append(content)
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
            uio.TableStaticLinkItem('category_name', Category.name, fp_col_name='category_name'),
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
    doc.body.append(table)
    return Markup(doc.get_html())

@app.route('/form', methods=['GET', 'POST'])
def load_form():
    
    # form
    form = uio.Form()
    register_date = uio.DateField('register_date', required=True)
    register_datetime = uio.DateTimeField('register_datetime', required=True)
    gender = uio.DropDownField('gender', [('Male', 'Male'), ('Female', 'Female')], required=True)
    category = uio.QueryDropDownField(
        'category',
        True,
        dbname='test',
        field_id='id',
        field_name='name',
        from_table='category',
        order_by='name desc',
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
    username = uio.TextField('username', required=True)
    password = uio.TextField('password', True, input_type='password')
    desc = uio.TextAreaField('description')
    content = uio.TextAreaSummernoteField('content')
    submit = uio.Button('Submit', _class='ui fluid primary button')
    form.append(
        register_date, 
        register_datetime,
        gender,
        category,
        post,
        username,
        password,
        desc,
        content,
        submit,
    )
    
    # doc content
    doc = uio.Document('FlaskUIO', True)
    container = uio.Container(_class='ui container')
    header = uio.Element('h1', _class='ui primary header', inner_text='FlaskUIO Form')
    container.append(header, form)
    doc.body.append(container)
    
    if form.validate_on_submit():
        register_date.data = register_date.data
        register_datetime.data = register_datetime.data
        gender.data = gender.data
        category.data = category.data
        post.data = post.data
        username.data = username.data
        password.data = password.data
        desc.data = desc.data
        content.data = content.data
        
    return Markup(doc.get_html())

@app.route('/basic')
def load_basic():
    doc = uio.Document('FlaskUIO')
    container = uio.Container(_class='ui container')
    header = uio.Element('h1', _class='ui primary header', inner_text='FlaskUIO')
    paragraph = uio.Element('p', 'Build user interface with FlaskUIO Element widget.')
    container.append(header, paragraph)
    doc.body.append(container)
    return Markup(doc.get_html())

@app.route('/doc')
def load_doc():
    doc = uio.Document('HTML Document')
    doc.body.append(uio.Element('h1', _class='ui blue center aligned header', inner_text='Document Widget'))
    
    container = uio.Container(_class='ui text container')
    
    card1 = uio.Cards(
        uio.Card(uio.CardImage(url_for('static', filename='python_logo.png')), url='https://www.python.org/'),
        uio.Card(uio.CardImage(url_for('static', filename='js.png'))),
        uio.Card(uio.CardImage(url_for('static', filename='c#.png'))),
        uio.Card(uio.CardImage(url_for('static', filename='python_logo.png'))),
        uio.Card(uio.CardImage(url_for('static', filename='js.png'))),
        uio.Card(uio.CardImage(url_for('static', filename='c#.png'))),
        nb_card=6
    )
    container.append(card1)
    
    card2 = uio.Card(
        uio.CardImage(url_for('static', filename='python_logo.png')),
        uio.CardContent(
            uio.CardContentHeader('Python'),
            uio.CardContentDesc('Python is a programming language that lets you work quickly and integrate systems more effectively'),
        ),
        uio.CardContent(
            uio.Button('Learn More', _class='ui blue button'),
            _class='extra content'
        ),
        _class='ui fluid card'
    )
    container.append(card2)
    
    container.append(uio.Element('div', _class='ui divider'))
    
    d = uio.Dropdown('Gender', 
        uio.DropdownMenu(
            uio.DropdownMenuItem('Male', icon=uio.Element('i', _class='male icon')),
            uio.DropdownMenuItem('Female', icon=uio.Element('i', _class='female icon')),
        ),
    )
    container.append(d)
    
    doc.body.append(container)
    
    return Markup(doc.get_html())

@app.route('/')
def index():
    google = uio.Element('a', 'Google', _href='http://google.com')
    # fields
    is_active = uio.CheckBoxField('is_active')
    submit = uio.Button('submit', 'register', _class='ui primary button')
    register = uio.LinkButton('Need an account?', 'register')
    img1 = uio.Image(url_for('static', filename='python_logo.png'))
    img2 = uio.LinkImage(url_for('static', filename='python_logo.png'), 'http://google.com')
    
    # form
    form = uio.Element('form', _class='ui form')
    form.append(is_active, submit, register)
    
    # html
    doctype = uio.Element('', '<!DOCTYPE html>')
    html = uio.Element('html', _lang='en')
    
    # head
    head = uio.Head('Flask UIO')
    head.append(
        uio.Element('meta', _charset='UTF-8'),
        uio.Element('meta', _name='viewport', _content='width=device-width, initial-scale=1.0')
    )
    head.append_link('https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.7/dist/semantic.min.css')
    
    # body
    body = uio.Body(_class='ui container', _style='background-color: #f2f2f2')
    body.append(
        google,
        form,
        img1,img2,
    )
    body.append_script(
        'https://cdn.jsdelivr.net/npm/jquery@3.3.1/dist/jquery.min.js',
        'https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.7/dist/semantic.min.js',
    )
    body.append_injected_script(uio.Script())
    html.append(head, body)
    doc = doctype.get_html() + html.get_html()
    return Markup(doc)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
