
Api
******

**Core**
   - :ref:`Element Section`
   - :ref:`Head Section`
   - :ref:`Body Section`
   - :ref:`Html Section`
   - :ref:`Script Section`
   - :ref:`Link Section`
   - :ref:`FieldElement Section`

**Widget**
   - :ref:`Document Section`
   - :ref:`Button Section`
   - :ref:`Card Section`
   - :ref:`Container Section`
   - :ref:`Dropdown Section`
   - :ref:`Divider Section`
   - :ref:`Breadcrumb Section`
   - :ref:`Icon Section`
   - :ref:`Modal Section`
   - :ref:`Image Section`
   - :ref:`Message Section`
   - :ref:`SideBar Section`

**Form Widget**
   - :ref:`Field Section`
   - :ref:`CheckBoxField Section`
   - :ref:`DateField Section`
   - :ref:`DateTimeField Section`
   - :ref:`DropDownField Section`
   - :ref:`QueryDropDownField Section`
   - :ref:`TextField Section`
   - :ref:`TextAreaField Section`
   - :ref:`TextAreaSummernoteField Section`
   - :ref:`UploadField Section`
   - :ref:`Form Section`


.. _Element Section:

Element
=====================
.. autoclass:: flask_uio.element.Element
   :members:


Example 1: Create elements

.. code-block:: python

    >>> from flask_uio import Element
    >>> box1 = Element('div', 'Box 1', _style='background-color: #333;')
    >>> box1.get_html()
    '<div style="background-color: #333;">Box 1</div>'
    >>> a = Element('a', 'Google', _href='http://google.com')
    >>> a.get_html()
    '<a href="http://google.com">Google</a>'

Example 2: Append elements

.. code-block:: python

    html = Element('html', _lang='en')
    head = Element('head')
    head.append(
        Element('title', 'Your Website'),
        Element('meta', _charset='UTF-8'),
        Element('meta', _name='viewport', _content='width=device-width, initial-scale=1.0'),
    )
    html.append(head)
    print(html.get_html())


.. _Head Section:

Head
=====================
.. autoclass:: flask_uio.element.Head
   :members:

.. _Body Section:

Body
=====================
.. autoclass:: flask_uio.element.Body
   :members:

.. _Html Section:

Html
=====================
.. autoclass:: flask_uio.element.Html
   :members:

.. _Script Section:

Script
=====================
.. autoclass:: flask_uio.element.Script
   :members:

.. _Link Section:

Link
=====================
.. autoclass:: flask_uio.element.Link
   :members:

.. _FieldElement Section:

FieldElement
=====================
.. autoclass:: flask_uio.element.FieldElement
   :members:

.. _Document Section:

Document
=====================
.. automodule:: flask_uio.base
   :members:


.. _Button Section:

Button
=====================
.. automodule:: flask_uio.button
   :members:

.. _Card Section:

Card
=====================
.. automodule:: flask_uio.card
   :members:

.. _Container Section:

Container
=====================
.. automodule:: flask_uio.container
   :members:

.. _Dropdown Section:

Dropdown
=====================
.. automodule:: flask_uio.dropdown
   :members:

Example: Create gender dropdown

.. code-block:: python

    d = Dropdown('Gender', 
        DropdownMenu(
            DropdownMenuItem('Male', icon=Element('i', _class='male icon')),
            DropdownMenuItem('Female', icon=Element('i', _class='female icon')),
        ),
    )

    # or use **append(*elements)** 

.. _Divider Section:

Divider
=====================
.. automodule:: flask_uio.divider
   :members:

.. _Breadcrumb Section:

Breadcrumb
=====================
.. automodule:: flask_uio.breadcrumb
   :members:

.. _Icon Section:

Icon
=====================
.. automodule:: flask_uio.icon
   :members:

.. _Modal Section:

Modal
=====================
.. automodule:: flask_uio.modal
   :members:

.. _Image Section:

Image
=====================
.. automodule:: flask_uio.image
   :members:

.. _Message Section:

Message
=====================
.. automodule:: flask_uio.message
   :members:    

.. _Field Section:

Field
=====================
.. autoclass:: flask_uio.field.Field
   :members:

.. _CheckBoxField Section:

CheckBoxField
=====================
.. autoclass:: flask_uio.field.CheckBoxField
   :members:

.. _DateField Section:

DateField
=====================
.. autoclass:: flask_uio.field.DateField
   :members:

.. _DateTimeField Section:

DateTimeField
=====================
.. autoclass:: flask_uio.field.DateTimeField
   :members:

.. _DropDownField Section:

DropDownField
=====================
.. autoclass:: flask_uio.field.DropDownField
   :members:

.. _QueryDropDownField Section:

QueryDropDownField
=====================
.. autoclass:: flask_uio.field.QueryDropDownField
   :members:

.. _TextField Section:

TextField
=====================
.. autoclass:: flask_uio.field.TextField
   :members:

.. _TextAreaField Section:

TextAreaField
=====================
.. autoclass:: flask_uio.field.TextAreaField
   :members:

.. _TextAreaSummernoteField Section:

TextAreaSummernoteField
=======================
.. autoclass:: flask_uio.field.TextAreaSummernoteField
   :members:

.. _UploadField Section:

UploadField
=====================
.. autoclass:: flask_uio.field.UploadField
   :members:

.. _Form Section:

Form
=====================
.. autoclass:: flask_uio.form.Form
   :members:    

.. _SideBar Section:

SideBar
=====================
.. autoclass:: flask_uio.sidebar.SideBar
   :members:    