
from sanic import Sanic
from sanic.response import json
import aiohttp

app = Sanic()

@app.route("/")
async def test(request):
    url = 'http://lovegaudi.art:3000'
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text = await resp.text()
    return json({"hello": text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# python3.7
# pip install sanic aiohttp
# python run.py

