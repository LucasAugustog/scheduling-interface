import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from ttkbootstrap import Style
import sys
import schedule
import threading
import datetime
import time
import mysql.connector
import re
from datetime import timedelta, time as dt_time
import oracledb


# ======================== CONEXOES ========================
#MySQL
conn_business = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
cursorSQLBusiness = conn_business.cursor()

#Oracle
#oracledb.init_oracle_client(lib_dir=r"C:\instantclient_23_4") #WINDOWS
#oracledb.init_oracle_client(config_dir="/opt/instantclient_23_6") #LINUX
#connection = oracledb.connect(user="", password="", dsn="")
#cursorOracle = connection.cursor()


# ======================== JOBS ========================
def job_updateTabela_vendasEmpSegCgoCateg(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)
    data_fim = data_fim.strftime("%d/%m/%Y")
        
    conn_business1 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness1 = conn_business1.cursor()

    #connection1 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle1 = connection1.cursor()
    
    sql = """select value from integrator_parameter where description like 'vendasEmpSegCgoCateg'"""
    cursorSQLBusiness1.execute(sql)
    result_sql = cursorSQLBusiness1.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela Vendas vendasEmpSegCgoCateg...")

        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta para tabela Vendas vendasEmpSegCgoCateg")


    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    cursorSQLBusiness1.close()
    conn_business1.close()

    #cursorOracle1.close()
    #connection1.close()

#Base quando precisa criar um novo
def job_updateTabela_Integrado5(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)
    data_fim = data_fim.strftime("%d/%m/%Y")

    #conn_business = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    #cursorSQLBusiness = conn_business.cursor()

    #connection = oracledb.connect(user="", password="", dsn="")
    #cursorOracle = connection.cursor()
        
    sql = """select value from integrator_parameter where description like 'Integrado5' """
    cursorSQLBusiness.execute(sql)
    result_sql = cursorSQLBusiness.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        teste = 0

        

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

def job_updateTabela_vendaCheckout(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)
    data_fim = data_fim.strftime("%d/%m/%Y")

    conn_business2 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness2 = conn_business2.cursor()

    #connection2 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle2 = connection2.cursor()
        
    sql = """select value from integrator_parameter where description like 'vendaCheckout' """
    cursorSQLBusiness2.execute(sql)
    result_sql = cursorSQLBusiness2.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela Vendas vendaCheckout...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida
        
        print("Finalizado coleta para tabela Vendas vendaCheckout")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    cursorSQLBusiness2.close()
    conn_business2.close()

    #cursorOracle2.close()
    #connection2.close()

def job_updateTabela_vendaFormaPagamento(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)
    data_fim = data_fim.strftime("%d/%m/%Y")

    conn_business3 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness3 = conn_business3.cursor()

    connection3 = oracledb.connect(user="", password="", dsn="")
    cursorOracle3 = connection3.cursor()

    sql = """select value from integrator_parameter where description like 'vendaFormaPagamento' """
    cursorSQLBusiness3.execute(sql)
    result_sql = cursorSQLBusiness3.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela Vendas vendaFormaPagamento...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta para tabela Vendas vendaFormaPagamento...")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    cursorSQLBusiness3.close()
    conn_business3.close()

    #cursorOracle3.close()
    #connection3.close()

def job_updateTabela_auditoriaPdv(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)
    data_fim = data_fim.strftime("%d/%m/%Y")

    

    conn_business4 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness4 = conn_business4.cursor()

    #connection4 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle4 = connection4.cursor()


    sql = """select value from integrator_parameter where description like 'auditoriaPdv' """
    cursorSQLBusiness4.execute(sql)
    result_sql = cursorSQLBusiness4.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela Vendas auditoriaPdv...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta para tabela Vendas auditoriaPdv")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    
    cursorSQLBusiness4.close()
    conn_business4.close()

    #cursorOracle4.close()
    #connection4.close()

