from telebot.types import Message
from keyboards.inline.information import inform_keyboards
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):

    bot.reply_to(message, f"Привет, {message.from_user.full_name}! \n"
                          f"Я виртуальный помощник, обладающий обширным запасом информации об аэропортах, рейсах, "
                          f"а также о расстояниях и времени полета между ними. Моя задача заключается в том, "
                          f"чтобы предоставлять вам данные, помогая вам легко и уверенно планировать свои "
                          f"путешествия. Независимо от того, нужна ли вам информация о конкретном аэропорте, "
                          f"актуальное расписание рейсов или точные детали о времени полета, я всегда готов помочь и "
                          f"быть вашим надежным источником информации.")
    inform_keyboards(message)
