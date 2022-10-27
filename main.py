import fdb
import pandas as pd
from tkinter import *
from tkcalendar import Calendar


def relatorio():
    dst_path = r'MTK:C:/Microsys/MsysIndustrial/Dados/MSYSDADOS.FDB'



    TABLE_NAME = 'CARREGAMENTO'
    SELECT = 'select CAR_NUMERO, CAR_KMVALOR, CAR_KMTOTAL, CAR_FRETEVALOR, CAR_DATA, CAR_MOTORISTA from %s ' \
             'WHERE CAR_KMVALOR  > 0 ORDER BY CAR_DATA' % TABLE_NAME

    con = fdb.connect(dsn=dst_path, user='SYSDBA', password='masterkey', charset='UTF8')

    cur = con.cursor()
    cur.execute(SELECT)

    table_rows = cur.fetchall()
#
    df = pd.DataFrame(table_rows)

################################################################################################
    root = Tk()

    # Set geometry
    root.geometry("400x500")

    # Add Calendar
    cal = Calendar(root, selectmode='day', date_patternstr = 'd/m/yy')

    cal.pack(pady=20)

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
                print(x.head(5))
                print("*" * 70)
                h.config(text="R$" + df_sum)
            else:
                pass


    Button(root, text="Escolha Primeira Data", command=grad_date1).pack(pady=10)
    date1 = Label(root, text="")
    date1.pack(pady=10)

    Button(root, text="Escolha Segunda Data", command=grad_date2).pack(pady=10)
    date2 = Label(root, text="")
    date2.pack(pady=10)

################################################################################################

    Button(root, text="Calcule Custo", command=calcula).pack(pady=10)
    h = Label(root, text="")
    h.pack(pady=10)

    root.mainloop()
################################################################################################
relatorio()

