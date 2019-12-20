
from sanic import Sanic
from sanic.response import json
import requests
import threading

print(threading.active_count())

app = Sanic()

@app.route("/")
async def test(request):
    url = 'http://lovegaudi.art:3000'
    requests.get(url)
    print(threading.active_count())
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

# python run.py

