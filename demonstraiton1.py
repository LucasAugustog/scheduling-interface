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
def job_updateTabela_vendasEmpSegCgoCateg(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)
    end_date = end_date.strftime("%d/%m/%Y")
        
    conn_business1 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness1 = conn_business1.cursor()

    #connection1 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle1 = connection1.cursor()
    
    sql = """select value from integrator_parameter where description like 'Sales'"""
    cursorSQLBusiness1.execute(sql)
    result_sql = cursorSQLBusiness1.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table Vendas Sales...")

        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table  Vendas Sales")


    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : Sales")

    cursorSQLBusiness1.close()
    conn_business1.close()

    #cursorOracle1.close()
    #connection1.close()

#Base quando precisa criar um novo
def job_updateTabela_Integrado5(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)
    end_date = end_date.strftime("%d/%m/%Y")

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
        print(f"⚠ [{now}] [JOB] INactivated : Integrador5")

def job_updateTabela_vendaCheckout(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)
    end_date = end_date.strftime("%d/%m/%Y")

    conn_business2 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness2 = conn_business2.cursor()

    #connection2 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle2 = connection2.cursor()
        
    sql = """select value from integrator_parameter where description like 'Sales Checkouts' """
    cursorSQLBusiness2.execute(sql)
    result_sql = cursorSQLBusiness2.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table Vendas Sales Checkouts...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida
        
        print("Finished collecting for table  Vendas Sales Checkouts")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : Sales Checkouts")

    cursorSQLBusiness2.close()
    conn_business2.close()

    #cursorOracle2.close()
    #connection2.close()

def job_updateTabela_vendaFormaPagamento(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)
    end_date = end_date.strftime("%d/%m/%Y")

    conn_business3 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness3 = conn_business3.cursor()

    #connection3 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle3 = connection3.cursor()

    sql = """select value from integrator_parameter where description like 'Sale Payment Method' """
    cursorSQLBusiness3.execute(sql)
    result_sql = cursorSQLBusiness3.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table Sale Payment Method...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table Sale Payment Method...")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : Sale Payment Method")

    cursorSQLBusiness3.close()
    conn_business3.close()

    #cursorOracle3.close()
    #connection3.close()

def job_updateTabela_auditoriaPdv(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)
    end_date = end_date.strftime("%d/%m/%Y")

    

    conn_business4 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness4 = conn_business4.cursor()

    #connection4 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle4 = connection4.cursor()


    sql = """select value from integrator_parameter where description like 'audit Pdv' """
    cursorSQLBusiness4.execute(sql)
    result_sql = cursorSQLBusiness4.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table audit Pdv...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table audit Pdv")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : audit Pdv")

    
    cursorSQLBusiness4.close()
    conn_business4.close()

    #cursorOracle4.close()
    #connection4.close()

def job_updateTabela_minhaGestaoReposicao(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")  # Corrigido!
    end_date += datetime.timedelta(days=1)  # Usa datetime.timedelta
    end_date = end_date.strftime("%d/%m/%Y")

    conn_business5 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness5 = conn_business5.cursor()

    #connection5 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle5 = connection5.cursor()
        
    sql = """select value from integrator_parameter where description like 'Replacement' """
    cursorSQLBusiness5.execute(sql)
    result_sql = cursorSQLBusiness5.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table Replacement...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table Replacement")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : Replacement")

    cursorSQLBusiness5.close()
    conn_business5.close()

    #cursorOracle5.close()
    #connection5.close()

def job_updateTabela_minhaGestaoAtividade(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y") 
    end_date += datetime.timedelta(days=1) 
    end_date = end_date.strftime("%d/%m/%Y")

    conn_business6 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness6 = conn_business6.cursor()

    #connection6 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle6 = connection6.cursor()



    sql = """select value from integrator_parameter where description like 'Activity' """
    cursorSQLBusiness6.execute(sql)
    result_sql = cursorSQLBusiness6.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table Activity...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table Activity")

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : Activity")

    cursorSQLBusiness6.close()
    conn_business6.close()

    #cursorOracle6.close()
    #connection6.close()

def job_updateTabela_PerdasQuebras(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")

    end_date_dt = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date_dt += datetime.timedelta(days=1)
    end_date = end_date_dt.strftime("%d/%m/%Y")

    start_date2 = datetime.datetime.strptime(start_date, "%d/%m/%Y").strftime("%Y-%m-%d")
    end_date2 = end_date_dt.strftime("%Y-%m-%d")

    conn_business7 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness7 = conn_business7.cursor()

    #connection7 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle7 = connection7.cursor()

    sql = """select value from integrator_parameter where description like 'Losses Breakages' """
    cursorSQLBusiness.execute(sql)
    result_sql = cursorSQLBusiness.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table Losses Breakages... ")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table Losses Breakages")

        if str(integrator_parameter) == "0":
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"⚠ [{now}] [JOB] INactivated : Losses Breakages")

    cursorSQLBusiness7.close()
    conn_business7.close()

    #cursorOracle7.close()
    #connection7.close()

