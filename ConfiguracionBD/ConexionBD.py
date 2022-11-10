from IPython.display import display
import oracledb
class ConexionBD:


    def __init__(self, user, password, port, dsn):
        self.user = user
        self.password = password
        self.port = port
        self.dsn = dsn

        try:

            self.conexion = oracledb.connect(user=self.user, password=self.password, dsn=self.dsn)
            # con=cx_Oracle.connect(user="GHCT",password="auto_333",
            #             dsn="melideo.claro.amx:1521/ARTCCARD")
            # print("Conexion a BD exitosa")
        except Exception as error:
            print("Error al intentar conectarse a la BD. Error: " + str(error))
            self.close()

    def ejecutarSelect(self, sql):
        cur = self.conexion.cursor()
        try:
            cur.execute(sql)
            datos = cur.fetchall()
            cur.close()
            return datos
        except Exception as error:
            cur.close()
            print("Error al intentar realizar el select. Error: " + str(error))

    def close(self):
        self.conexion.close()


def step_impl():
    conex = ConexionBD(user='EXB35249', password='Matias12', port='1521',
                       dsn='sascmt04.claro.amx/TSASCM')

    registro = conex.ejecutarSelect("""select campaign, country, offer_code, treatment, start_date, end_date
                                     from AR_aux.OFFERS_MATRIX 
                                     where offer_code in ('cluster_cr_hu_sp', 'cluster_cr_mi_sp', 'cluster_cr_li_sp')""")


    display(registro[0])
    display(registro[1])
    display(registro[2])


step_impl()