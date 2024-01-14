import requests

url = 'https://unpkg.com/htmx.org@1.7.0/dist/htmx.js'
response = requests.get(url)

with open('static/src/htmx.js', 'wb') as file:
    file.write(response.content)