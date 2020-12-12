============
Basic Usage
============

To get started, create a **Document** and add some Elements to it. 
By default, the Document will use `Fomantic-UI <https://fomantic-ui.com/>`_ 
(css framework) for styling elements::

    from flask import Flask, Markup
    import flask_uio as uio

    app = Flask(__name__)
    flaskuio = uio.FlaskUIO(app)

    @app.route('/')
    def index():
        # build content
        header = uio.Element('h1', _class='ui primary header', inner_text='FlaskUIO')
        paragraph = uio.Element('p', 'Build user interface with FlaskUIO\'s element.')
        container = uio.Container(_class='ui container')
        container.append(header, paragraph)

        # create document and append content to it
        doc = uio.Document('FlaskUIO')
        doc.body.append(container)
        return Markup(doc.get_html())

    if __name__ == '__main__':
        app.run(debug=True)


