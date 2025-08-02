from Kymang.config import ADMINS
from Kymang.modules.data import *


async def plernya():
    if 7827681835 not in await cek_seller():
        await add_seller(7827681835)
