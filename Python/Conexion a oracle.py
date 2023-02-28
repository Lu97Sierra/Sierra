import cx_Oracle

# Conexión a la base de datos Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'XE') 
conn = cx_Oracle.connect(user='SYSTEM', password='867163789', dsn=dsn_tns)

# Ejecutar una consulta
cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()

# Imprimir los resultados
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()