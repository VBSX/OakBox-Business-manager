
from consulta_horario_sys import HorarioDoSistema
import sqlite3



class EnvioBanco:
    def __init__(self, nome_produto, nome_da_loja):
        self.nome_produto = nome_produto
        self.nome_da_loja = nome_da_loja
        self.sys_date = HorarioDoSistema()
        self.data_agora = self.sys_date.get_data_sistema()
        self.hora_agora = self.sys_date.get_horario_sistema()
        self.banco = sqlite3.connect('banco.db')
        self.cursor = self.banco.cursor()

    def fechar_banco(self):
        self.banco.close()

    def send_dados_para_o_banco_tabela_dos_precos(self, preco_atual):
        try:
            self.preco_atual = preco_atual
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS valores_dos_sites (produto text, cotacao text, loja text, "
                "data_consulta numeric, hora_consulta numeric) ")
            self.cursor.execute(
                "INSERT INTO valores_dos_sites (produto, cotacao, loja, data_consulta, hora_consulta) "
                "VALUES ('" + self.nome_produto + "','" + self.preco_atual + "', '" + self.nome_da_loja + "', '" +
                self.data_agora + "', '" + self.hora_agora + "')")
            self.banco.commit()
            self.fechar_banco()
            
            return print('\ndados cadastrados no banco;')

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
            
            return erro

    def send_dados_tabela_cadastro_de_produtos(self, id_do_produto, link_do_produto):
        self.link_do_produto = link_do_produto
        self.id_do_produto = id_do_produto
        try:
            self.cursor.execute(
                "INSERT INTO dados_dos_sites (id_cadastro, produto, url, loja) values "
                "('" + self.id_do_produto + "', '" + self.nome_produto + "', '" +
                self.link_do_produto + "', '" + self.nome_da_loja + "')")
            self.banco.commit()
            self.fechar_banco()
            
        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
            
            return erro
