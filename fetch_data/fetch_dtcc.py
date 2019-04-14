import os
from datetime import datetime
from fetch_data.conn import dbconn
import zipfile
import pandas as pd
from numpy import nan
from urllib import request, error
from sqlalchemy import create_engine

swap_list = ("Commodity:Energy:Oil:Swap:Cash", "Commodity:Metals:NonPrecious:Swap:Cash",
             "Commodity:Metals:NonPrecious:SpotFwd:Physical", "Commodity:Metals:Precious:SpotFwd:Physical",
             "Commodity:Index:Swap:Cash", "Commodity:Agricultural:Softs:Swap:Cash",
             "Commodity:Agricultural:Dairy:Swap:Cash", "Commodity:Agricultural:GrainsOilSeeds:Swap:Cash",
             "Commodity:MultiCommodityExotic", "Commodity:Energy:Elec:Swap:Cash", "Commodity:Energy:NatGas:Swap:Cash",
             "Commodity:Agricultural:Livestock:Swap:Cash", "Commodity:Metals:Precious:Swap:Cash",
             "Commodity:Energy:Coal:Swap:Cash", "Commodity:Energy:InterEnergy:Swap:Cash",
             "Commodity:Environmental:Emissions:SpotFwd:Physical", "Commodity:Energy:NatGas:SpotFwd:Physical",
             "Commodity:Agricultural:GrainsOilSeeds:SpotFwd:Physical", "Commodity:Freight:Swap:Cash",
             "Commodity:Agricultural:Forestry:Swap:Cash", "Commodity:Energy:Elec:SpotFwd:Physical",
             "Commodity:Energy:Elec:SpotFwd:Physical", "Commodity:Environmental:Weather:Swap:Cash",
             "Commodity:Agricultural:Softs:SpotFwd:Physical", "Commodity:Energy:Coal:SpotFwd:Physical",
             "Commodity:Metals:Precious:LoanLease:Cash", "Commodity:Agricultural:Livestock:SpotFwd:Physical",
             "Commodity:Metals:Precious:LoanLease:Physical")


def unzip(f_path):
    print("Unzipping file")
    zip_file = zipfile.ZipFile(f_path, 'r')
    for name in zip_file.namelist():
        zip_file.extract(name, 'zip_files/')
        # extract_csv(name)

    zip_file.close()
    print("Removing zip file")
    os.remove(f_path)


def sdr_fetch(url):
    print("Fetching data")
    f_name = url.split('/')[-1]
    csv_name = '_'.join(f_name.split('_')[1:])
    csv_name = csv_name.split('.')[0] + '.csv'
    print(csv_name)
    if os.path.exists('zip_files/' + csv_name):
        print("Skipping")
    else:
        save_path = 'zip_files/' + f_name
        with request.urlopen(url) as zip:
            print("downloading data")
            with open(save_path, 'wb') as outfile:
                outfile.write(zip.read())
        unzip(save_path)


def get_utc():
    return datetime.utcnow().strftime('%Y_%m_%d')


def fetch_record(date, index):
    while True:
        try:
            index += 1
            print("Fetching %d record" % index)
            sdr_fetch(
                "https://kgc0418-tdw-data2-0.s3.amazonaws.com/slices/SLICE_COMMODITIES_{}_{}.zip".format(date, index))
            print()
        except error.HTTPError:
            # Update newest date to
            print(index)
            date = date + '_' + str(index - 1)
            with dbconn() as db:
                print("Saving stop point to database", date)
                cursor = db.cursor()
                sql = """INSERT INTO NEWEST_DATE (NAME, DATE) VALUES ('dtcc','{}') 
                        ON DUPLICATE KEY UPDATE DATE='{}';""".format(date, date)
                cursor.execute(sql)
                db.commit()
            break


def get_colname(table_name):
    with dbconn() as db:
        cursor = db.cursor()
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name='{}' and table_schema='mlp'".format(
            table_name)
        cursor.execute(sql)
        names = cursor.fetchall()
        for i in range(len(names)):
            names[i] = names[i]['COLUMN_NAME']

        return names


def main():
    # Get newest date from database
    with dbconn() as db:
        cursor = db.cursor()
        cursor.execute("SELECT DATE FROM NEWEST_DATE WHERE NAME='dtcc'")
        newest_id = cursor.fetchone()

    if newest_id is None:
        print("No data from newest date")
        date = str(datetime.today().strftime('%Y_%m_%d'))
        index = 0
        print(newest_id)
    else:
        newest_id = newest_id['DATE'].split('_')
        date = '_'.join(newest_id[:-1])
        index = int(newest_id[-1])
        print("Reading from stop point!", index)

    utc = get_utc()

    # Fetching the newest record of this date
    fetch_record(date, index)

    # Coming to a new date
    if utc != date:
        print("Having new date info")
        fetch_record(utc, 0)

    df = pd.DataFrame()
    print("Reading csv and combining them together")

    name_list = os.listdir('zip_files/')
    for f_name in name_list:
        if f_name.endswith('csv'):
            csv = pd.read_csv('zip_files/' + f_name, index_col=False)
            df = df.append(csv)
            os.remove('zip_files/' + f_name)

    # df = pd.read_csv('full.csv', index_col=False)
    if len(df) > 0:
        print("Uploading to database")
        # mysql_conn = create_engine("mysql+mysqldb://root:admin@119.29.53.97:3306/mlp").connect()
        # df.to_sql(name='dtcc', con=mysql_conn, if_exists='append', index=False)

        df = df.replace(nan, ' ', regex=True)
        df_swap = df[df['TAXONOMY'].str.contains('Exotic|Option') == False]
        df_swap.drop_duplicates(['TAXONOMY'], keep='last', inplace=True)

        df_option = df[df['TAXONOMY'].str.contains('Exotic|Option')]
        df_option.drop_duplicates(['TAXONOMY'], keep='last', inplace=True)

        with dbconn() as db:
            cursor = db.cursor()
            if len(df_swap) > 0:
                table_name = 'COM/SWAP'
                col_name = get_colname(table_name)
                col_str = "{}".format(','.join(col_name))
                for i in range(0, len(df_swap)):
                    value_str = "{}".format(','.join(
                        ['%r' % df_swap.iloc[i][name] if type(df_swap.iloc[i][name]) != float else str(round(
                            df_swap.iloc[i][name], 4)) for name in col_name]))
                    print(value_str)
                    # print("Updating Commodities swap", date)
                    sql = """REPLACE INTO `{}` ({}) VALUES ({});""".format(table_name, col_str, value_str)
                    print(sql)
                    cursor.execute(sql)

            if len(df_option) > 0:
                table_name = 'COM/OPTION'
                col_name = get_colname(table_name)
                col_str = "{}".format(','.join(col_name))
                for i in range(0, len(df_option)):
                    value_str = "{}".format(','.join(
                        ['%r' % df_option.iloc[i][name] for name in col_name]))
                    print(value_str)
                    # print("Updating Commodities swap", date)
                    sql = """REPLACE INTO `{}` ({}) VALUES ({});""".format(table_name, col_str, value_str)
                    print(sql)
                    cursor.execute(sql)
            db.commit()

    else:
        print("Already newest")


if __name__ == '__main__':
    while True:
        main()
