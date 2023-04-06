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
        
    def add_on_database_new_product(
            self,   
            codigo_de_barras,
            nome,
            valor_custo,
            valor_por_unidade,
            quantidade,       
            estoque_minimo,
            estoque_maximo,
            unidade_de_medida,
            categoria):
        try:
            self.cursor.execute(
                "INSERT INTO Produtos (Codigo_do_produto,"
                    "Nome, Valor_de_custo, Valor_unitario, Quantidade,"
                    "Estoque_minimo,Estoque_maximo, Unidade_de_medida,Categoria)"
                    "VALUES ('" +
                    codigo_de_barras+ "','" +
                    nome+ "','" +
                    valor_custo+ "','" +
                    valor_por_unidade+ "','" +
                    quantidade+ "','" +
                    estoque_minimo+ "', '" +
                    estoque_maximo+ "','" +
                    unidade_de_medida+ "','" +
                    categoria+ "')")

            self.banco.commit()
            return True
        except sqlite3.Error as er:
            return er
        
    def update_item_quantity(self,id, quantidade, nome, quantidade_de_entrada):
        data = self.horario_sys.get_data_sistema()
        horario = self.horario_sys.get_horario_sistema()
        
        self.cursor.execute(
                           f"UPDATE Produtos SET Quantidade='{quantidade}'"
                            f"WHERE Id={id} AND Nome='{nome}'"
)                           
        self.cursor.execute(
                    "INSERT INTO Entrada_prod ( Data,Horario, Id, Produto,Quantidade) "
        f"VALUES ('{data}','{horario}','{id}','{nome}','{quantidade_de_entrada}')")
        self.banco.commit()
        return True
    
    def update_quantidade_estoque_atual(self, nova_quantidade, nome_produto, id_produto):
        self.cursor.execute(
                           f"UPDATE Prod_estoque SET Quantidade_atual='{nova_quantidade}'"
                            f"WHERE Id={id_produto}"
)
        
        self.cursor.execute(
                    f"UPDATE Produtos SET Quantidade='{nova_quantidade}'"
                    f"WHERE Nome='{nome_produto}'"
)
        self.banco.commit()
        return True   
    
    def insert_produtos_vendidos(self, id_produto, nome_do_produto, quantidade_vendida, valor_unitario, valor_venda):
        data = self.horario_sys.get_data_sistema()
        horario = self.horario_sys.get_horario_sistema()
        
        self.cursor.execute(
                    "INSERT INTO Saidas_prod ( Produto,Id_produto,Quantidade_vendida,Preco_unitario, Valor_venda, Horario_venda, Data_venda) "
        f"VALUES ('{nome_do_produto}', '{id_produto}','{quantidade_vendida}','{valor_unitario}','{valor_venda}', '{horario}','{data}')")
        self.banco.commit()
        return True
    
    def update_stock(self,id, quantidade, nome):
        
        self.cursor.execute(
                           f"UPDATE Prod_estoque SET Quantidade_atual='{quantidade}'"
                            f"WHERE Id={id}"
)
        self.cursor.execute(
                           f"UPDATE Produtos SET Quantidade='{quantidade}'"
                            f"WHERE Nome='{nome}'"
)    
    def adicionar_usuario(self, usuario, nome, sobrenome, senha):
        self.cursor.execute(
                    "INSERT INTO Usuarios ( Usuario,Nome,Sobrenome,Senha) "
        f"VALUES ('{usuario}', '{nome}','{sobrenome}','{senha}')")
        self.banco.commit()
        return True
    
    def update_one_part_of_the_product_information(
        self, 
        witch_field_to_update,
        iformation_to_update,
        id_of_product,
        ):
        try:
            self.cursor.execute(
                f"UPDATE Produtos SET '{witch_field_to_update}'='{iformation_to_update}'"
                f"WHERE Id = '{id_of_product}'"
    )    
            self.banco.commit()
            return True
        except sqlite3.Error as er:
            return er
    
    def add_new_unit_of_mesurament(self, name,acronym):
        try:
            self.cursor.execute(
                        "INSERT INTO Unidades_medidas (Nome, Sigla) "
            f"VALUES ('{name}', '{acronym}')")
            self.banco.commit()
            return True
        except sqlite3.Error as er:
            return er
            
if __name__ =='__main__':
    s = AddProducts()
    # print(s.update_item_quantity( 2, 30,'a', 50))
    # print(s.insert_produtos_vendidos(1,'salame', 10, 2, 250))
    # print(s.adicionar_usuario('admin','Admin', 'Sys', '123456'))
    # print(s.add_on_database_new_product('4654864646321', 'Pirulito', '6','15','1','5','10', 'UN', 'DOCES'))
    s.add_new_unit_of_mesurament('s', 'ss')
    # s.a()