import os
import sqlite3

class Database():
    def __init__(self, reset = False):
        if (reset == True):
            os.remove('customer.db')
            
        self.db = sqlite3.connect('customer.db')
        
    def create_tables(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS Products
                            ( PRODUCT_ID    INTEGER NOT NULL,
                              PRODUCT_NAME  VARCHAR(100) NOT NULL,
                              PRODUCT_PRICE DECIMAL(6,2) NOT NULL,
                              PRODUCT_DESC  VARCHAR(1000),
                              PRODUCT_CAT   VARCHAR(100) NOT NULL,
                              PRODUCT_IMG   VARCHAR(1000) NOT NULL,
                              PRODUCT_RATING DECIMAL(2,1) NOT NULL,
                              PRODUCT_RATING_COUNT DECIMAL(7,0) NOT NULL,
                              PRIMARY KEY (PRODUCT_ID)
                            );
                        """)
        
        self.db.commit()
        
    def __setitem__ (self, table, values):
        if (table == "Products"):
            placeholders = ','.join(['?']*len(values))
            columns = ','.join(['PRODUCT_ID', 'PRODUCT_NAME', 'PRODUCT_PRICE', 
                                'PRODUCT_DESC', 'PRODUCT_CAT', 'PRODUCT_IMG', 
                                'PRODUCT_RATING', 'PRODUCT_RATING_COUNT'
                                ])
            query = f"INSERT INTO {table}({columns}) VALUES ({placeholders})"
            self.db.execute("""
                            """)
    
    def __del__(self):
        self.db.close()