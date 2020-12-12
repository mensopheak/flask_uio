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

# c1 = Category(id=1, name='Sport')
# c2 = Category(id=2, name='Technology')
# c3 = Category(id=3, name='Culture')
# p1 = Post(title='Sport Post 1', category_id=1, content='Sport Post 1')
# p2 = Post(title='Sport Post 2', category_id=1, content='Sport Post 2')
# t1 = Post(title='Tech Post 1', category_id=2, content='Tech Post 1')
# t2 = Post(title='Tech Post 2', category_id=2, content='Tech Post 2')
# c1 = Post(title='Culture Post 1', category_id=3, content='Culture Post 1')
# c2 = Post(title='Culture Post 2', category_id=3, content='Culture Post 2')

def get_card(title):
    inner_text = f'''
    <div class="content">
        <div class="header">{title}</div>
    </div>
    '''
    return uio.Element('div', css_class='ui fluid card', inner_text=inner_text)

@app.route('/message')
def load_message():
    msg1 = uio.Message('The transaction is commited sucessfully.', 'success', 'The transaction is commited sucessfully.', has_segment=True, hideable=False)
    msg2 = uio.Message('The transaction is commited sucessfully.', 'negative', 'The transaction is commited sucessfully.', icon=uio.Icon('inbox icon'), has_segment=True, hideable=False)
    msg3 = uio.Message('The transaction is commited sucessfully.', 'success', icon=uio.Icon('inbox icon'), has_segment=True, hideable=False)
    msg4 = uio.Message('The transaction is commited sucessfully.', 'success', 'The transaction is commited sucessfully.', icon=uio.Icon('inbox icon'), has_segment=True, hideable=False)
    msg5 = uio.Message('The transaction is commited sucessfully.', 'blue', has_segment=True, hideable=False)
    doc = uio.Document('Fomantic Ui - Image')
    doc.body.append(msg1, msg2, msg3, msg4, msg5)
    return Markup(doc.get_html())

@app.route('/breadcrumb')
def load_breadcrumb():
    b1 = uio.Breadcrumb()
    b1.append_inner(
        uio.BreadcrumbSection('Home', 'home', True)
    )
    b2 = uio.Breadcrumb()
    b2.append_inner(
        uio.BreadcrumbSection('Home', 'home', False),
        uio.BreadcrumbDividerIcon(),
        uio.BreadcrumbSection('List', 'list', False),
        uio.BreadcrumbDividerIcon(),
        uio.BreadcrumbSection('Info',is_active=True),
    )
    b3 = uio.Breadcrumb(is_dividing=False)
    b3.append_inner(
        uio.BreadcrumbSection('Home', 'home', False),
        uio.BreadcrumbDividerIcon(),
        uio.BreadcrumbSection('List', 'list', False),
        uio.BreadcrumbDividerIcon(),
        uio.BreadcrumbSection('Info',is_active=True),
    )
    
    segment = uio.Segment(b1, b2, b3, opt_css_class='basic')
    doc = uio.Document('Fomantic Ui - Image')
    doc.body.append(segment)
    return Markup(doc.get_html())

@app.route('/image')
def load_image():
    img1 = uio.Image(url_for('static', filename='vlogo.png'), opt_css_class='centered')
    img2 = uio.Image(url_for('static', filename='hlogo.png'), opt_css_class='centered')
    
    segment = uio.Segment(img1, img2, opt_css_class='basic')
    doc = uio.Document('Fomantic Ui - Image')
    doc.body.append(segment)
    return Markup(doc.get_html())

