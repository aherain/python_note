import time
import asyncio

now = lambda : time.time()
async def do_some_work(x):
    print('waiting:', x)
    return 1

#最大的优势用同步的方式写异步的程序
print('直接调用异步方法:', do_some_work(21))

start = now()
coroutine = do_some_work(1212)
print("""corountine""", coroutine)
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print('TIME', now() - start)


#绑定回调
def callback(future):
    print('Callback', future.result())


#create_task 方式创建任务
corouti_1 = do_some_work('包成task任务，可以查看任务状态')
task = loop.create_task(corouti_1) #通过事件的循环体可以创建一个任务，可以检测任务的执行执行状态
task.add_done_callback(callback)
print(task)
loop.run_until_complete(task)
print('任务的计算结果', task.result())



#ensure_future方式创建任务
counit2 = do_some_work('绑定回调函数')
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(counit2)
task.add_done_callback(callback) #等价于 callback(task)
loop.run_until_complete(task)


#通过task的结果属性result,也可以拿到最终的jieguo
print('最后task执行完成的结果值：', task.result())



#阻塞和wait

async def do_work_wait(t):
    print("等待时长秒数：%s" % t)
    await asyncio.sleep(t)
    return 'Done after {}s'.format(t)

start = now()
coro_3 = do_work_wait(3)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coro_3)
loop.run_until_complete(task)
print('Task ret：', task.result())
print("TIME：", now() - start)



#并行和并发

start = now()
cor1 = do_work_wait(8)
cor2 = do_work_wait(4)
cor3 = do_work_wait(2)

tasks = [
    asyncio.ensure_future(cor1),
    asyncio.ensure_future(cor2),
    asyncio.ensure_future(cor3)
]

loop = asyncio.get_event_loop()
asy_tasks = asyncio.wait(tasks) #包装成等待的任务列表
loop.run_until_complete(asy_tasks)

for task in tasks:
    print('Task ret:', task.result())
print('TIME：', now() - start)



#协程套协程
print("协程嵌套协程")
async def main():
    dones, pendings = await asyncio.wait(tasks)
    print('nihao1234', dones, pendings)
    for task in dones:
        print("Task ret：", task.result())

start = now()
loop = asyncio.get_event_loop()
result1 = loop.run_until_complete(main())

#asyncio.gather 使用的案例
async def main1():
    return await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
results = loop.run_until_complete(main1())
for res in results:
    print('fianal result：', res)
#aiohttp

