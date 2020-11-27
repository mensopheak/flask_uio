from .table_col_item import TableColItem
from .prop import ValidProp
from flask import current_app
from datetime import datetime

class TableDateItem(TableColItem):
    format = ValidProp(str)
    display_format = ValidProp(str)
    
    def __init__(self, name, db_column=None, is_hidden=False, format=None, display_format=None, default_sort=False, default_sort_asc=False):
        super().__init__(name, db_column, allow_search=False, is_hidden=is_hidden, default_sort=default_sort, default_sort_asc=default_sort_asc)
        self.format = format or current_app.config['FLASK_UIO_DATE_FORMAT']
        self.display_format = display_format or current_app.config['FLASK_UIO_DATE_DISPLAY_FORMAT']
        
    def get_value(self, date_string):
        if not isinstance(date_string, str):
            raise ValueError(f'date string must be a string type.')
        return datetime.strptime(date_string, self.format).date()
    
    def get_text(self, date):
        if type(date) not in (datetime.date, datetime):
            raise ValueError(f'date string must be a date type.')
        return datetime.strftime(date, self.display_format)
    
    