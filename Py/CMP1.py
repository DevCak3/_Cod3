import requests

def obtener_enlaces_videos_pagina(access_token, pagina_id):
    url_base = f'https://graph.facebook.com/v12.0/concejodepasto/videos'
    parametros = {
        'access_token': access_token,
        'fields': 'id,title,source',
        'limit': 1000   # Puedes ajustar esto según tus necesidades
    }

    enlaces_videos = []

    while True:
        respuesta = requests.get(url_base, params=parametros)
        datos = respuesta.json()

        if 'data' not in datos:
            break

        for video in datos['data']:
            if 'description' in video:
                enlaces_videos.append(video['source'])

        if 'paging' in datos and 'next' in datos['paging']:
            parametros['after'] = datos['paging']['cursors']['after']
        else:
            break

    return enlaces_videos

if __name__ == "__main__":
    # Reemplaza con tu token de acceso, ID de la página y palabra clave
    token_acceso = "EAAEJy5FE2c4BO0vveyBp4nAGVzfedwETUBZBOiKSTVbLfI0ePYOK6rk82YDlmhAN6TtZBAj64J3ZCZBqZBfzagEu9uVvuZCpoOAUVr498aoeQz9wUor2H8WfZCBrGqVZA7krpl1XlQJbphggWtZBWiPSRu5kXToECEapgmZCvmXhnYHnbq8zX6Ef3zgyOLFQygMxrrrsNGdaoUdN35hBUnYaxgLrQ2sOVYZBIcZAJpi22hGd1wZDZD"
    id_pagina = "concejodepasto"

    enlaces = obtener_enlaces_videos_pagina(token_acceso, id_pagina)

    print("Enlaces de videos encontrados:")
    for enlace in enlaces:
        print(enlace)    