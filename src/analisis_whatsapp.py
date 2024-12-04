from datetime import datetime
import re
import matplotlib.pyplot as plt
from typing import NamedTuple

SO = "android"

ANDROID_RE = r'(\d\d?/\d\d?/\d\d?), (\d\d?:\d\d) - ([^:]+): (.+)'
IOS_RE = r'\[(\d\d?/\d\d?/\d\d?), (\d\d?:\d\d):\d\d\] ([^:]+): (.+)'

Mensaje = NamedTuple('Mensaje', [('fecha', datetime.date), ('hora', datetime.time), ('usuario', str), ('texto', str)])

# Esta función se da implementada
def carga_log(fichero: str, os: str = SO, debug: bool = False) -> list[Mensaje]:
    '''
    Carga un log de Whatsapp, devolviéndolo como lista de tuplas.

    :param fichero: Nombre del fichero del que se quieren leer los datos
    :type fichero: str
    :param os: Tipo de sistema operativo del log, por defecto 'android'
    :type os: str
    :param debug: Indica si se desea obtener información sobre la carga, por defecto False
    :type debug: bool
    :return: Lista de mensajes
    :rtype: list[Mensaje]

    Si el parámetro debug es True se mostrarán los usuarios y el intervalo de 
    fechas procesado. Por ejemplo: 
        3779 mensajes leídos.
        Usuarios: {'Penny', 'Sheldon', 'Howard', 'Raj', 'Lesley', 'Leonard'}
        Intervalo de fechas: 2016-02-25 -> 2017-03-04
    
    La función devuelve una lista de tuplas, cada una de ellas conteniendo la fecha,
    la hora, el usuario y el texto de un mensaje. El orden de las tuplas en la lista
    es el mismo que el que aparece en el fichero, es decir, cronológico.
    '''
    if os=='android':
        regex = ANDROID_RE
    elif os=='ios':
        regex = IOS_RE
    else:
        raise Exception('OS no permitido') # Lanza una excepción
        
    log = []
    with open(fichero, encoding='utf8') as f:        
        for linea in f:
            # Aplicamos la expresión regular sobre cada línea
            matches = re.findall(regex, linea)
            if matches:  # Si se encuentran coincidencias para los patrones
                fecha_str, hora_str, usuario, texto = matches[0]
                fecha = datetime.strptime(fecha_str, '%d/%m/%y').date()
                hora = datetime.strptime(hora_str, '%H:%M').time()
                log.append(Mensaje(fecha,hora,usuario, texto))
            
    return log

def calcula_usuarios(log: list[Mensaje]) -> list[str]:
    '''
    Devuelve una lista ordenada con los usuarios que aparecen en el log, sin duplicados.

    :param log: Lista de mensajes
    :type log: list[Mensaje]
    :return: Lista de usuarios
    :rtype: list[str]
    '''
    pass

def cuenta_mensajes_por_usuario(log: list[Mensaje]) -> dict[str, int]:
    '''
    Devuelve un diccionario en el que las claves son los usuarios y los valores son el número de mensajes de cada usuario.

    :param log: Lista de mensajes
    :type log: list[Mensaje]
    :return: Diccionario de número de mensajes por usuario
    :rtype: dict[str, int]
    '''
    pass

def muestra_numero_mensajes_por_usuario(log: list[Mensaje]) -> None:
    '''
    Muestra una gráfica de barras indicando el número de mensajes por cada usuario.

    :param log: Lista de mensajes
    :type log: list[Mensaje]

    Esta función no retorna ningún valor, pero muestra en pantalla un diagrama de barras
    con el número de mensajes enviados por cada usuario que aparece en el log.
    '''
    # TODO: Construya las listas usuarios y num_mensajes, que contengan
    # respectivamente los usuarios que aparecen en log y el número de 
    # mensajes de cada uno de ellos. Se aconseja que la lista de usuarios
    # aparezca ordenada alfabéticamente
    usuarios = None # TODO
    num_mensajes = None # TODO

    plt.barh(usuarios, num_mensajes)
    plt.show()

