from database.core import crud
from loader import bot
from telebot import custom_filters
import handlers
from utils.set_bot_commands import set_default_commands

db_write = crud.create()
db_read = crud.retrieve()

if __name__ == "__main__":
    set_default_commands(bot)
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(custom_filters.IsDigitFilter())
    bot.infinity_polling(skip_pending=True)
