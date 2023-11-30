import requests

def obtener_info_invocador(nombre_invocador):
    url_base = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    url_base_games = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/"
    clave_api = "RGAPI-02d2fcb4-18a6-4f05-a78b-5f00c759b457"
    url_invocador = f"{url_base}{nombre_invocador}"

    headers = {"X-Riot-Token": clave_api}

    respuesta = requests.get(url_invocador, headers=headers)

    if respuesta.status_code == 200:
        datos_invocador = respuesta.json()
        print("Información del Invocador:")
        print(f"Nombre: {datos_invocador['name']}")
       
        encrypt_id = datos_invocador['id']
        url_games = f"{url_base_games}{encrypt_id}"
        response = requests.get(url_games, headers=headers)

        if response.status_code == 200:
            matchlist_data = response.json()
            for queue_data in  matchlist_data:
                queue_type = queue_data["queueType"]
                wins = queue_data["wins"]
                losses = queue_data["losses"]
                total_games = wins + losses

                if total_games > 0:
                    winrate = (wins / total_games) * 100
                    print(f"{queue_type}: Games:{total_games}  Wins: {wins}, Losses: {losses}, Winrate: {winrate:.2f}%")
                else:
                    print(f"{queue_type}: No games played.")
        else:
            print(f"Error en la solicitud Matches. Código de respuesta: {response.status_code}")
    else:
        print(f"Error en la solicitud User. Código de respuesta: {respuesta.status_code}")

# Ejemplo de uso

nombre = input("Introduce nombre de invocador: ")
obtener_info_invocador(nombre)
