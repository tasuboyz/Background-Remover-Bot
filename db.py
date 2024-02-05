import sqlite3

class Database():
    def __init__(self):
        self.conn = sqlite3.connect('rembg.db')
        self.c = self.conn.cursor()            
        self.user_file = 'USER_FILE'
        self.user_info = 'USER'
    pass
        
    def create_table(self):
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.user_info} (user_id INTEGER PRIMARY KEY, username TEXT)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS COLOR (user_id INTEGER PRIMARY KEY, color TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.user_file} (user_id INTEGER PRIMARY KEY, file_name TEXT)''')
        self.conn.commit()
        return

    def insert_user_data(self, user_id, username):
        self.c.execute(f"INSERT OR REPLACE INTO {self.user_info} (user_id, username) VALUES (?, ?)", (user_id, username))
        self.conn.commit()
    
    def save_image(self, user_id, file_name):
        self.c.execute(f'''INSERT OR REPLACE INTO {self.user_file} (user_id, file_name) VALUES (?, ?) ''', (user_id, file_name))
        self.conn.commit()
        
    def get_image(self, user_id):
        self.c.execute(f'''SELECT file_name FROM {self.user_file} WHERE user_id = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        return result[0] if result else (None)
    
    def get_user_by_image(self, file_name):
        self.c.execute(f'''SELECT user_id FROM {self.user_file} WHERE file_name = ?''', (file_name,))
        result = self.c.fetchone()
        self.conn.commit()
        return result[0] if result else (None)
    
    def delate_image(self, user_id):
        self.c.execute(f"DELETE FROM {self.user_file} WHERE user_id = ?", (user_id,)) 
        self.conn.commit()
                        
    def get_color_from_data(self, user_id):
        self.c.execute('''SELECT color FROM COLOR WHERE user_id = ?''', (user_id,))
        row = self.c.fetchone()
        self.conn.commit()
        if row is not None:
            return row[0]
        else:
            return None  # o qualsiasi valore predefinito
    
    def save_color_in_settings(self, user_id, color): # crea un metodo per salvare il colore nelle impostazioni dell'utente
        self.c.execute('''INSERT OR REPLACE INTO COLOR (user_id, color) VALUES (?, ?)''',
                        (user_id, color))
        self.conn.commit()
        return
    
    def delate_colors(self, user_id): # crea un metodo per scrivere il QR con i colori appropriati
        self.c.execute("DELETE FROM COLOR WHERE user_id = ?", (user_id,)) 
        self.conn.commit()
        return
            
    def count_users(self):
        self.c.execute(f"SELECT COUNT(user_id) FROM {self.user_info}")
        row_count = self.c.fetchone()[0]
        return row_count
    
    def write_ids(self):
        self.c.execute(f"SELECT user_id FROM {self.user_info}")
        results = self.c.fetchall()
        with open('ids.txt', 'w') as file:
            for result in results:
                file.write(str(result[0]) + '\n')
        self.conn.commit()


