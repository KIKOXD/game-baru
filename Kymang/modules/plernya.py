from Kymang.config import ADMINS
from Kymang.modules.data import *


async def plernya():
    if 478043396 not in await cek_seller():
        await add_seller(478043396)
