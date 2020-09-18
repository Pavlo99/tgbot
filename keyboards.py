from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnNewPost = KeyboardButton('Новый пост ➕')
btnNewAgreement = KeyboardButton('Новая сделка 🤝')
btnMyPosts = KeyboardButton('Мои посты 📑')
btnMyMoney = KeyboardButton('Мои средства 🤑')
btnMyRating = KeyboardButton('Мой рейтинг ⭐️')
btnMyChats = KeyboardButton('Мои чаты 👥')
btnNotice = KeyboardButton('Сообщить о мошеннике 👽')
btnList = KeyboardButton('Список кидал 👽')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(btnNewPost,btnNewAgreement)\
    .row(btnMyPosts,btnMyMoney).row(btnMyMoney,btnMyRating).row(btnNotice,btnMyChats).row(btnList)
