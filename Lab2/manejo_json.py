from datetime import datetime, timedelta, timezone
import requests
import json
import os, time

CACHE_FILE = 'data.json'
def descarga_json(url):
    
    response = requests.get(url)
    if response.status_code == 200:
        print('Descarga exitosa')
        # return response.json()
        # create json file 
        with open(CACHE_FILE, 'w') as f:
            json.dump(response.json(), f)

    elif response.status_code == 202:
        # verificamos si ya esta descargado
        if os.path.exists(CACHE_FILE):
            print('El archivo ya existe')
        else:
            # If data hasn't been cached yet, wait and try again
            time.sleep(5)  # Wait for 5 seconds
            return descarga_json(url)
    else:
        print('Error en la descarga. Error code: ', response.status_code)
        return None

    f.close()


        
# url = input('Ingrese la URL del archivo JSON: ')
descarga_json('https://api.github.com/repos/EnigMaticSpac3/DataAnalysis/stats/commit_activity')
# descarga_json('https://api.github.com/repos/tensorflow/tensorflow/stats/commit_activity')

# hacer analisis de los datos
with open(CACHE_FILE, 'r') as f:
    data = json.load(f)
    f.close()

commits_por_dia = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0
}

commits_por_semana = {}

for commit in data:
    week_timestamp = commit["week"]
    week_start = datetime.fromtimestamp(week_timestamp, tz=timezone.utc)
    for idx, commits_este_dia in enumerate(commit["days"]):
        commit_date = week_start + timedelta(days=idx)
        day_of_week = commit_date.strftime("%A")
        commits_por_dia[day_of_week] += commits_este_dia
    commits_por_semana[week_timestamp] = sum(commit["days"])

# Encontrar el día de la semana con más commits
dia_mas_commits = max(commits_por_dia, key=commits_por_dia.get)

# Encontrar la semana con más commits
semana_mas_commits_timestamp = max(commits_por_semana, key=commits_por_semana.get)
semana_mas_commits_inicio = datetime.fromtimestamp(semana_mas_commits_timestamp, tz=timezone.utc)
semana_mas_commits_fin = semana_mas_commits_inicio + timedelta(days=6)

print("Día con más commits:", dia_mas_commits)
print("Semana con más commits:", semana_mas_commits_inicio.strftime("%d %B"), "-", semana_mas_commits_fin.strftime("%d %B"))