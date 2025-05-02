import cx_Oracle

def create_connection():
    try:
        dsn = cx_Oracle.makedsn("192.168.0.224", 1521, service_name="ho")
        conn = cx_Oracle.connect(user="perfect", password="perfect", dsn=dsn)
        return conn
    except cx_Oracle.DatabaseError as e:
        raise Exception(f"Database connection failed: {e}")
