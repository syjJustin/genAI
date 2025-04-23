import pandas as pd
from pandasql import sqldf

class ExcelProcessor:
    def __init__(self):
        self.df = None
        self.original_columns = []
    
    def load_excel(self, file_path, sheet_name=0):
        """Load Excel file into DataFrame"""
        self.df = pd.read_excel(file_path, sheet_name=sheet_name)
        self.original_columns = list(self.df.columns)
        return self.df
    
    def query_excel(self, sql_query):
        """Execute SQL query on Excel data"""
        return sqldf(sql_query, {'df': self.df})
