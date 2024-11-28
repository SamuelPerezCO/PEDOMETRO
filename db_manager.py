import mysql.connector

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'user': 'admin_peo',        
    'password': '1234',  
    'database': 'pedometro_db'    
}

def conectar():
    """
    Establece una conexión con la base de datos utilizando las configuraciones definidas.

    Returns:
        mysql.connector.connect: Conexión a la base de datos.
    """
    return mysql.connector.connect(**DB_CONFIG)

def inicializar_bd():
    """
    Inicializa la base de datos creando la tabla 'peo_contadores' si no existe.

    Esta función crea la tabla 'peo_contadores' en la base de datos con las columnas 
    para almacenar los contadores de peos del día, semana, mes y año.
    Si la tabla ya existe, no realiza ninguna acción.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS peo_contadores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        peos_dia INT DEFAULT 0,
        peos_semana INT DEFAULT 0,
        peos_mes INT DEFAULT 0,
        peos_ano INT DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

def obtener_peo_contadores():
    """
    Obtiene los contadores de peos desde la base de datos.

    Si los contadores no existen, inserta un nuevo registro con los valores por defecto 
    (todos en cero).

    Returns:
        dict: Diccionario con los contadores de peos (peos_dia, peos_semana, peos_mes, peos_ano).
    """
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT peos_dia, peos_semana, peos_mes, peos_ano FROM peo_contadores WHERE id = 1')
    datos = cursor.fetchone()

    if not datos:
        # Si no hay datos, inserta el primer registro
        cursor.execute('''INSERT INTO peo_contadores (peos_dia, peos_semana, peos_mes, peos_ano)
                          VALUES (0, 0, 0, 0)''')
        conn.commit()
        datos = {'peos_dia': 0, 'peos_semana': 0, 'peos_mes': 0, 'peos_ano': 0}

    conn.close()
    return datos

def actualizar_peo_contadores(peos_dia, peos_semana, peos_mes, peos_ano):
    """
    Actualiza los contadores de peos en la base de datos.

    Si el registro de la tabla 'peo_contadores' con id = 1 no existe, se crea un nuevo registro. 
    Si el registro ya existe, se actualizan los valores de los contadores.

    Args:
        peos_dia (int): Contador de peos del día.
        peos_semana (int): Contador de peos de la semana.
        peos_mes (int): Contador de peos del mes.
        peos_ano (int): Contador de peos del año.
    """
    conn = conectar()
    cursor = conn.cursor()

    # Verifica si el registro con id = 1 existe, si no lo inserta
    cursor.execute('SELECT id FROM peo_contadores WHERE id = 1')
    if not cursor.fetchone():
        cursor.execute('''INSERT INTO peo_contadores (peos_dia, peos_semana, peos_mes, peos_ano)
                          VALUES (%s, %s, %s, %s)''', (peos_dia, peos_semana, peos_mes, peos_ano))
    else:
        # Si existe, actualiza
        query = """
        UPDATE peo_contadores
        SET peos_dia = %s, peos_semana = %s, peos_mes = %s, peos_ano = %s
        WHERE id = 1
        """
        cursor.execute(query, (peos_dia, peos_semana, peos_mes, peos_ano))

    conn.commit()
    conn.close()

def obtener_usuario_actual():
    """
    Obtiene el usuario actual conectado a la base de datos.

    Returns:
        str: Nombre del usuario conectado a la base de datos.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT USER();")
    usuario = cursor.fetchone()[0]
    conn.close()
    return usuario
