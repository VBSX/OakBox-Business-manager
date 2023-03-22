
import sqlite3
import os       



class ProductsData():
    def __init__(self):
        local_path = os.path.abspath('database')
        print(local_path)
        database_path =local_path+'\\'+'banco.db'
        print(database_path,'\n\n')
        self.banco = sqlite3.connect(database_path)
        self.cursor = self.banco.cursor()
        
        

        
    def get_products_by_id(self, id_of_product):
        
        self.cursor.execute(
            f"SELECT Id,Nome,Quantidade, Valor_unitario FROM Produtos WHERE Id = '{id_of_product}'")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_products_by_name(self, name_of_product):
        self.cursor.execute(
            f"SELECT Id,Nome,Quantidade, Valor_unitario FROM Produtos WHERE Nome LIKE '%{name_of_product}%'")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_product_by_id_and_name(self, id_of_product,name_of_product):
        self.cursor.execute(
            f"SELECT Id,Nome,Quantidade, Valor_unitario FROM Produtos WHERE Id = '{id_of_product}'AND Nome LIKE '%{name_of_product}%'")
        data_database = self.cursor.fetchall()

        return data_database
if __name__ =='__main__':
    s = ProductsData()
    print(s.get_products_by_id(3))