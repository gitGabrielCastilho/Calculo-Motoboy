import fdb
import pandas as pd
from tkinter import *
from tkcalendar import Calendar


def relatorio():

    TABLE_NAME = 'CARREGAMENTO'
    SELECT = 'select CAR_NUMERO, CAR_KMVALOR, CAR_KMTOTAL, CAR_FRETEVALOR, CAR_DATA from %s ' \
             'WHERE CAR_KMVALOR  > 0 ORDER BY CAR_DATA' % TABLE_NAME

    con = fdb.connect(dsn=r'C:\Users\Gabriel\Desktop\MSYSDADOS.FDB', user='SYSDBA', password='masterkey',
                      charset='UTF8')

    cur = con.cursor()
    cur.execute(SELECT)

    table_rows = cur.fetchall()
#
    df = pd.DataFrame(table_rows)
    print(df.head(5))
    print('*' * 70)

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

        l = str(date1.cget("text"))
        k = str(date2.cget("text"))

        x = df.loc[(df[4] >= l) & (df[4] < k)]

        df_sum = str(sum(x[2]))

        print(x.head(5))

        print("*" * 70)

        h.config(text="R$" + df_sum)


    # Add Button and Label
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

    # Execute Tkinter
    root.mainloop()
################################################################################################
relatorio()

