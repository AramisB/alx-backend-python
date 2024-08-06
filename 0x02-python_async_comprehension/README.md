Asynchronous Generators
Asynchronous generators allow you to iterate over values that are produced asynchronously, such as data fetched from a network or a database.

Creating an Asynchronous Generator
To create an asynchronous generator, use the async def syntax along with yield:

python
async def async_gen():
    for i in range(10):
        await asyncio.sleep(1)
        yield i
In this example, async_gen yields numbers from 0 to 9, waiting 1 second between each value.

Using an Asynchronous Generator
To use an asynchronous generator, you can iterate over it using async for:

python
import asyncio

async def main():
    async for value in async_gen():
        print(value)

asyncio.run(main())
In this example, async for is used to iterate over the values produced by async_gen.

Async Comprehensions
Async comprehensions allow you to create lists, sets, and dictionaries from asynchronous iterators in a concise manner.

Example of an Async List Comprehension
async def main():
    result = [i async for i in async_gen()]
    print(result)

asyncio.run(main())
In this example, an async list comprehension is used to collect all values produced by async_gen into a list.

Type-Annotating Generators
Type annotations provide hints about the types of values that functions return or expect as arguments. This helps with code readability and can be useful for static type checkers.

Type-Annotating Synchronous Generators
For synchronous generators, use the Generator type from the typing module:

python
from typing import Generator

def sync_gen() -> Generator[int, None, None]:
    for i in range(10):
        yield i
Here, Generator[int, None, None] indicates that sync_gen yields integers, does not accept any values via send, and does not return any value.

Type-Annotating Asynchronous Generators
For asynchronous generators, use the AsyncGenerator type from the typing module:

python
from typing import AsyncGenerator
import asyncio

async def async_gen() -> AsyncGenerator[int, None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield i
Here, AsyncGenerator[int, None] indicates that async_gen yields integers and does not return any value.

Examples
Example 1: Asynchronous Generator
python
import asyncio
from typing import AsyncGenerator

async def async_gen() -> AsyncGenerator[int, None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield i

async def main():
    async for value in async_gen():
        print(value)

asyncio.run(main())
Example 2: Async Comprehension
python
import asyncio

async def async_gen() -> AsyncGenerator[int, None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield i

async def main():
    result = [i async for i in async_gen()]
    print(result)

asyncio.run(main())
Example 3: Type-Annotated Synchronous Generator
python
from typing import Generator

def sync_gen() -> Generator[int, None, None]:
    for i in range(10):
        yield i

for value in sync_gen():
    print(value)