import mysql.connector
def conectar(consulta_sql):

# Credenciales para la conexión

    config = {
'user': 'uhddz0ye6dmcybf8',
'password': 'hnlhh6NxR5ZmI22Y0CDP',
'host': 'bo6ldsjwsu31ht7uqveu-mysql.services.clever-cloud.com',
'database': 'bo6ldsjwsu31ht7uqveu',
'raise_on_warnings': True
}
# Conectar a la base de datos
    try:
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")

        # Objeto para crear consultas
        consulta = conexion.cursor()

        # función para agregar la consulta SQL
        consulta.execute(consulta_sql)

        # Almacenamos el resultado de la consulta SLQ
        resultado = consulta.fetchall()

        return resultado

# Respuesta si al conectar da error
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")

