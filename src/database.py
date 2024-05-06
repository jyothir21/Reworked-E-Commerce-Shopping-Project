import os
import sqlite3

# Database class to handle all database operations required
class Database():
    # constructor to create the database
    def __init__(self, reset = False):
        if (reset == True):
            os.remove('customer.db')
            
        self.db = sqlite3.connect('customer.db')
    
    # method to create tables for database
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
    
    # method to set the values in the database from the FakeStoreAPI
    def __setitem__ (self, table, values):
        if (table == "Products"):
            # Unpack the rating dictionary into separate items
            rating = values.pop('rating')
            values.update(rating)

            # Create placeholders and columns strings
            placeholders = ','.join(['?']*len(values))
            columns = ','.join(['PRODUCT_ID', 'PRODUCT_NAME', 'PRODUCT_PRICE', 
                                'PRODUCT_DESC', 'PRODUCT_CAT', 'PRODUCT_IMG', 
                                'PRODUCT_RATING', 'PRODUCT_RATING_COUNT'
                                ])

            # Create the query string
            query = f"INSERT INTO {table}({columns}) VALUES ({placeholders})"

            # Execute the query
            self.db.execute(query, list(values.values()))

        self.db.commit()
    
    # destructor method to close the database
    def __del__(self):
        self.db.close()