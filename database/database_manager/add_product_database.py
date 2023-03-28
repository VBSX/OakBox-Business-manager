import sqlite3
import os       
import sys
path = os.path.abspath('env_get')
sys.path.append(path)
from consulta_horario_sys import HorarioDoSistema

class AddProducts():
    def __init__(self):
        local_path = os.path.abspath('database')
  
        database_path =local_path+'\\'+'banco.db'
        print(database_path,'\n\n')
        self.banco = sqlite3.connect(database_path)
        self.cursor = self.banco.cursor()
        self.horario_sys = HorarioDoSistema()
        
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
        
    def update_item_quantity(self,id, quantidade, nome, quantidade_de_entrada):
        data = self.horario_sys.get_data_sistema()
        horario = self.horario_sys.get_horario_sistema()
        
        self.cursor.execute(
                           f"UPDATE Prod_estoque SET Quantidade_atual='{quantidade}'"
                            f"WHERE Id={id}"
)
        self.cursor.execute(
                           f"UPDATE Produtos SET Quantidade='{quantidade}'"
                            f"WHERE Nome='{nome}'"
)
                            
                            
        self.cursor.execute(
                    "INSERT INTO Entrada_prod ( Data,Horario, Id, Produto,Quantidade) "
        f"VALUES ('{data}','{horario}','{id}','{nome}', '{quantidade_de_entrada}')")


        self.banco.commit()
        return True
if __name__ =='__main__':
    s = AddProducts()
    print(s.update_item_quantity( 2, 30,'a'))
    # s.a()