@app.route('/sidebar')
def load_sidebar():
    sidebar = uio.SideBar()
    sidebar.sidebar_menu.append_inner(
        uio.Image(url_for('static', filename='vlogo.png'), opt_css_class='small centered'),
        uio.MenuHeaderItem('PYSONICE'),
        uio.MenuItem('Admin', 'admin'),
        uio.MenuItem('CRM', 'crm'),
        uio.MenuItem('CUS', 'cus'),
    )
    system_dd = uio.Dropdown('System', css_class='ui dropdown item')
    system_dd.append_inner(
        uio.DropdownMenu(
            uio.DropdownMenuItem('Module', url='module', icon=uio.Icon('tools icon'))
        )
    )
    sidebar.nav_menu.append_inner(
        uio.MenuHeaderItem('FlaskUIO'),
        system_dd,
        uio.MenuItem('Resource'),
        uio.RightMenu(
            uio.MenuItem('Men Sopheak', 'account', uio.Icon('user icon')),
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
        css_class='ui primary inverted large menu custom',
    )
    menu2 = uio.Menu(
        uio.MenuActiveItem('Home', 'home'),
        uio.MenuItem('Message', 'message'),
        uio.MenuItem('Friend', 'friend'),
        uio.RightMenu(
            uio.MenuItem('Men Sopheak', 'account', uio.Icon('user icon')),
            uio.MenuItem('Logout', 'logout', uio.Icon('sign out alternate icon'))    
        ),
        opt_css_class='secondary',
    )
    display_options = uio.DropdownMenu(
        uio.DropdownMenuItem('Text Size', css_class='header'),
        uio.DropdownMenuItem('Small', 'small'),
        uio.DropdownMenuItem('Medium', 'medium'),
        uio.DropdownMenuItem('Large', 'large'),
    )
    menu3 = uio.Menu(
        uio.MenuActiveItem('Account', 'account'),
        uio.MenuItem('Settings', 'setting'),
        uio.Dropdown('Display Options', display_options, css_class='ui dropdown item'),
        opt_css_class='vertical'
    )
    
    segment = uio.Segment(menu2, menu3, opt_css_class='basic')
    doc = uio.Document('Fomantic Ui - Menu')
    doc.body.append(menu1, segment)
    return Markup(doc.get_html())

@app.route('/dropdown')
def load_dropdown():
    dd = uio.Dropdown('File')
    ddi1 = uio.DropdownMenuItem('Publish To Web', icon=uio.Icon('dropdown icon'))
    ddi1.append_inner(
        uio.DropdownMenu(
            uio.DropdownMenuItem('Google Docs', 'http://google.com'),
            uio.DropdownMenuItem('Google Drive'),
            uio.DropdownMenuItem('Dropbox'),
        )
    )
    ddm = uio.DropdownMenu(
        uio.DropdownMenuItem('New'),
        uio.DropdownMenuItem('Open', desc='ctrl + o'),
        uio.DropdownMenuItem('Save as...', desc='ctrl + s'),
        uio.Divider(),
        ddi1,
    )
    dd.append_inner(ddm)
    segment = uio.Segment(dd, opt_css_class='basic')
    doc = uio.Document('Fomantic Ui - Dropdown')
    doc.body.append(segment)
    return Markup(doc.get_html())

@app.route('/card')
def load_card():
    card_group = uio.Cards(
        uio.Card(
            uio.CardImage(url_for('static', filename='python_logo.png')),
            uio.CardContent(
                uio.CardContentHeader('Elliot Fu'),
                uio.CardContentMeta('Friend'),
                uio.CardContentDesc('Elliot Fu is a film-maker from New York.'),
            ),
            uio.CardExtraContent(
                uio.Button('Join Group', btn_type='button')
            )
        ),
        uio.Card(
            uio.CardImage(url_for('static', filename='js.png')),
            uio.CardContent(
                uio.CardContentHeader('Veronika Ossi'),
                uio.CardContentMeta('Friend'),
                uio.CardContentDesc('Veronika Ossi is a set designer living in New York who enjoys kittens, music, and partying.'),
            ),
            uio.CardExtraContent(
                uio.Button('Join Group', btn_type='button')
            )
        ),
        uio.Card(
            uio.CardImage(url_for('static', filename='c#.png')),
            uio.CardContent(
                uio.CardContentHeader('Jenny Hess'),
                uio.CardContentMeta('Friend'),
                uio.CardContentDesc('Jenny is a student studying Media Management at the New School.'),
            ),
            uio.CardExtraContent(
                uio.Button('Join Group', btn_type='button')
            )
        ),
    )
    
    card_group2 = uio.Cards(
        uio.Card(uio.CardImage(url_for('static', filename='python_logo.png')), url='https://www.python.org/'),
        uio.Card(uio.CardImage(url_for('static', filename='js.png'))),
        uio.Card(uio.CardImage(url_for('static', filename='c#.png'))),
        uio.Card(uio.CardImage(url_for('static', filename='python_logo.png'))),
        uio.Card(uio.CardImage(url_for('static', filename='js.png'))),
        uio.Card(uio.CardImage(url_for('static', filename='c#.png'))),
        nb_card=6
    )
    
    segment = uio.Segment(card_group, card_group2, opt_css_class='basic')
    doc = uio.Document('Fomantic Ui - Card')
    doc.body.append(segment)
    return Markup(doc.get_html())

@app.route('/grid')
def load_grid():
    grid1 = uio.Grid()
    grid1.append_inner(uio.GridColumn(nb_wide=4).append_inner(get_card('4 wide column')))
    grid1.append_inner(uio.GridColumn(nb_wide=4).append_inner(get_card('4 wide column')))
    grid1.append_inner(uio.GridColumn(nb_wide=4).append_inner(get_card('4 wide column')))
    grid1.append_inner(uio.GridColumn(nb_wide=4).append_inner(get_card('4 wide column')))
    
    grid2 = uio.Grid()
    grid2.append_inner(uio.GridColumn(get_card('4 wide column'), nb_wide=4))
    grid2.append_inner(uio.GridColumn(get_card('4 wide column'), nb_wide=4))
    grid2.append_inner(uio.GridColumn(get_card('4 wide column'), nb_wide=4))
    grid2.append_inner(uio.GridColumn(get_card('4 wide column'), nb_wide=4))
    grid2.append_inner(uio.GridColumn(get_card('2 wide column'), nb_wide=2))
    grid2.append_inner(uio.GridColumn(get_card('8 wide column'), nb_wide=8))
    grid2.append_inner(uio.GridColumn(get_card('6 wide column'), nb_wide=6))
    
    grid3 = uio.Grid(nb_col=4)
    grid3.append_inner(
        uio.GridRow(
            uio.GridColumn(get_card('column')),
            uio.GridColumn(get_card('column')),
            uio.GridColumn(get_card('column')),
        )
    )
    grid3.append_inner(uio.GridColumn(get_card('column')))
    grid3.append_inner(uio.GridColumn(get_card('column')))
    grid3.append_inner(uio.GridColumn(get_card('column')))
    grid3.append_inner(uio.GridColumn(get_card('column')))
    
    segment = uio.Segment(grid1, grid2, grid3, opt_css_class='basic')
    doc = uio.Document('Fomantic Ui - Grid')
    doc.body.append(segment)
    return Markup(doc.get_html())

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
    message = uio.Message('The transaction is successfully.','success', has_segment=True)
    content = uio.Segment(message, uio.A(url='http://google.com', text='google', target='_blank'), table, opt_css_class='basic')
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
    doc = uio.Document('Fomantic Ui', summernote=True)
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
    color = uio.DropDownField('color', [('Red', 'red'), ('Yellow', 'yellow'), ('Green', 'green')])
    post_date = uio.DateField('post_date', required=True)
    publish_at = uio.DateTimeField('publish_at', required=True)
    is_private = uio.CheckBoxField('is_private')
    submit = uio.Button('Submit', btn_type='button', color='blue')
    modal = uio.ConfirmModal('Confirmation Modal', 'Are you sure to proceed this form?', calling_id=submit.id, form_id=f.id, icon=uio.Icon('delete icon'))
    f.append_inner(
        username,
        password,
        color,
        category,
        post,
        post_date,
        publish_at,
        is_private,
        post_content,
        submit,
        modal,
    )
    segment = uio.Element('div', 'ui segment', inner_elements=[title, f])
    container = uio.Container(segment)
    doc.body.append(container)
    if f.validate_on_submit():
        f.flash_success()
    
    username.data = username.data
    password.data = password.data
    color.data = color.data
    category.data = category.data
    post.data = post.data
    post_content.data = post_content.data
    post_date.data = post_date.data
    publish_at.data = publish_at.data
    is_private.data = is_private.data
    
    return Markup(doc.get_html())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
