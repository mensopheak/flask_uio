from .prop import ValidProp
from sqlalchemy.orm.attributes import InstrumentedAttribute

class TableColItem:
    name = ValidProp(str)
    allow_search = ValidProp(bool)
    is_key=ValidProp(bool)
    is_hidden=ValidProp(bool)
    default_sort=ValidProp(bool)
    default_sort_asc=ValidProp(bool)
    
    def __init__(self, name, column=None, allow_search=True, is_key=False, is_hidden=False, default_sort=False, default_sort_asc=False):
        self.name = name
        self.column = column
        self.allow_search = allow_search
        self.is_key = is_key
        self.is_hidden = is_hidden
        self.default_sort = default_sort
        self.default_sort_asc = default_sort_asc
        
    @property
    def column(self):
        return getattr(self, '_column', None)
    
    @column.setter
    def column(self, value):
        if value is not None:
            if type(value) is not InstrumentedAttribute:
                raise ValueError('sort column must be a type of InstrumentedAttribute.')
        setattr(self, '_column', value)
    
    @property
    def friendly_name(self):
        return self.name.replace('_', ' ').title()
    
    def __repr__(self):
        return f"ColItem(name='{self.name}', column={self.column}, allow_search={self.allow_search})"