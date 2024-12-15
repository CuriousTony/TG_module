import asyncio
import logging
from bot_giblets import bot, dp
from handlers import command_handlers, callback_handlers
from keyboards import reply

dp.include_routers(command_handlers.router,
                   callback_handlers.router
                   )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