def job_updateTabela_PedidosAprovadosReprovados(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
        
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)  
    end_date = end_date.strftime("%d/%m/%Y")

    conn_business8 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness8 = conn_business8.cursor()

    #connection8 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle8 = connection8.cursor()


    sql = """select value from integrator_parameter where description like 'Requests Approved Rejected' """
    cursorSQLBusiness8.execute(sql)
    result_sql = cursorSQLBusiness8.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table Requests Approved Rejected...")
    
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table Requests Approved Rejected") 
        

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : Requests Approved Rejected")

    cursorSQLBusiness8.close()
    conn_business8.close()

    #cursorOracle8.close()
    #connection8.close()

def job_updateTabela_ProdutosEstoqueAtual(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)
    end_date = end_date.strftime("%d/%m/%Y")

    conn_business9 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness9 = conn_business9.cursor()

    #connection9 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle9 = connection9.cursor()

    sql = """select value from integrator_parameter where description like 'Products StockCurrent' """
    cursorSQLBusiness.execute(sql)
    result_sql = cursorSQLBusiness.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table Products StockCurrent...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table  Products StockCurrent") 
        


    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : Products StockCurrent")

    cursorSQLBusiness9.close()
    conn_business9.close()

    #cursorOracle9.close()
    #connection9.close()

def job_updateTabela_vendas_dia_lojas_simplificado(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)
    end_date = end_date.strftime("%d/%m/%Y")

    conn_business10 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness10 = conn_business10.cursor()

    #connection10 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle10 = connection10.cursor()
            
    sql = """select value from integrator_parameter where description like 'Simplified Sale' """
    cursorSQLBusiness10.execute(sql)
    result_sql = cursorSQLBusiness10.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table Simplified Sale...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table  Simplified Sale") 

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : Simplified Sale")

    cursorSQLBusiness10.close()
    conn_business10.close()

    #cursorOracle10.close()
    #connection10.close()

def job_updateTabela_produtos_por_time(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)
    end_date = end_date.strftime("%d/%m/%Y")

    conn_business11 = mysql.connector.connect(host="localhost", user="root", password="", database="InterfaceJobs")
    cursorSQLBusiness11 = conn_business11.cursor()

    #connection11 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle11 = connection11.cursor()
        
    sql = """select value from integrator_parameter where description like 'product Per Hour' """
    cursorSQLBusiness.execute(sql)
    result_sql = cursorSQLBusiness.fetchall()
    result_sql = str(result_sql).replace("[(", "").replace(",)]", "").replace("'", "")
    integrator_parameter = (result_sql)

    if str(integrator_parameter) == "1":
        print("Starting collection for table product Per Hour...")
        
        #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

        print("Finished collecting for table  product Per Hour") 

    if str(integrator_parameter) == "0":
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"⚠ [{now}] [JOB] INactivated : product Per Hour")

    cursorSQLBusiness11.close()
    conn_business11.close()

    #cursorOracle11.close()
    #connection11.close()