def job_updateTabela_minhaGestaoReposicao(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")  # Corrigido!
    data_fim += datetime.timedelta(days=1)  # Usa datetime.timedelta
    data_fim = data_fim.strftime("%d/%m/%Y")

    conn_business5 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness5 = conn_business5.cursor()

    #connection5 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle5 = connection5.cursor()
        
    sql = """select value from integrator_parameter where description like 'Reposição' """
    cursorSQLBusiness5.execute(sql)
    result_sql = cursorSQLBusiness5.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela Minha Gestão Reposição...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta para tabela Minha Gestão Reposição")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    cursorSQLBusiness5.close()
    conn_business5.close()

    #cursorOracle5.close()
    #connection5.close()

def job_updateTabela_minhaGestaoAtividade(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y") 
    data_fim += datetime.timedelta(days=1) 
    data_fim = data_fim.strftime("%d/%m/%Y")

    conn_business6 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness6 = conn_business6.cursor()

    #connection6 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle6 = connection6.cursor()



    sql = """select value from integrator_parameter where description like 'Atividade' """
    cursorSQLBusiness6.execute(sql)
    result_sql = cursorSQLBusiness6.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela Minha Gestão Atividade...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta para tabela Minha Gestão Atividade")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    cursorSQLBusiness6.close()
    conn_business6.close()

    #cursorOracle6.close()
    #connection6.close()

def job_updateTabela_PerdasQuebras(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")

    data_fim_dt = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim_dt += datetime.timedelta(days=1)
    data_fim = data_fim_dt.strftime("%d/%m/%Y")

    data_inicio2 = datetime.datetime.strptime(data_inicio, "%d/%m/%Y").strftime("%Y-%m-%d")
    data_fim2 = data_fim_dt.strftime("%Y-%m-%d")

    conn_business7 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness7 = conn_business7.cursor()

    connection7 = oracledb.connect(user="", password="", dsn="")
    cursorOracle7 = connection7.cursor()

    sql = """select value from integrator_parameter where description like 'PerdasQuebras' """
    cursorSQLBusiness.execute(sql)
    result_sql = cursorSQLBusiness.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela perdas_quebras... ")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta de dados para tabela perdas_quebras")

        if str(integrator_parameter) == "0":
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_PerdasQuebras")

    cursorSQLBusiness7.close()
    conn_business7.close()

    #cursorOracle7.close()
    #connection7.close()

def job_updateTabela_PedidosAprovadosReprovados(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
        
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)  
    data_fim = data_fim.strftime("%d/%m/%Y")

    conn_business8 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness8 = conn_business8.cursor()

    #connection8 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle8 = connection8.cursor()


    sql = """select value from integrator_parameter where description like 'PedidosAprovadosReprovados' """
    cursorSQLBusiness8.execute(sql)
    result_sql = cursorSQLBusiness8.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela pedidos_aprovados_reprovados...")
    
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta de dados para tabela pedidos_aprovados_reprovados") 
        

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    cursorSQLBusiness8.close()
    conn_business8.close()

    #cursorOracle8.close()
    #connection8.close()

def job_updateTabela_ProdutosEstoqueAtual(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)
    data_fim = data_fim.strftime("%d/%m/%Y")

    conn_business9 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness9 = conn_business9.cursor()

    connection9 = oracledb.connect(user="", password="", dsn="")
    cursorOracle9 = connection9.cursor()

    sql = """select value from integrator_parameter where description like 'ProdutosEstoqueAtual' """
    cursorSQLBusiness.execute(sql)
    result_sql = cursorSQLBusiness.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela produtos_estoque_atual...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta de dados para tabela produtos_estoque_atual") 
        


    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    cursorSQLBusiness9.close()
    conn_business9.close()

    #cursorOracle9.close()
    #connection9.close()

def job_updateTabela_vendas_dia_lojas_simplificado(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)
    data_fim = data_fim.strftime("%d/%m/%Y")

    conn_business10 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness10 = conn_business10.cursor()

    connection10 = oracledb.connect(user="", password="", dsn="")
    cursorOracle10 = connection10.cursor()
            
    sql = """select value from integrator_parameter where description like 'VendaSimplificada' """
    cursorSQLBusiness10.execute(sql)
    result_sql = cursorSQLBusiness10.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela vendas_dia_lojas_simplificado...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta de dados para tabela vendas_dia_lojas_simplificado") 

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    cursorSQLBusiness10.close()
    conn_business10.close()

    #cursorOracle10.close()
    #connection10.close()

def job_updateTabela_produtos_por_hora(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)
    data_fim = data_fim.strftime("%d/%m/%Y")

    conn_business11 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness11 = conn_business11.cursor()

    connection11 = oracledb.connect(user="", password="", dsn="")
    cursorOracle11 = connection11.cursor()
        
    sql = """select value from integrator_parameter where description like 'produtoPorHora' """
    cursorSQLBusiness.execute(sql)
    result_sql = cursorSQLBusiness.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Iniciando coleta para tabela produtos_por_hora...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finalizado coleta de dados para tabela produtos_por_hora") 

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INATIVADO : job_updateTabela_vendasEmpSegCgoCateg")

    cursorSQLBusiness11.close()
    conn_business11.close()

    #cursorOracle11.close()
    #connection11.close()

def job_updateTabela_usuariosDjango(data_inicio=None, data_fim=None):
    if data_inicio is None:
        data_inicio = datetime.date.today().strftime("%d/%m/%Y")
    if data_fim is None:
        data_fim = datetime.date.today().strftime("%d/%m/%Y")
    
    data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    data_fim += datetime.timedelta(days=1)
    data_fim = data_fim.strftime("%d/%m/%Y")

    conn_Django12 = mysql.connector.connect(host="", user="", password="", database="django")
    cursorSQLDjango12 = conn_Django12.cursor()

    #connection12 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle12 = connection12.cursor()



    print("Iniciando coleta para tabela usuarios...")
    
    #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

    print("Finalizado coleta de dados para tabela usuarios")



# ======================== REDIRECIONADOR DE TERMINAL ========================

class RedirectTerminal:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.tag_config('green', foreground='green')
        self.text_widget.tag_config('red', foreground='red')
        self.text_widget.tag_config('yellow', foreground='yellow')
        self.text_widget.tag_config('blue', foreground='deep sky blue')

    def write(self, string):
        #CORES
        self.text_widget.configure(state='normal')
        if "ERROR" in string.upper():
            self.text_widget.insert(tk.END, string, 'red')
        elif "⚠️" in string or "INATIVADO" in string.upper():
            self.text_widget.insert(tk.END, string, 'yellow')
        elif "⏱" in string or "⏰" in string: 
            self.text_widget.insert(tk.END, string, 'blue')
        else:
            self.text_widget.insert(tk.END, string, 'green')
        self.text_widget.configure(state='disabled')
        self.text_widget.see(tk.END)

    def flush(self):
        pass

# ======================== INTERFACE ========================
class InterfaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface de Gestão do Integrador do BI")
        self.root.geometry("1024x720")

        self.style = Style(theme="darkly")
        

        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill='both', expand=True)

        self.agendamentos_salvos = {}
        self.horarios = {}
        self.vars_toggle = {}
        self.executar_buttons = {}
        self.jobs_agendados = {}  # Para rastrear jobs agendados
        self.data_inicio_entries = {}
        self.data_fim_entries = {}

        self.funcoes_jobs = {
            "vendasEmpSegCgoCateg": job_updateTabela_vendasEmpSegCgoCateg,
            "vendaCheckout": job_updateTabela_vendaCheckout,
            "vendaFormaPagamento": job_updateTabela_vendaFormaPagamento,
            "auditoriaPdv": job_updateTabela_auditoriaPdv,
            "Integrado5": job_updateTabela_Integrado5,
            "Atividade": job_updateTabela_minhaGestaoAtividade,
            "Reposição": job_updateTabela_minhaGestaoReposicao,
            "PerdasQuebras": job_updateTabela_PerdasQuebras,
            "PedidosAprovadosReprovados": job_updateTabela_PedidosAprovadosReprovados,
            "ProdutosEstoqueAtual": job_updateTabela_ProdutosEstoqueAtual,
            "VendaSimplificada": job_updateTabela_vendas_dia_lojas_simplificado,
            "produtoPorHora": job_updateTabela_produtos_por_hora,
            "Usuarios": job_updateTabela_usuariosDjango
        }

        abas = ["Vendas", "Minha Gestão", "Estoque", "Financeiro", "Produtos", "Pedidos", "Auditoria", "Usuarios"]
        for nome in abas:
            self.criar_aba(nome)

        self.criar_terminal()
        self.carregar_parametros_integrador()
        self.carregar_parametros_agendador()
        self.iniciar_scheduler()

    def carregar_parametros_integrador(self):
        try:
            cursorSQLBusiness.execute("SELECT id, description, value FROM integrator_parameter")
            resultados = cursorSQLBusiness.fetchall()
            
            print("Carregando parâmetros do integrador...")
            for id, description, value in resultados:
                if description in self.vars_toggle:
                    self.vars_toggle[description].set(int(value))
                    
                    if description in self.executar_buttons:
                        if int(value) == 1:
                            self.executar_buttons[description].pack(side='right', padx=5)
                        else:
                            self.executar_buttons[description].pack_forget()
                    
                    print(f"✅ Parâmetro carregado: {description} = {value}")
                else:
                    print(f"⚠️ Parâmetro não encontrado na interface: {description}")
                    
        except Exception as e:
            print(f"⚠️ Erro ao carregar parâmetros do integrador: {e}")

    def carregar_parametros_agendador(self):
        try:
            # Limpar agendamentos existentes
            schedule.clear()
            self.jobs_agendados.clear()
            
            cursorSQLBusiness.execute("""
                SELECT description, scheduling_type, value 
                FROM scheduler_parameter 
            """)
            resultados = cursorSQLBusiness.fetchall()

            # Limpar Listbox
            for listbox in self.horarios.values():
                listbox.delete(0, tk.END)
            for chave in self.agendamentos_salvos:
                self.agendamentos_salvos[chave] = []

            for description, scheduling_type, value in resultados:
                agendamento = f"{scheduling_type}: {value}"

                # Atualizar interface
                if description in self.horarios:
                    listbox = self.horarios[description]
                    listbox.insert(tk.END, agendamento)
                    self.agendamentos_salvos[description].append(agendamento)
                else:
                    print(f"Descrição '{description}' não encontrada em self.horarios")

                # Agendar execução
                if description in self.funcoes_jobs:
                    funcao = self.funcoes_jobs[description]
                    try:
                        if scheduling_type == "A Cada Hora":
                            try:
                                horas = int(value.split(':')[0])  # Pega a parte das horas
                                minutos = int(value.split(':')[1]) if len(value.split(':')) > 1 else 0
                                segundos = int(value.split(':')[2]) if len(value.split(':')) > 2 else 0
                                
                                intervalo = horas + minutos/60 + segundos/3600
                                if intervalo <= 0:
                                    print(f"⚠️ Intervalo inválido para '{description}': {value}")
                                    continue
                                    
                                job = schedule.every(intervalo).hours.do(funcao)
                                self.jobs_agendados[agendamento] = job
                                print(f"⏱️ Agendado '{description}' para rodar a cada {intervalo} horas.")
                            except ValueError as e:
                                print(f"⚠️ value inválido para 'A Cada Hora' em '{description}': {value} - {e}")
                                
                        elif scheduling_type == "Horário Fixo":
                            try:
                                # Verifica se o value está no formato HH:MM ou HH:MM:SS
                                if re.match(r'^\d{1,2}:\d{2}(:\d{2})?$', value):
                                    partes = value.split(':')
                                    hora = int(partes[0])
                                    minuto = int(partes[1])
                                    segundo = int(partes[2]) if len(partes) > 2 else 0
                                    
                                    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 59:
                                        print(f"⚠️ Horário inválido para '{description}': {value}")
                                        continue
                                        
                                    job = schedule.every().day.at(value).do(funcao)
                                    self.jobs_agendados[agendamento] = job
                                    print(f"⏰ Agendado '{description}' para rodar todos os dias às {value}.")
                                else:
                                    print(f"⚠️ Formato de horário inválido para '{description}': {value}")
                            except ValueError as e:
                                print(f"⚠️ Erro ao processar horário fixo '{description}': {e}")
                        else:
                            print(f"❌ Tipo de agendamento desconhecido para '{description}': {scheduling_type}")
                    except Exception as e:
                        print(f"⚠️ Erro ao agendar '{description}': {e}")
                else:
                    print(f"⚠️ Função '{description}' não encontrada em self.funcoes_jobs")

        except mysql.connector.Error as err:
            print(f"Erro ao carregar agendamentos do banco de dados: {err}")
            
    def salvar_integrator_parameter(self, description, value):
        try:
            cursorSQLBusiness.execute("SELECT id FROM integrator_parameter WHERE description = %s", (description,))
            existe = cursorSQLBusiness.fetchone()
            
            if existe:
                cursorSQLBusiness.execute(
                    "UPDATE integrator_parameter SET value = %s WHERE description = %s",
                    (value, description))
            else:
                cursorSQLBusiness.execute(
                    "INSERT INTO integrator_parameter (description, value) VALUES (%s, %s)",
                    (description, value))
            
            conn_business.commit()
            print(f"✅ Parâmetro {description} salvo com value {value}")
        except Exception as e:
            print(f"⚠️ Erro ao salvar parâmetro {description}: {e}")

    def salvar_scheduler_parameter(self, description, tipo, value):
        try:
            cursorSQLBusiness.execute(
                "INSERT INTO scheduler_parameter (description, scheduling_type, value) VALUES (%s, %s, %s)",
                (description, tipo, value))
            conn_business.commit()
            print(f"✅ Agendamento salvo: {description} - {tipo} - {value}")
            
            # Reagendar após salvar
            self.carregar_parametros_agendador()
        except Exception as e:
            print(f"⚠️ Erro ao salvar agendamento: {e}")

    def deletar_scheduler_parameter(self, description, agendamento_str):
        try:
            partes = agendamento_str.split(": ")
            if len(partes) == 2:
                tipo = partes[0]
                value = partes[1]
                
                cursorSQLBusiness.execute(
                    "DELETE FROM scheduler_parameter WHERE description = %s AND scheduling_type = %s AND value = %s",
                    (description, tipo, value))
                conn_business.commit()
                
                # Cancelar o job agendado
                if agendamento_str in self.jobs_agendados:
                    schedule.cancel_job(self.jobs_agendados[agendamento_str])
                    del self.jobs_agendados[agendamento_str]
                
                print(f"✅ Agendamento removido: {description} - {tipo} - {value}")
                return True
            return False
        except Exception as e:
            print(f"⚠️ Erro ao remover agendamento: {e}")
            return False

    def validate_time_format(self, P):
        if P == "":
            return True
        if len(P) > 8:
            return False
        if not re.match(r'^\d{0,2}:?\d{0,2}:?\d{0,2}$', P):
            return False
        if P.count(':') > 2:
            return False
        return True

    def criar_aba(self, nome):
        frame = ttk.Frame(self.tabs)
        self.tabs.add(frame, text=nome)

        esquerda = ttk.LabelFrame(frame, text="Ativar ou Inativar", width=200)
        esquerda.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        direita_container = ttk.Frame(frame)
        direita_container.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        direita = ttk.LabelFrame(direita_container, text="Agendamento", width=400)
        direita.pack(fill='both', expand=True, side='left')

        canvas = tk.Canvas(direita)
        scrollbar = ttk.Scrollbar(direita, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=2)
        frame.grid_rowconfigure(0, weight=1)

        if nome == "Vendas":
            variaveis = ["vendasEmpSegCgoCateg", "vendaCheckout", "vendaFormaPagamento", "VendaSimplificada"]

        elif nome == "Minha Gestão":
            variaveis = ["Atividade", "Reposição"]

        elif nome == "Estoque":
            variaveis = ["PerdasQuebras", "ProdutosEstoqueAtual"]

        elif nome == "Pedidos":
            variaveis = ["PedidosAprovadosReprovados"] 

        elif nome == "Produtos":
            variaveis = ["produtoPorHora"]  

        elif nome == "Usuarios":
            variaveis = ["Usuarios"]  
        
        elif nome == "Auditoria":
            variaveis = ["auditoriaPdv"]        

        else:
            variaveis = ["Integrador1", "Integrador2", "Integrador3", "Integrador4"]

        for var in variaveis:
            if var not in self.agendamentos_salvos:
                self.agendamentos_salvos[var] = []

            frame_toggle = ttk.Frame(esquerda)
            frame_toggle.pack(fill='x', pady=5, anchor='w')

            toggle_frame = ttk.Frame(frame_toggle)
            toggle_frame.pack(side='left', fill='x', expand=True)

            var_bool = tk.IntVar(value=0)
            chk = ttk.Checkbutton(
                toggle_frame,
                text=var,
                variable=var_bool,
                bootstyle="success-round-toggle",
                command=lambda v=var, vb=var_bool: self.toggle_variavel(v, vb)
            )
            chk.pack(side='left', anchor='w')

            btn_forcar = ttk.Button(
                frame_toggle,
                text="▶ Executar Agora!",
                command=lambda v=var: self.forcar_execucao(v),
                bootstyle="info-outline"
            )
            self.executar_buttons[var] = btn_forcar

            self.vars_toggle[var] = var_bool

            agendamento_frame = ttk.Frame(scrollable_frame)
            agendamento_frame.pack(fill='x', pady=5, anchor='w')

            label = ttk.Label(agendamento_frame, text=var)
            label.pack(side='top', anchor='w')

            # Frame para datas
            frame_datas = ttk.Frame(agendamento_frame)
            frame_datas.pack(fill='x', pady=5)
            
            # Data Inicial
            lbl_data_inicio = ttk.Label(frame_datas, text="Data Inicial:")
            lbl_data_inicio.pack(side='left', padx=2)
            
            data_inicio = ttk.Entry(frame_datas, width=10)
            data_inicio.insert(0, datetime.date.today().strftime("%d/%m/%Y"))
            data_inicio.pack(side='left', padx=2)
            self.data_inicio_entries[var] = data_inicio
            
            # Data Final
            lbl_data_fim = ttk.Label(frame_datas, text="Data Final:")
            lbl_data_fim.pack(side='left', padx=2)
            
            data_fim = ttk.Entry(frame_datas, width=10)
            data_fim.insert(0, datetime.date.today().strftime("%d/%m/%Y"))
            data_fim.pack(side='left', padx=2)
            self.data_fim_entries[var] = data_fim

            combo = ttk.Combobox(agendamento_frame, values=["A Cada Hora", "Horário Fixo"])
            combo.pack(side='left', padx=5)

            vcmd = (self.root.register(self.validate_time_format), '%P')
            
            entry = ttk.Entry(
                agendamento_frame, 
                width=10,
                validate="key",
                validatecommand=vcmd
            )
            entry.insert(0, "00:00:00")
            entry.pack(side='left')

            scroll_frame = ttk.Frame(scrollable_frame)
            scroll_frame.pack(fill='x', padx=10, pady=2)

            listbox = tk.Listbox(scroll_frame, height=3)
            listbox.pack(side='left', fill='x', expand=True)

            listbox_scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=listbox.yview)
            listbox_scrollbar.pack(side='right', fill='y')

            

            listbox.config(yscrollcommand=listbox_scrollbar.set)
            self.horarios[var] = listbox

            btn_add = ttk.Button(
                agendamento_frame, text="Adicionar",
                command=lambda v=var, c=combo, e=entry: self.adicionar_agendamento(v, c, e)
            )
            btn_add.pack(side='left', padx=5)

            btn_deletar = ttk.Button(
                agendamento_frame, text="Deletar Selecionado",
                command=lambda v=var, lb=listbox: self.deletar_agendamento(v, lb),
                bootstyle="danger-outline"
            )
            btn_deletar.pack(side='left', padx=5)

    def deletar_agendamento(self, nome_var, listbox):
        selecionado = listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Nenhum agendamento selecionado para deletar!")
            return
        
        index = selecionado[0]
        agendamento = listbox.get(index)
        if self.deletar_scheduler_parameter(nome_var, agendamento):
            listbox.delete(index)
            self.agendamentos_salvos[nome_var].remove(agendamento)

    def forcar_execucao(self, nome_funcao):
        if nome_funcao in self.funcoes_jobs:
            data_inicio = self.data_inicio_entries[nome_funcao].get()
            data_fim = self.data_fim_entries[nome_funcao].get()
            
            print(f"⚡ Iniciando execução forçada do job em thread separada: {nome_funcao}")
            # Criar e iniciar a thread para executar o job
            thread = threading.Thread(target=self.funcoes_jobs[nome_funcao], args=(data_inicio, data_fim), daemon=True)
            thread.start()

    def adicionar_agendamento(self, nome_var, combo, entry):
        tipo = combo.get()
        value = entry.get()
        
        if not tipo or not value:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
            return
            
        # Validação do formato de tempo
        if tipo == "Horário Fixo":
            if not re.match(r'^\d{1,2}:\d{2}(:\d{2})?$', value):
                messagebox.showwarning("Formato inválido", "Para Horário Fixo, use HH:MM ou HH:MM:SS")
                return
            try:
                partes = value.split(':')
                hora = int(partes[0])
                minuto = int(partes[1])
                segundo = int(partes[2]) if len(partes) > 2 else 0
                
                if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 59:
                    messagebox.showwarning("Horário inválido", "valuees fora do intervalo permitido (Hora: 0-23, Minuto/Segundo: 0-59)")
                    return
            except ValueError:
                messagebox.showwarning("value inválido", "Por favor, insira números válidos para hora, minuto e segundo")
                return
                
        elif tipo == "A Cada Hora":
            if not re.match(r'^\d{1,2}:\d{2}(:\d{2})?$', value):
                messagebox.showwarning("Formato inválido", "Para 'A Cada Hora', use HH:MM:SS")
                return
            try:
                horas = int(value.split(':')[0])
                minutos = int(value.split(':')[1]) if len(value.split(':')) > 1 else 0
                segundos = int(value.split(':')[2]) if len(value.split(':')) > 2 else 0
                
                if horas == 0 and minutos == 0 and segundos == 0:
                    messagebox.showwarning("Intervalo inválido", "O intervalo não pode ser zero")
                    return
            except ValueError:
                messagebox.showwarning("value inválido", "Por favor, insira números válidos para horas, minutos e segundos")
                return

        agendamento = f"{tipo}: {value}"
        self.horarios[nome_var].insert(tk.END, agendamento)
        self.agendamentos_salvos[nome_var].append(agendamento)
        self.salvar_scheduler_parameter(nome_var, tipo, value)
        print(f"✅ Agendamento Adicionado: {agendamento}")

    def toggle_variavel(self, nome_var, var_bool):
        value = var_bool.get()
        self.salvar_integrator_parameter(nome_var, value)
        
        if nome_var in self.executar_buttons:
            if value == 1:
                self.executar_buttons[nome_var].pack(side='right', padx=5)
                print(f"✔️ {nome_var} ativado!")
            else:
                self.executar_buttons[nome_var].pack_forget()
                print(f"❌ {nome_var} desativado!")

    def criar_terminal(self):
        terminal_frame = ttk.LabelFrame(self.root, text="Terminal", padding=10)
        terminal_frame.pack(fill='both', expand=True, padx=10, pady=10)

        terminal_text = scrolledtext.ScrolledText(terminal_frame, wrap=tk.WORD, height=10)
        terminal_text.pack(fill='both', expand=True)

        sys.stdout = RedirectTerminal(terminal_text)

    def iniciar_scheduler(self):
        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(1)
                
        # Inicia o scheduler em uma thread separada
        scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        scheduler_thread.start()
        print("✅ Scheduler iniciado em thread separada")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    
    # Configuração para fechar as conexões ao sair
    def on_closing():
        try:
            #cursorSQL.close()
            #conn_mysql.close()
            #connection.close()
            conn_business.close()
            cursorSQLBusiness.close()
            conn_business.close()
            print("✅ Conexões com o banco de dados fechadas")
        except:
            pass
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()