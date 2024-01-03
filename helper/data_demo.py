import sqlite3 

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
            CREATE TABLE Users (
            CID INTEGER PRIMARY KEY NOT NULL,
            manzil varchar(255)
        );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, cid: int):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"
        try:
            sql = """
            INSERT INTO Users(CID,manzil) VALUES(?,?)
            """
            self.execute(sql, parameters=(cid,"home"), commit=True)
        except:
            print("Error 1")
    
    def get_location(self,cid):
        x = self.execute(f"SELECT * FROM users WHERE cid={cid}",fetchone=True)
        return x[1]


    def add_location(self, cid: int, manzil: str):
        sql = """ 
        UPDATE Users SET manzil=? WHERE cid=?
        """
        return self.execute(sql, parameters=(manzil, cid), commit=True)
        
    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)


    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")




import sqlite3 

class Database_gr:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
            CREATE TABLE Users (
            CID INTEGER PRIMARY KEY NOT NULL,
            manzil varchar(255)
        );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, cid: int):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"
        try:
            sql = """
            INSERT INTO Users(CID,manzil) VALUES(?,?)
            """
            self.execute(sql, parameters=(cid,"home"), commit=True)
        except:
            print("Error 1")
    
    def get_location(self,cid):
        x = self.execute(f"SELECT * FROM users WHERE cid={cid}",fetchone=True)
        return x[1]


    def add_location(self, cid: int, manzil: str):
        sql = """ 
        UPDATE Users SET manzil=? WHERE cid=?
        """
        return self.execute(sql, parameters=(manzil, cid), commit=True)
        
    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)


    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
