from aiogram import Bot, types, executor, Dispatcher
from configure import config
from main_bs4 import parse



bot = Bot(token=config)
dp = Dispatcher(bot)

'''----------------------------Рабочая информация----------------------------'''
async def on_startup(_):
    print('Bot is online!')

'''----------------------------Команды----------------------------'''
@dp.message_handler(commands=['start'])
async def command_start(message:types.Message):
    await bot.send_message(message.from_user.id, 'Привет, {0.first_name}. Я бот Парсер, структурирую данные с сайта Drom!\nНапиши команду /help, чтобы познакомиться с функционалом!'.format(message.from_user))

@dp.message_handler(commands=['help'])
async def command_help(message:types.Message):
    await bot.send_message(message.from_user.id, 'Всe очень просто!\nУкажи на сайте Drom те параметры, которые тебе нужны для поиска автомобилей.\nЗатем отправь мне URL ссылку, чтобы я мог собрать данные для тебя!')


'''----------------------------URL----------------------------'''
@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(text='Собираем информацию! Процесс может занять время, пожалуйста подождите!')
    try:
        parse(message.text)
        await message.answer_document(open('cars.csv', 'rb'))
    except:
        await message.answer(text='Oшибка на сервере сайта, либо вы неправильно ввели URL!\nПовторите попытку!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

