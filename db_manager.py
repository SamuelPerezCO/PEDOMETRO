import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'admin_peo',        
    'password': '1234',  
    'database': 'pedometro_db'    
}

def conectar():
    return mysql.connector.connect(**DB_CONFIG)

def inicializar_bd():
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
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT USER();")
    usuario = cursor.fetchone()[0]
    conn.close()
    return usuario