def cuenta_mensajes_por_meses(log: list[Mensaje]) -> dict[str, int]:
    '''
    Devuelve un diccionario en el que las claves son los meses a lo largo de los años 
    (por ejemplo, "2/2016", "3/2016",...) y los valores son el número de mensajes de cada mes/año.

    :param log: Lista de mensajes
    :type log: list[Mensaje]
    :return: Diccionario de número de mensajes por mes/año
    :rtype: dict[str, int]
    '''
    pass

def cuenta_mensajes_por_dia_semana(log: list[Mensaje]) -> dict[str, int]:
    '''
    Devuelve un diccionario en el que las claves son los días de la semana 
    ("L", "M", "X", "J", "V", "S" y "D") y los valores son el número de mensajes de cada día.
    Usa el método weekday() del tipo date para determinar el día de la semana.

    :param log: Lista de mensajes
    :type log: list[Mensaje]
    :return: Diccionario de número de mensajes por día de la semana
    :rtype: dict[str, int]
    '''
    pass

def cuenta_mensajes_por_momento_del_dia(log: list[Mensaje]) -> dict[str, int]:
    '''
    Devuelve un diccionario en el que las claves son los momentos del día 
    ("MAÑANA", "TARDE", "NOCHE") y los valores son el número de mensajes de cada momento.
    Los momentos del día se definen como:
    - "MAÑANA": de 7 a 13 horas
    - "TARDE": de 14 a 20 horas
    - "NOCHE": de 21 a 6 horas

    :param log: Lista de mensajes
    :type log: list[Mensaje]
    :return: Diccionario de número de mensajes para cada momento del día
    :rtype: dict[str, int]
    '''
    pass
   
def calcula_media_horas_entre_mensajes(log: list[Mensaje]) -> float:
    '''
    Devuelve la media de horas entre mensajes consecutivos en el tiempo.

    Para combinar una fecha y una hora en un solo objeto datetime, se utiliza la función datetime.combine.
    Para calcular el número de horas entre dos objetos datetime d1 y d2, se utiliza la expresión: 
    (d1-d2).total_seconds() / 3600

    :param log: Lista de mensajes
    :type log: list[Mensaje]
    :return: Media de horas entre mensajes consecutivos
    :rtype: float
    '''
    pass
   
def genera_conteos_palabras_usuario_y_resto(log: list[Mensaje], usuario: str) -> tuple[dict[str, int], dict[str, int]]:
    '''
    Genera dos diccionarios, uno con el conteo de las palabras usadas por el usuario,
    y otro con el conteo de palabras usadas por el resto de usuarios.

    :param log: Lista de mensajes
    :type log: list[Mensaje]
    :param usuario: Usuario específico para el conteo de palabras
    :type usuario: str
    :return: Tupla conteniendo dos diccionarios, uno para el usuario y otro para el resto
    :rtype: tuple[dict[str, int], dict[str, int]]

    Para dividir el texto en palabras, se usa split. Para cada palabra,
    se utiliza la instrucción palabra.strip(".,:();¿?¡!") para eliminar signos de puntuación.
    '''
    pass

def genera_palabras_caracteristicas_usuario(log: list[Mensaje], usuario: str, umbral: int = 2) -> dict[str, float]:
    '''
    Genera un diccionario con la importancia de las palabras usadas por un usuario.

    :param log: Lista de mensajes
    :type log: list[Mensaje]
    :param usuario: Usuario del que se calculará la importancia de las palabras
    :type usuario: str
    :param umbral: Frecuencia mínima para tener en cuenta una palabra, por defecto 2
    :type umbral: int
    :return: Diccionario de importancia de las palabras del usuario
    :rtype: dict[str, float]

    El diccionario contiene palabras con su respectiva importancia, calculada en base 
    a su frecuencia de uso por el usuario indicado, considerando solo aquellas palabras 
    con una frecuencia igual o superior al umbral especificado.
    '''
    pass



