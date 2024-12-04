from wordcloud import WordCloud
from analisis_whatsapp import *
import matplotlib.pyplot as plt

def muestra_word_cloud(log: list[Mensaje], usuario: str, max_words: int = 150) -> None:
    '''
    Muestra una word cloud (nube de palabras) para un usuario específico a partir de un log de mensajes.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :param usuario: Usuario específico para generar la word cloud
    :type usuario: str
    :param max_words: Número máximo de palabras a mostrar en la word cloud, por defecto 150
    :type max_words: int
    '''
    dicc_palabras_caracteristicas = genera_palabras_caracteristicas_usuario(log, usuario)
    wordcloud = WordCloud(
                        font_path='data/seguiemj.ttf',                        
                        background_color='white',
                        width=1800,
                        height=1400,
                        normalize_plurals=False,
                        max_words=max_words
                        ).generate_from_frequencies(dicc_palabras_caracteristicas)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

def grafica_mensajes_por_meses(ax, log):
    mensajes_por_meses = cuenta_mensajes_por_meses(log)
    meses, num_mensajes_por_meses = zip(*mensajes_por_meses.items())
    ax.plot(meses, num_mensajes_por_meses, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)
        
    step = max(1, len(meses) // 10)
    ax.set_xticks(meses[::step])
    ax.set_xticklabels(meses[::step], rotation=60, fontsize=10)
    
    ax.set_title('Evolución mensajes por meses')
    ax.grid(True)

def grafica_mensajes_por_dia_semana(ax, log):
    mensajes_por_dia = cuenta_mensajes_por_dia_semana(log)
    etiquetas_dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
    num_mensajes_por_dias = [mensajes_por_dia[dia] for dia in etiquetas_dias]
    ax.bar(etiquetas_dias, num_mensajes_por_dias, color='g')
    ax.set_title('Mensajes por día de la semana')
    ax.grid(True, axis='y')

def grafica_mensajes_por_momento_del_dia(ax, log):
    mensajes_por_momento = cuenta_mensajes_por_momento_del_dia(log)
    etiquetas_momentos = ["MAÑANA", "TARDE", "NOCHE"]
    num_mensajes_por_momento = [mensajes_por_momento[momento] for momento in etiquetas_momentos]
    ax.bar(etiquetas_momentos, num_mensajes_por_momento, color='r')
    ax.set_title('Mensajes por momento del día')
    ax.grid(True, axis='y')

def genera_informe(log: list[Mensaje], titulo: str = "Informe", usuario: str | None = None) -> None:
    '''
    Muestra un conjunto de gráficas, incluyendo:
     - La evolución del número de mensajes mensualmente.
     - El número de mensajes agregados por día de la semana.
     - El número de mensajes agregados por momento del día.

    Si el parámetro usuario no es None, sólo se usarán los mensajes del usuario indicado 
    para generar el informe.

    :param log: Lista de mensajes
    :type log: List[Mensaje]
    :param titulo: Título del informe, por defecto "Informe"
    :type titulo: str
    :param usuario: Usuario específico para filtrar los mensajes, por defecto None
    :type usuario: Optional[str]
    '''    
    if usuario != None:
        log = [m for m in log if m.usuario == usuario]

    fig, axs = plt.subplots(3, figsize=(10, 15))
    fig.suptitle(titulo+f"\nMedia de horas entre mensajes: {calcula_media_horas_entre_mensajes(log):.2f}", fontsize=16)       
    
    grafica_mensajes_por_meses(axs[0], log)
    grafica_mensajes_por_dia_semana(axs[1], log)
    grafica_mensajes_por_momento_del_dia(axs[2], log)

    plt.tight_layout(rect=[0, 0, 1, 0.96])    
    plt.show()