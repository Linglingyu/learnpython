import asyncio
import threading

# @asyncio.coroutine
# def hello():
# 	print("Hello world!(%s)"%threading.currentThread())
# 	#异步调用asyncio.sleep(1):
# 	r=yield from asyncio.sleep(1)
# 	print("Hello again!(%s)"%threading.currentThread())

#使用async/await新语法
async def hello():
	print("Hello world!(%s)"%threading.currentThread())
	#异步调用asyncio.sleep(1):
	r=await asyncio.sleep(1)
	print("Hello again!(%s)"%threading.currentThread())


#获取Eventloop:
loop=asyncio.get_event_loop()
#执行coroutine
# loop.run_until_complete(hello())
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
#两个coroutine是由同一个线程并发执行的
loop.close()