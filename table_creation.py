import pyodbc


class Table_create:
    def __init__(self, table_name, column_info):
        self.server = ''
        self.database = 'Airbnb'
        self.username = ''
        self.password = ''
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='
                                   + self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.cnxn.cursor()
        self.table_name = table_name
        self.columns_info = column_info
        self.column_strings = []
        self.table_string = ''
        self.create_database()
        self.set_column_strings()
        self.set_table_string()
        self.create_table()

    def create_database(self):
        self.cursor.execute(f"CREATE DATABASE {self.database}")

    def set_column_strings(self):
        for column in self.columns_info.keys():
            column_string = column
            column_string += ' '
            column_string += self.columns_info[column]['type']

            if 'Primary_Key' in self.columns_info[column].keys():
                column_string += ' IDENTITY PRIMARY KEY NOT NULL'

            elif 'Foreign_Key' in self.columns_info[column].keys():
                column_string += ' FOREIGN KEY REFERENCES '
                column_string += self.columns_info[column]['Foreign_Key']

            elif 'Not_Null' in self.columns_info[column].keys():
                column_string += ' NOT NULL'
            self.column_strings.append(column_string)

    def set_table_string(self):
        self.table_string = 'CREATE TABLE '
        self.table_string += self.table_name
        self.table_string += ' ('
        for column in self.column_strings[:-1]:
            self.table_string += (column + ', ')
        self.table_string += self.column_strings[-1]
        self.table_string += ');'


    def create_table(self):
        self.cursor.execute(self.table_string)
        self.cnxn.commit()









