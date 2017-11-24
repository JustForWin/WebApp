import sys
import orm
import asyncio
from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(loop = loop ,user='root', password='d514', db='pydb')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
    yield from orm.destory_pool()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait([test( loop )]) )
    loop.close()
    if loop.is_closed():
        sys.exit(0)