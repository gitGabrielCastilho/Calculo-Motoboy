import fdb
import pandas as pd
from tkinter import *
from tkcalendar import Calendar



dst_path = r'MTK:C:/Microsys/MsysIndustrial/Dados/MSYSDADOS.FDB'



TABLE_NAME = 'CARREGAMENTO'
SELECT = 'select CAR_NUMERO, CAR_KMVALOR, CAR_KMTOTAL, CAR_FRETEVALOR, CAR_DATA, CAR_MOTORISTA ' \
         'from %s WHERE CAR_KMVALOR  > 0 ORDER BY CAR_DATA' % TABLE_NAME

con = fdb.connect(dsn=dst_path, user='SYSDBA', password='masterkey', charset='UTF8')

cur = con.cursor()
cur.execute(SELECT)

table_rows = cur.fetchall()

df = pd.DataFrame(table_rows)

################################################################################################
root = Tk()

# Set geometry
root.geometry()

# Add Calendar
cal = Calendar(root, selectmode='day', date_patternstr='dd/mm/yy')

cal.grid(padx=30, pady=(15,0), columnspan=3)

def grad_date1():
    date1.config(text= cal.get_date())

def grad_date2():
    date2.config(text= cal.get_date())

def calcula():

    for nome in df.loc[5]:
        if nome == "GUALTER":
            l = str(date1.cget("text"))
            k = str(date2.cget("text"))
            x = df.loc[(df[4] >= l) & (df[4] <= k)]
            df_sum = str(sum(x[2]))
            h.config(text="R$" + df_sum)
        else:
            pass


Button(root, text="Escolha Primeira Data", command=grad_date1 ).grid(row=2, pady=10)
date1 = Label(root, text="")
date1.grid(pady=10, row=3)
###################################################################################################
Button(root, text="Escolha Segunda Data", command=grad_date2).grid(row=2, column=2)
date2 = Label(root, text="")
date2.grid(pady=10, column=2, row=3)
###################################################################################################
Button(root, text="Calcule Custo", command=calcula).grid(row=4,pady=10, columnspan=3)
h = Label(root, text="")
h.grid(row=5, pady=10, columnspan=3)

root.mainloop()



