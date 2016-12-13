import asyncio

from aiohttp import web

asnyc def index(request):
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>Index</h1>')

asnyc def hello(request):
	await asyncio.sleep(0.5)
	text=