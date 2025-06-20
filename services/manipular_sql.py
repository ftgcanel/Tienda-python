import mysql.connector
def manipular(consulta_sql, parametros=None):
    config = {
        'user': 'uhddz0ye6dmcybf8',
        'password': 'hnlhh6NxR5ZmI22Y0CDP',
        'host': 'bo6ldsjwsu31ht7uqveu-mysql.services.clever-cloud.com',
        'database': 'bo6ldsjwsu31ht7uqveu',
        'raise_on_warnings': True
    }

    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()

        # Ejecutar con o sin parámetros
        if parametros:
            cursor.execute(consulta_sql, parametros)
        else:
            cursor.execute(consulta_sql)

        # Si es una consulta SELECT, obtener resultados
        if consulta_sql.strip().lower().startswith("select"):
            resultado = cursor.fetchall()
        else:
            # Para INSERT, UPDATE, DELETE: confirmar cambios
            conexion.commit()
            resultado = cursor.rowcount  # Devuelve cantidad de filas afectadas

        cursor.close()
        conexion.close()
        return resultado

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
