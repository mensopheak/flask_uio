from .table_col_item import TableColItem
from .prop import ValidProp

class TableStaticLinkItem(TableColItem):
    fp_col_name = ValidProp(str)
    
    def __init__(self, name, db_column=None, is_hidden=False, default_sort=False, default_sort_asc=False, fp_col_name=None):
        super().__init__(name, db_column, allow_search=False, is_hidden=is_hidden, default_sort=default_sort, default_sort_asc=default_sort_asc)
        self.fp_col_name = fp_col_name
        
    
    