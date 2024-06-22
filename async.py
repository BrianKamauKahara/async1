import asyncio
# Checking
async def delayed_hi(seconds: int):
    await asyncio.sleep(seconds)
    print(f"Hi after {seconds}")

async def yoghurt_is_nice():
    await asyncio.sleep(2.5)
    print('Yoghurt is incredible! 2.5s of sweetness is worth everything!')

async def main():
    await asyncio.gather(
        delayed_hi(1),
        delayed_hi(5),
        delayed_hi(3),
        yoghurt_is_nice()
    )

asyncio.run(main())