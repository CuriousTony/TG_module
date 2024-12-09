from os import getenv
import dotenv
from aiogram import Bot, Dispatcher

dotenv.load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
