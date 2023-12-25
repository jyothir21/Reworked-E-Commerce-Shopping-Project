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
    
    def __del__(self):
        self.db.close()