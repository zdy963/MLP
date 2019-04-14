import quandl
from fetch_data.conn import dbconn
from sqlalchemy import create_engine

col_names = ['FRED/GDP', 'FRED/GDPC1', 'FRED/GDPPOT', 'FRED/CPIAUCSL', 'FRED/CPILFESL', 'FRED/GDPDEF', 'FRED/BASE',
                'FRED/M1', 'FRED/M2', 'FRED/M1V', 'FRED/M2V', 'FRED/DFF', 'FRED/DTB3', 'FRED/DGS5', 'FRED/DGS10',
                'FRED/DGS30', 'FRED/T5YIE', 'FRED/T10YIE', 'FRED/T5YIFR', 'FRED/TEDRATE', 'FRED/DPRIME', 'FRED/UNRATE',
                'FRED/NROU', 'FRED/NROUST', 'FRED/CIVPART', 'FRED/EMRATIO', 'FRED/UNEMPLOY', 'FRED/PAYEMS',
                'FRED/MANEMP', 'FRED/ICSA', 'FRED/IC4WSA', 'FRED/MEHOINUSA672N', 'FRED/DSPIC96', 'FRED/PCE',
                'FRED/PCEDG', 'FRED/PSAVERT', 'FRED/RRSFS', 'FRED/DSPI', 'FRED/INDPRO', 'FRED/TCU', 'FRED/HOUST',
                'FRED/GPDI', 'FRED/CP', 'FRED/STLFSI', 'FRED/DCOILWTICO', 'FRED/USSLIND', 'FRED/DTWEXM', 'FRED/DTWEXB',
                'FRED/GFDEBTN', 'FRED/GFDEGDQ188S', 'FRED/EXCSRESNW', 'FRED/TOTCI']


def init_update():
    quandl.ApiConfig.api_key = "-a9RmMjaPBg-phm3w83Y"
    mysql_conn = create_engine("mysql+mysqldb://root:admin@119.29.53.97:3306/mlp").connect()

    for col in col_names:
        print('Fetching: ',col)
        data = quandl.get(col)
        data = data.reset_index()
        data['Date'] = data['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        data['Value'] = data['Value'].apply(lambda x: str(x))
        data.to_sql(name=col, con=mysql_conn, if_exists='replace', index=False)

        newest_date = data['Date'].iloc[-1]
        print(newest_date)
        with dbconn() as db:
            print("Saving to database")
            cursor = db.cursor()
            sql = """INSERT INTO NEWEST_DATE (NAME, DATE) VALUES ('{}','{}') 
                ON DUPLICATE KEY UPDATE DATE='{}';""".format(col, newest_date, newest_date)

            cursor.execute(sql)
            db.commit()


def main():
    quandl.ApiConfig.api_key = "-a9RmMjaPBg-phm3w83Y"
    mysql_conn = create_engine("mysql+mysqldb://root:admin@119.29.53.97:3306/mlp").connect()

    for col in col_names:
        # Get the newest date
        with dbconn() as db:
            cursor = db.cursor()
            cursor.execute("SELECT DATE FROM NEWEST_DATE WHERE NAME='{}'".format(col))
            newest_id = cursor.fetchone()['DATE']
        print('Fetching: ',col)
        data = quandl.get(col, start_date=newest_id)
        if len(data) > 1:
            data = data.reset_index()
            data['Date'] = data['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            data['Value'] = data['Value'].apply(lambda x: str(x))
            data.to_sql(name=col, con=mysql_conn, if_exists='append', index=False)

            newest_date = data['Date'].iloc[-1]
            print(newest_date)
            with dbconn() as db:
                print("Saving to database")
                cursor = db.cursor()
                sql = """INSERT INTO NEWEST_DATE (NAME, DATE) VALUES ('{}','{}') 
                    ON DUPLICATE KEY UPDATE DATE='{}';""".format(col, newest_date, newest_date)

                cursor.execute(sql)
                db.commit()
        else:
            print("Nothing new")


if __name__ == '__main__':
    while True:
        main()