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
    
    def get_all_info_of_product(self, product_id, name_of_product, find_by_id,find_by_name):
        if find_by_id == True:
            self.cursor.execute(
                f"SELECT * FROM Produtos WHERE Id = '{product_id}'")
            data_database = self.cursor.fetchall()

            return data_database
        elif find_by_name == True:
            self.cursor.execute(
                f"SELECT * FROM Produtos WHERE Nome LIKE '%{name_of_product}%'")
            data_database = self.cursor.fetchall()

            return data_database
        
      
    def get_products_by_id(self, id_of_product):
        
        self.cursor.execute(
            f"SELECT Id, Nome, Quantidade, Valor_unitario, Unidade_de_medida,Categoria from PRodutos WHERE Id = '{id_of_product}'")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_products_by_name(self, name_of_product):
        self.cursor.execute(
            f"SELECT Id, Nome, Quantidade, Valor_unitario, Unidade_de_medida,Categoria FROM Produtos WHERE Nome LIKE '%{name_of_product}%'")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_product_by_id_and_name(self, id_of_product,name_of_product):
        self.cursor.execute(
            f"SELECT Id, Nome, Quantidade, Valor_unitario, Unidade_de_medida,Categoria, Estoque_minimo, Estoque_maximo FROM Produtos WHERE Id = '{id_of_product}'AND Nome LIKE '%{name_of_product}%'")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_product_by_exact_name(self,name_of_product):
        self.cursor.execute(
            f"SELECT Id, Nome, Quantidade, Valor_unitario, Unidade_de_medida,Categoria FROM Produtos WHERE Nome = '{name_of_product}'")
        data_database = self.cursor.fetchall()

        return data_database
    
    
    def get_price_of_product(self, name_of_product, id):
        self.cursor.execute(
            f"SELECT Valor_unitario FROM Produtos WHERE Nome = '{name_of_product}' AND Id = '{id}'")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_product_quatity(self,  name_of_product, id):
        self.cursor.execute(
            f"SELECT Quantidade FROM Produtos WHERE Nome = '{name_of_product}' AND Id = '{id}'")
        data_database = self.cursor.fetchall()

        return data_database[0][0]
    
    def get_password_by_user(self, user):
        self.cursor.execute(
            f"SELECT Senha FROM Usuarios WHERE Usuario = '{user}'")
        data_database = self.cursor.fetchall()
        return data_database
    
    def get_user_info(self, user):
        self.cursor.execute(
            f"SELECT Id, Usuario,Nome,Sobrenome FROM Usuarios WHERE Usuario = '{user}'")
        data_database = self.cursor.fetchall()
        return data_database

    def get_all_products(self):
        self.cursor.execute(
            "SELECT Id, Nome, Quantidade, Valor_unitario, Unidade_de_medida,Categoria, Estoque_minimo, Estoque_maximo FROM Produtos")
        data_database = self.cursor.fetchall()
        
        return data_database

    def get_some_data_by_id_and_name_from_products_table(self, id_of_product,name_of_product, wich_colum_to_take):
        self.cursor.execute(
            f"SELECT {wich_colum_to_take} FROM Produtos WHERE Nome = '{name_of_product}' AND Id = '{id_of_product}'")
        data_database = self.cursor.fetchall()

        return data_database[0][0]

    def get_all_info_of_all_products(self):
        
        self.cursor.execute(
            f"SELECT * FROM Produtos")
        data_database = self.cursor.fetchall()
        
        return data_database
    
    def get_all_unity_of_mesurament_name(self):
        self.cursor.execute(
            f"SELECT Nome FROM Unidades_medidas")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_all_unity_of_mesurament_acronym(self):
        self.cursor.execute(
            f"SELECT Sigla FROM Unidades_medidas")
        data_database = self.cursor.fetchall()

        return data_database
    def get_all_unity_of_mesurament_info(self):
        self.cursor.execute(
            f"SELECT * FROM Unidades_medidas")
        data_database = self.cursor.fetchall()

        return data_database
        
    def get_all_category(self):
        self.cursor.execute(
            f"SELECT Nome FROM Categorias")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_especific_unity_by_name(self, name):
        self.cursor.execute(
            f"SELECT Nome FROM Unidades_medidas WHERE Nome = '{name}'")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_especific_unity_by_acronym(self,acronym):
        self.cursor.execute(
            f"SELECT Sigla FROM Unidades_medidas WHERE Sigla = '{acronym}'")
        data_database = self.cursor.fetchall()

        return data_database
    
    def get_category_by_name(self, name):
        self.cursor.execute(
            f"SELECT Nome FROM Categorias WHERE Nome = '{name}'")
        data_database = self.cursor.fetchall()

        return data_database
    
if __name__ =='__main__':
    s = ProductsData()
    # print(s.get_all_products())
    # print(s.get_some_data_by_id_and_name_from_products_table(1, 'pudim', 'Valor_de_custo'))
    # print(type(s.get_product_quatity('pudim', 1)))
    # print(s.get_products_of_stock_by_name('salame'))
    # print(s.get_product_quatity('salame', 11))
    # print(s.get_all_products())
    # print(s.get_all_unity_of_mesurament_info())
    # print(s.get_especific_unity_by_name('UNIDADE'))
    print(s.get_all_category())
    