def job_updateTabela_usuariosDjango(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today().strftime("%d/%m/%Y")
    if end_date is None:
        end_date = datetime.date.today().strftime("%d/%m/%Y")
    
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    end_date += datetime.timedelta(days=1)
    end_date = end_date.strftime("%d/%m/%Y")

    #conn_Django12 = mysql.connector.connect(host="", user="", password="", database="django")
    #cursorSQLDjango12 = conn_Django12.cursor()

    #connection12 = oracledb.connect(user="", password="", dsn="")
    #cursorOracle12 = connection12.cursor()



    print("Starting collection for table Users...")
    
    #Lógica da conexão ao banco Oracle e inserção no banco MySQL removida

    print("Finished collecting for table  Users")



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
        elif "⚠️" in string or "INactivated" in string.upper():
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
        self.root.title("Scheduling Interface Python | Tkinter | MySQL | schedule threading |")
        self.root.geometry("1024x720")

        self.style = Style(theme="darkly")
        

        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill='both', expand=True)

        self.Schedulings_salvos = {}
        self.timerios = {}
        self.vars_toggle = {}
        self.executar_buttons = {}
        self.jobs_agendados = {}  # Para rastrear jobs agendados
        self.start_date_entries = {}
        self.end_date_entries = {}

        self.funcoes_jobs = {
            "Sales": job_updateTabela_vendasEmpSegCgoCateg,
            "Sales Checkouts": job_updateTabela_vendaCheckout,
            "Sales Payment Method": job_updateTabela_vendaFormaPagamento,
            "audit Pdv": job_updateTabela_auditoriaPdv,
            "Integrado5": job_updateTabela_Integrado5,
            "Activity": job_updateTabela_minhaGestaoAtividade,
            "Replacement": job_updateTabela_minhaGestaoReposicao,
            "Losses Breakages": job_updateTabela_PerdasQuebras,
            "Requests Approved Rejected": job_updateTabela_PedidosAprovadosReprovados,
            "Products Stock Current": job_updateTabela_ProdutosEstoqueAtual,
            "Simplified Sales": job_updateTabela_vendas_dia_lojas_simplificado,
            "Product Per Hour": job_updateTabela_produtos_por_time,
            "Users": job_updateTabela_usuariosDjango
        }

        abas = ["Sales", "My Management", "Stock", "Products", "Orders", "Audit", "Users"]
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
            
            print("Loading integrator parameters...")
            for id, description, value in resultados:
                if description in self.vars_toggle:
                    self.vars_toggle[description].set(int(value))
                    
                    if description in self.executar_buttons:
                        if int(value) == 1:
                            self.executar_buttons[description].pack(side='right', padx=5)
                        else:
                            self.executar_buttons[description].pack_forget()
                    
                    print(f"✅ Loaded parameter: {description} = {value}")
                else:
                    print(f"⚠️ Parameter not found in interface: {description}")
                    
        except Exception as e:
            print(f"⚠️ Error loading integrator parameters: {e}")

    def carregar_parametros_agendador(self):
        try:
            # Limpar Schedulings existentes
            schedule.clear()
            self.jobs_agendados.clear()
            
            cursorSQLBusiness.execute("""
                SELECT description, scheduling_type, value 
                FROM scheduler_parameter 
            """)
            resultados = cursorSQLBusiness.fetchall()

            # Limpar Listbox
            for listbox in self.timerios.values():
                listbox.delete(0, tk.END)
            for chave in self.Schedulings_salvos:
                self.Schedulings_salvos[chave] = []

            for description, scheduling_type, value in resultados:
                Scheduling = f"{scheduling_type}: {value}"

                # Atualizar interface
                if description in self.timerios:
                    listbox = self.timerios[description]
                    listbox.insert(tk.END, Scheduling)
                    self.Schedulings_salvos[description].append(Scheduling)
                else:
                    print(f"Description '{description}' not found in self.timerios")

                # Agendar execução
                if description in self.funcoes_jobs:
                    funcao = self.funcoes_jobs[description]
                    try:
                        if scheduling_type == "Every hour":
                            try:
                                times = int(value.split(':')[0])
                                minutes = int(value.split(':')[1]) if len(value.split(':')) > 1 else 0
                                seconds = int(value.split(':')[2]) if len(value.split(':')) > 2 else 0
                                
                                interval = times + minutes/60 + seconds/3600
                                if interval <= 0:
                                    print(f"⚠️ invalid interval for '{description}': {value}")
                                    continue
                                    
                                job = schedule.every(interval).hours.do(funcao)
                                self.jobs_agendados[Scheduling] = job
                                print(f"⏱️ Scheduled '{description}' to run every {interval} times.")
                            except ValueError as e:
                                print(f"⚠️ Invalid value for 'Every hour' in '{description}': {value} - {e}")
                                
                        elif scheduling_type == "Fixed Schedule":
                            try:
                                if re.match(r'^\d{1,2}:\d{2}(:\d{2})?$', value):
                                    parts = value.split(':')
                                    time = int(parts[0])
                                    minute = int(parts[1])
                                    second = int(parts[2]) if len(parts) > 2 else 0
                                    
                                    if time < 0 or time > 23 or minute < 0 or minute > 59 or second < 0 or second > 59:
                                        print(f"⚠️ Invalid time for '{description}': {value}")
                                        continue
                                        
                                    job = schedule.every().day.at(value).do(funcao)
                                    self.jobs_agendados[Scheduling] = job
                                    print(f"⏰ Scheduled '{description}' to run every day at {value}.")
                                else:
                                    print(f"⚠️ Invalid time format for '{description}': {value}")
                            except ValueError as e:
                                print(f"⚠️ Error processing Fixed Schedule'{description}': {e}")
                        else:
                            print(f"❌ Scheduling Type unknown to'{description}': {scheduling_type}")
                    except Exception as e:
                        print(f"⚠️ Error when scheduling '{description}': {e}")
                else:
                    print(f"⚠️ Function '{description}' not found in self.funcoes_jobs")

        except mysql.connector.Error as err:
            print(f"Error loading Schedulings from database: {err}")
            
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
            print(f"✅ Scheduling salvo: {description} - {tipo} - {value}")
            
            self.carregar_parametros_agendador()
        except Exception as e:
            print(f"⚠️ Erro ao salvar Scheduling: {e}")

    def delete_scheduler_parameter(self, description, Scheduling_str):
        try:
            parts = Scheduling_str.split(": ")
            if len(parts) == 2:
                tipo = parts[0]
                value = parts[1]
                
                cursorSQLBusiness.execute(
                    "DELETE FROM scheduler_parameter WHERE description = %s AND scheduling_type = %s AND value = %s",
                    (description, tipo, value))
                conn_business.commit()
                
                # Cancelar o job agendado
                if Scheduling_str in self.jobs_agendados:
                    schedule.cancel_job(self.jobs_agendados[Scheduling_str])
                    del self.jobs_agendados[Scheduling_str]
                
                print(f"✅ Scheduling removed: {description} - {tipo} - {value}")
                return True
            return False
        except Exception as e:
            print(f"⚠️ Error removing Scheduling: {e}")
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

        left = ttk.LabelFrame(frame, text="Enable or Disable", width=200)
        left.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        right_container = ttk.Frame(frame)
        right_container.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        right = ttk.LabelFrame(right_container, text="Scheduling", width=400)
        right.pack(fill='both', expand=True, side='left')

        canvas = tk.Canvas(right)
        scrollbar = ttk.Scrollbar(right, orient="vertical", command=canvas.yview)
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
 
        if nome == "Sales":
            variaveis = ["Sales", "Sales Checkouts", "Sales Payment Method", "Simplified Sales"]

        elif nome == "My Management":
            variaveis = ["Activity", "Replacement"]

        elif nome == "Stock":
            variaveis = ["Losses Breakages", "Products StockCurrent"]

        elif nome == "Products":
            variaveis = ["Requests Approved Rejected"] 

        elif nome == "Orders":
            variaveis = ["productPerHour"]  

        elif nome == "Users":
            variaveis = ["Users"]  
        
        elif nome == "Audit":
            variaveis = ["audit Pdv"]        

        else:
            variaveis = ["Integrador1", "Integrador2", "Integrador3", "Integrador4"]

        for var in variaveis:
            if var not in self.Schedulings_salvos:
                self.Schedulings_salvos[var] = []

            frame_toggle = ttk.Frame(left)
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
                text="▶ Run Now!",
                command=lambda v=var: self.forcar_execucao(v),
                bootstyle="info-outline"
            )
            self.executar_buttons[var] = btn_forcar

            self.vars_toggle[var] = var_bool

            Scheduling_frame = ttk.Frame(scrollable_frame)
            Scheduling_frame.pack(fill='x', pady=5, anchor='w')

            label = ttk.Label(Scheduling_frame, text=var)
            label.pack(side='top', anchor='w')

            # Frame para datas
            frame_datas = ttk.Frame(Scheduling_frame)
            frame_datas.pack(fill='x', pady=5)
            
            # Initial data:
            lbl_start_date = ttk.Label(frame_datas, text="Initial data:")
            lbl_start_date.pack(side='left', padx=2)
            
            start_date = ttk.Entry(frame_datas, width=10)
            start_date.insert(0, datetime.date.today().strftime("%d/%m/%Y"))
            start_date.pack(side='left', padx=2)
            self.start_date_entries[var] = start_date
            
            # End Date:
            lbl_end_date = ttk.Label(frame_datas, text="End Date:")
            lbl_end_date.pack(side='left', padx=2)
            
            end_date = ttk.Entry(frame_datas, width=10)
            end_date.insert(0, datetime.date.today().strftime("%d/%m/%Y"))
            end_date.pack(side='left', padx=2)
            self.end_date_entries[var] = end_date

            combo = ttk.Combobox(Scheduling_frame, values=["Every hour", "Fixed Schedule"])
            combo.pack(side='left', padx=5)

            vcmd = (self.root.register(self.validate_time_format), '%P')
            
            entry = ttk.Entry(
                Scheduling_frame, 
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
            self.timerios[var] = listbox

            btn_add = ttk.Button(
                Scheduling_frame, text="To Add",
                command=lambda v=var, c=combo, e=entry: self.adicionar_Scheduling(v, c, e)
            )
            btn_add.pack(side='left', padx=5)

            btn_deletar = ttk.Button(
                Scheduling_frame, text="Delete Selected",
                command=lambda v=var, lb=listbox: self.deletar_Scheduling(v, lb),
                bootstyle="danger-outline"
            )
            btn_deletar.pack(side='left', padx=5)

    def deletar_Scheduling(self, nome_var, listbox):
        selecionado = listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Warning", "No Scheduling selected to delete!")
            return
        
        index = selecionado[0]
        Scheduling = listbox.get(index)
        if self.delete_scheduler_parameter(nome_var, Scheduling):
            listbox.delete(index)
            self.Schedulings_salvos[nome_var].remove(Scheduling)

    def forcar_execucao(self, nome_funcao):
        if nome_funcao in self.funcoes_jobs:
            start_date = self.start_date_entries[nome_funcao].get()
            end_date = self.end_date_entries[nome_funcao].get()
            
            print(f"⚡ Starting forced execution of the job in a separate thread: {nome_funcao}")
            # Criar e iniciar a thread para executar o job
            thread = threading.Thread(target=self.funcoes_jobs[nome_funcao], args=(start_date, end_date), daemon=True)
            thread.start()

    def adicionar_Scheduling(self, nome_var, combo, entry):
        tipo = combo.get()
        value = entry.get()
        
        if not tipo or not value:
            messagebox.showwarning("Warning", "Please fill in all fields!")
            return
            
        # Validação do formato de tempo
        if tipo == "Fixed Schedule":
            if not re.match(r'^\d{1,2}:\d{2}(:\d{2})?$', value):
                messagebox.showwarning("Invalid format", "For Fixed Time, use HH:MM or HH:MM:SS")
                return
            try:
                parts = value.split(':')
                time = int(parts[0])
                minute = int(parts[1])
                second = int(parts[2]) if len(parts) > 2 else 0
                
                if time < 0 or time > 23 or minute < 0 or minute > 59 or second < 0 or second > 59:
                    messagebox.showwarning("Invalid time", "values ​​outside the allowed range (time: 0-23, minute/second: 0-59)")
                    return
            except ValueError:
                messagebox.showwarning("invalid value", "Please enter valid numbers for time, minute and second")
                return
                
        elif tipo == "Every hour":
            if not re.match(r'^\d{1,2}:\d{2}(:\d{2})?$', value):
                messagebox.showwarning("Invalid format", "For 'Every team', use HH:MM:SS")
                return
            try:
                times = int(value.split(':')[0])
                minutes = int(value.split(':')[1]) if len(value.split(':')) > 1 else 0
                seconds = int(value.split(':')[2]) if len(value.split(':')) > 2 else 0
                
                if times == 0 and minutes == 0 and seconds == 0:
                    messagebox.showwarning("Invalid range", "Range cannot be zero")
                    return
            except ValueError:
                messagebox.showwarning("invalid value", "Please enter valid numbers for times, minutes and seconds")
                return

        Scheduling = f"{tipo}: {value}"
        self.timerios[nome_var].insert(tk.END, Scheduling)
        self.Schedulings_salvos[nome_var].append(Scheduling)
        self.salvar_scheduler_parameter(nome_var, tipo, value)
        print(f"✅ Scheduling Adicionado: {Scheduling}")

    def toggle_variavel(self, nome_var, var_bool):
        value = var_bool.get()
        self.salvar_integrator_parameter(nome_var, value)
        
        if nome_var in self.executar_buttons:
            if value == 1:
                self.executar_buttons[nome_var].pack(side='right', padx=5)
                print(f"✔️ {nome_var} activated!")
            else:
                self.executar_buttons[nome_var].pack_forget()
                print(f"❌ {nome_var} deactivated!")

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
        print("✅ Scheduler started in separate thread")

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
            print("✅ Database connections closed")
        except:
            pass
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()