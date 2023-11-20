import asyncio


async def main():
    print('1 main')
    await foo('2 text')
    print('3 done')

async def foo(text):
    print(text)
    await asyncio.sleep(2)

# used only inside async function
# await main()
print(type(main()))
asyncio.run(main())


async def main2():
    print('1 main2')
    task = asyncio.create_task(foo2('3 text2'))
    print('2 done2')

async def foo2(text):
    print(text)
    await asyncio.sleep(2)

asyncio.run(main2())


async def fech_data():
    print('data send')
    await asyncio.sleep(2)
    print('data got')
    return {1:'1'}

async def generate_data():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.3)

async def main3():
    task1 = asyncio.create_task(fech_data())
    task2 = asyncio.create_task(generate_data())

    result = await task1



asyncio.run(main3())
