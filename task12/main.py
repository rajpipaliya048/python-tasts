from operation import *
from connection import *


selected_db = db_selection()

while True:
    if selected_db == '3':
        break
    operation = menu()
    
    if selected_db == '1':
        if operation == '13':
            print("logging out ....")
            log_out(connection_for_psql())
            selected_db = db_selection()
        elif operation == "1":
            create_database(connection_for_mysql())
        elif operation == '2':
            database = use_database()
            connection_for_mysql(database)
        elif operation == '3':
            database_list(connection_for_mysql(), "SHOW DATABASES")
        elif operation == '4':
            db = input("pleaase enter database name: ")
            tables_list(connection_for_mysql(db), "SHOW TABLES")
        elif operation == '5':
            db = input("pleaase enter database name: ")
            create_table(connection_for_mysql(db))
        elif operation == '6':
            db = input("pleaase enter database name in which table is exist: ")
            add_column(connection_for_mysql(db))
        elif operation == '7':
            db = input("pleaase enter database name in which table is exist: ")
            insert_record(connection_for_mysql(db))
        elif operation == '8':
            db = input("pleaase enter database name in which table is exist: ")
            update_record(connection_for_mysql(db))
        elif operation == '9':
            db = input("pleaase enter database name in which table is exist: ")
            delete_record(connection_for_mysql(db))
        elif operation == '10':
            db = input("pleaase enter database name in which table is exist: ")
            display_table_data(connection_for_mysql(db))
        elif operation == '11':
            db = input("pleaase enter database name in which table is exist: ")
            drop_column(connection_for_mysql(db))
        elif operation == '12':
            db = input("pleaase enter database name in which table is exist: ")
            drop_table(connection_for_mysql(db))

    if selected_db == '2':
        if operation == '13':
            print("logging out ....")
            log_out(connection_for_psql())
            selected_db = db_selection()
        elif operation == "1":
            create_database(connection_for_psql())
        elif operation == '2':
            database = use_database()
            connection_for_psql(database)()
        elif operation == '3':
            database_list(connection_for_psql(), "SELECT datname FROM pg_database WHERE datistemplate = false;")
        elif operation == '4':
            db = input("pleaase enter database name: ")
            tables_list(connection_for_psql(db), "SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
        elif operation == '5':
            db = input("pleaase enter database name: ")
            create_table(connection_for_psql(db))
        elif operation == '6':
            db = input("pleaase enter database name in which table is exist: ")
            add_column(connection_for_psql (db))
        elif operation == '7':
            db = input("pleaase enter database name in which table is exist: ")
            insert_record(connection_for_psql (db))
        elif operation == '8':
            db = input("pleaase enter database name in which table is exist: ")
            update_record(connection_for_psql(db))
        elif operation == '9':
            db = input("pleaase enter database name in which table is exist: ")
            delete_record(connection_for_psql(db))
        elif operation == '10':
            db = input("pleaase enter database name in which table is exist: ")
            display_table_data(connection_for_psql(db))
        elif operation == '11':
            db = input("pleaase enter database name in which table is exist: ")
            drop_column(connection_for_psql(db))
        elif operation == '12':
            db = input("pleaase enter database name in which table is exist: ")
            drop_table(connection_for_psql(db))
