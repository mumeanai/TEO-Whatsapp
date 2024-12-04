from analisis_whatsapp import *

# Sustituye por la ruta de tu propio log, si quieres
FICHERO = 'data/bigbangtheory_es.txt' 

def test_carga_log() -> list[Mensaje]:
    print("---> Test de carga_log:")
    mensajes = carga_log(FICHERO)
    print(f"{len(mensajes)} mensajes leídos.")
    print("Usuarios:", {m.usuario for m in mensajes})
    fecha_minima = min(m.fecha for m in mensajes)
    fecha_maxima = max(m.fecha for m in mensajes)
    print(f"Intervalo de fechas: {fecha_minima} -> {fecha_maxima}")
    print("Mostrando los 5 primeros mensajes:")
    for m in mensajes[:5]:
        print("\t", m)
    print("="*40)
    print()
    # Devolvemos los mensajes leídos para usarlos en el resto de los tests
    return mensajes 

def test_calcula_usuarios(mensajes: list[Mensaje]) -> None:
    print("---> Test de cuenta_mensajes_por_usuario:")
    print("Los usuarios del log son:", calcula_usuarios(mensajes))
    print("="*40)
    print()

def test_cuenta_mensajes_por_usuario(mensajes: list[Mensaje]) -> None:
    print("---> Test de cuenta_mensajes_por_usuario:")
    numero_mensajes_por_usuario = cuenta_mensajes_por_usuario(mensajes)
    for usuario, numero_mensajes in sorted(numero_mensajes_por_usuario.items()):
        print(f"{usuario}: {numero_mensajes}")        
    print("="*40)
    print()

def test_muestra_numero_mensajes_por_usuario(mensajes: list[Mensaje]) -> None:
    print("---> Test de muestra_numero_mensajes_por_usuario:")
    muestra_numero_mensajes_por_usuario(mensajes)
    print("="*40)
    print()

def test_cuenta_mensajes_por_meses(mensajes: list[Mensaje]) -> None:
    print("---> Test de cuenta_mensajes_por_meses:")
    numero_mensajes_por_meses = cuenta_mensajes_por_meses(mensajes)
    for mes, numero_mensajes in sorted(numero_mensajes_por_meses.items()):
        print(f"{mes}: {numero_mensajes}")        
    print("="*40)
    print()

def test_cuenta_mensajes_por_dia_semana(mensajes: list[Mensaje]) -> None:
    print("---> Test de cuenta_mensajes_por_dia_semana:")
    numero_mensajes_por_dias = cuenta_mensajes_por_dia_semana(mensajes)
    for dia in ["L", "M", "X", "J", "V", "S", "D"]:
        print(f"{dia}: {numero_mensajes_por_dias[dia]}")        
    print("="*40)
    print()

def test_cuenta_mensajes_por_momento_del_dia(mensajes: list[Mensaje]) -> None:
    print("---> Test de cuenta_mensajes_por_momento_del_dia:")
    numero_mensajes_por_momento = cuenta_mensajes_por_momento_del_dia(mensajes)
    for momento, numero_mensajes in numero_mensajes_por_momento.items():
        print(f"{momento}: {numero_mensajes}")        
    print("="*40)
    print()


def test_calcula_media_horas_entre_mensajes(mensajes: list[Mensaje]) -> None:
    print("---> Test de calcula_media_horas_entre_mensajes:")
    print(f"La media de horas entre mensajes consecutivos es", 
          calcula_media_horas_entre_mensajes(mensajes))
    print("="*40)
    print()

def test_genera_conteos_palabras_usuario_y_resto(mensajes: list[Mensaje]) -> None:
    print("---> Test de genera_conteos_palabras_usuario_y_resto:")
    usuario = mensajes[0].usuario
    conteo_usuario, conteo_resto = genera_conteos_palabras_usuario_y_resto(mensajes, usuario)    
    for palabra in list(conteo_usuario)[:10]:
        print(f'La palabra "{palabra}" fue usada\n\t{conteo_usuario[palabra]} veces por {usuario} y\n\t{conteo_resto[palabra] if palabra in conteo_resto else 0} veces por el resto.\n')
    print("="*40)
    print()

def test_genera_palabras_caracteristicas_usuario(mensajes: list[Mensaje]) -> None:
    print("---> Test de genera_palabras_caracteristicas_usuario:")
    usuario = mensajes[0].usuario
    importancia_usuario = genera_palabras_caracteristicas_usuario(mensajes, usuario)
    print('Usuario:', usuario)
    for palabra, importancia in sorted(importancia_usuario.items(), key=lambda t:t[1], reverse=True)[:10]:
            print('   ',palabra,'->',importancia)
    print("="*40)
    print()


if __name__ == '__main__':
    mensajes = test_carga_log()
    test_calcula_usuarios(mensajes)
    test_cuenta_mensajes_por_usuario(mensajes)
    test_muestra_numero_mensajes_por_usuario(mensajes)
    test_cuenta_mensajes_por_meses(mensajes)
    test_cuenta_mensajes_por_dia_semana(mensajes)    
    test_cuenta_mensajes_por_momento_del_dia(mensajes)
    test_calcula_media_horas_entre_mensajes(mensajes)
    test_genera_conteos_palabras_usuario_y_resto(mensajes)
    test_genera_palabras_caracteristicas_usuario(mensajes)
    