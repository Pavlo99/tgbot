from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start(message: types.Message):
    await bot.send_message(message.from_user.id, '🤚 С помощью этого бота Вы можете публиковать и контролировать посты '
                                                 'на канале Олег і Павло корпорейшн 🚁 \n\n В '
                                                 'нижней части чата у Вас есть кнопки для взаимодействия с ботом'
                                                 '👇\n\nНовый пост ➕ — опубликовать пост на канале'
                                                 '\nНовая сделка 🤝 — создать защищенную сделку без публикации на канале'
                                                 '\nМои посты 📑 — просмотреть и контролировать свои посты'
                                                 '\nМои средства 🤑 — вывод средств со счета канала'
                                                 '\nМой рейтинг ⭐️ — Ваш рейтинг в сервисе'
                                                 '\nСообщить о мошеннике 👽 — сообщить администрации о потенциальном'
                                                 ' мошеннике'
                                                 '\n\nПо вопросам рекламы, сотрудничества или любым дургим вопросам, а также'
                                                 ' если есть идеи по улучшению сервиса, пишите администрации канала.')

@dp.message_handler(commands=['menu'])
async def process_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вибери', reply_markup=kb.greet_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)