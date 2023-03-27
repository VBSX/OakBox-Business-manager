import sqlite3
import os       



class AddProducts():
    def __init__(self):
        local_path = os.path.abspath('database')
  
        database_path =local_path+'\\'+'banco.db'
        print(database_path,'\n\n')
        self.banco = sqlite3.connect(database_path)
        self.cursor = self.banco.cursor()
        
        

        
    def add_on_database_new_product(self, nome, quantidade, valor_unidade):
        qnt_now = '0'
        self.cursor.execute(
                
                "INSERT INTO Produtos ( Nome, Quantidade, Valor_unitario) "
                "VALUES ('" +nome+ "','" +quantidade+ "', '" +valor_unidade+ "')")
        
        self.cursor.execute(
                            "INSERT INTO Prod_estoque ( Produtos, Quantidade, Quantidade_atual) "
                "VALUES ('" +nome+ "','" +qnt_now+ "', '" +qnt_now+ "')")

        self.banco.commit()
        return True
        
        

    
    
if __name__ =='__main__':
    s = AddProducts()
    print(s.add_on_database_new_product('a', '2', '13'))