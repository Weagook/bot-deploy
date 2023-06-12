import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, InputFile
from aiogram.utils import executor,markdown
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


# Установите уровень журналирования, чтобы получать сообщения об ошибках и предупреждениях
logging.basicConfig(level=logging.INFO)

# Установите токен бота
TOKEN = "6176195486:AAHDZQWy7iodEQzbgxQosXBVj6b7BUrqzbA"

# Создаем объект бота
bot = Bot(token=TOKEN)

# Создаем объект диспетчера
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Получаем имя пользователя
    user_name = message.from_user.first_name

    # Создаем две кнопки
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Python", callback_data="button1"))
    markup.add(InlineKeyboardButton("Html", callback_data="button2"))
    markup.add(InlineKeyboardButton("Ссылки", callback_data="links"))

    # Отправляем сообщение с приветствием и кнопками пользователю
    await bot.send_message(chat_id=message.chat.id, text=f"Привет, {user_name}! я бот помощник.")
    await bot.send_message(chat_id=message.chat.id, text="Выбери язык:", reply_markup=markup)

# Обработчик нажатия на кнопку 1
@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    with open('Python.jpg', 'rb') as photo_file:
        photo = InputFile(photo_file)
        text = "Выберите тему Python"
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("Переменные и типы данных/Операторы и выражения",url='https://clck.ru/34HC4M', callback_data="topic1"),
            InlineKeyboardButton("Условные операторы (if/else)/Циклы (for/while)",url='https://clck.ru/34HCAP', callback_data="topic2"),
            InlineKeyboardButton("Функции",url='https://clck.ru/34HCCL', callback_data="topic3"),
            InlineKeyboardButton("Списки и кортежи/Словари/Множества",url='https://clck.ru/34HCDm', callback_data="topic4"),
            InlineKeyboardButton("Строки/Ввод и вывод данных",url='https://clck.ru/34HCFH', callback_data="topic5"),
            InlineKeyboardButton("Обработка исключений",url='https://clck.ru/34HCHT', callback_data="topic6"),
            InlineKeyboardButton("Скачать PDF-python", callback_data="send_Python_pdfs"),
            InlineKeyboardButton("Назад", callback_data="back")
        )

        # Отправляем сообщение с фото и кнопками пользователю
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=photo, caption=text, reply_markup=markup)

# Обработчик нажатия на кнопку 2
@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button2(callback_query: types.CallbackQuery):
    with open('html.jpg', 'rb') as photo_file:
        photo = InputFile(photo_file)
        text = "Выберите тему Html"
        # Создаем четыре кнопки: три темы по Python и кнопку "Назад"
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("Синтаксис и структура HTML",url='https://clck.ru/34HCPc', callback_data="topichtml1"),
            InlineKeyboardButton("Формы и элементы управления",url='https://clck.ru/34HCRi', callback_data="topichtml2"),
            InlineKeyboardButton("Таблицы и списки",url='https://clck.ru/34HCSq', callback_data="topichtml3"),
            InlineKeyboardButton("Гиперссылки и изображения",url='https://clck.ru/34HCVE', callback_data="topichtml4"),
            InlineKeyboardButton("Стили и форматирование",url='https://clck.ru/34HCW4', callback_data="topichtml5"),
            InlineKeyboardButton("Мультимедиа и аудио",url='https://clck.ru/34HCWf', callback_data="topichtml6"),
            InlineKeyboardButton("Фреймы и iframe",url='https://clck.ru/34HCYA', callback_data="topichtml7"),
            InlineKeyboardButton("Скачать PDF-Html", callback_data="send_Html_pdfs"),
            InlineKeyboardButton("Назад", callback_data="back")
        )

        # Отправляем сообщение с кнопками пользователю
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=photo, caption=text, reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data == 'back')
async def process_callback_back(callback_query: types.CallbackQuery):
    # Создаем две кнопки
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Python", callback_data="button1"))
    markup.add(InlineKeyboardButton("Html", callback_data="button2"))
    markup.add(InlineKeyboardButton("Ссылки", callback_data="links"))

    # Отправляем сообщение с кнопками пользователю
    await bot.send_message(chat_id=callback_query.message.chat.id, text="Выбери язык:", reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data == 'links')
async def process_callback_links(callback_query: types.CallbackQuery):
    # Создаем кнопку "Назад"
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data="back"))

    # Отправляем сообщение с информацией о выбранной теме
    await bot.send_message(chat_id=callback_query.message.chat.id, text="Ссылки на каналы:\n\
        GoingToInternet: обучение различным языкам программирования, включая Python, JavaScript, HTML/CSS, React, MongoDB и другие. (https://www.youtube.com/c/GoingToInternet/videos)\n\n\
        Suprun Alexey: обучение основам программирования, в том числе языкам Python и JavaScript. (https://www.youtube.com/@SuprunAlexey/videos)\n\n\
        YEM Digital: обучение веб-разработке, включая HTML/CSS, JavaScript, PHP, WordPress и другие технологии. (https://www.youtube.com/c/yemdigital/videos)\n\n\
        Alexey Bychkov: обучение веб-разработке и программированию на языках Python, JavaScript, PHP и других. (https://www.youtube.com/@alexeybychkov_/videos)\n\n\
        Yan Ageenko: обучение веб-разработке, включая HTML/CSS, JavaScript, PHP, MySQL и другие. (https://www.youtube.com/@YanAgeenko/videos)\n\n\
        ITVDN: обучение различным языкам программирования, включая C#, Java, Python, JavaScript, PHP, HTML/CSS и другие, а также технологиям и инструментам веб-разработки. (https://www.youtube.com/c/ITVDN/videos)\n\n\
        BrainsCloud: обучение веб-разработке, включая HTML/CSS, JavaScript, React, Redux, MongoDB и другие технологии. (https://www.youtube.com/@BrainsCloud/videos)\n\n\
        WAYUPIN: обучение веб-разработке, включая HTML/CSS, JavaScript, Vue.js, Node.js, и другие технологии. (https://www.youtube.com/@WAYUPIN/videos)\n\n\
        Granich: обучение различным языкам программирования, включая C++, C#, Java, Python и другие. (https://www.youtube.com/c/Granich/videos)\n\n\
        OrizonDesign: обучение веб-разработке, дизайну и маркетингу, включая HTML/CSS, JavaScript, Adobe Photoshop и другие. (https://www.youtube.com/c/OrizonDesign/videos)\n\n\
        Nikita Yudaev: обучение веб-разработке, включая HTML/CSS, JavaScript, React, Node.js и другие технологии. (https://www.youtube.com/c/NikitaYudaev/videos)\n\n\
        OnlineTutorials4Designers: обучение дизайну и веб-разработке, включая HTML/CSS, JavaScript, React, Adobe Photoshop и другие. (https://www.youtube.com/c/OnlineTutorials4Designers/videos)\n\n\
        codeBurger: обучает различным языкам программирования, включая Python, Java, PHP и другие, а также алгоритмам и структурам данных. (https://www.youtube.com/c/codeBurger/videos)\n\n\
        DesignCourse: обучает веб-разработке, дизайну и маркетингу, включая HTML/CSS, JavaScript, React, Adobe Photoshop и другие. (https://www.youtube.com/c/DesignCourse/videos)\n\n\
        RaddyDev: обучает веб-разработке, включая HTML/CSS, JavaScript, React, Node.js и другие технологии. (https://www.youtube.com/c/RaddyDev/videos)\n\n\
        kepowob: обучает различным языкам программирования, включая Python, Java, C# и другие, а также технологиям веб-разработки, таким как HTML, CSS, React, Vue.js и другие. (https://www.youtube.com/c/kepowob/videos)\n\n\
        UPROCK: ориентирован на разработку игр, уроки по использованию различных игровых движков, таких как Unity и Unreal Engine, а также по программированию на языках C#, C++ и других. (https://www.youtube.com/c/UPROCK/videos)\n\n\
        PsForceRu: уроки по различным языкам программирования, включая Python, C++, C#, а также по работе с технологиями, такими как Arduino и Raspberry Pi. (https://www.youtube.com/c/PsForceRu/videos)\n\n\
        WebCademy: уроки по веб-разработке, включая HTML, CSS, PHP, а также уроки по использованию различных фреймворков, таких как React и Angular. (https://www.youtube.com/c/WebCademy/videos)\n\n\
        TildaPublishing: создание сайтов и приложений на Tilda, платформе для создания сайтов без использования кода. Уроки по созданию сайтов различной сложности. (https://www.youtube.com/@TildaPublishing/videos)\n\n\
        JulioCodes: уроки по Python, Java и C#, а также разработке веб-приложений с использованием фреймворков, таких как Flask и Django. (https://www.youtube.com/c/JulioCodes/videos)\n\n\
        CodingArtist: ориентирован на разработку веб-приложений, уроки по HTML, CSS, React и другим фреймворкам для веб-разработки. (https://www.youtube.com/@CodingArtist/videos)", reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data == 'send_Python_pdfs')
async def send_Python_pdfs_callback(callback_query: types.CallbackQuery):
    await send_Python_pdfs(callback_query.message)

async def send_Python_pdfs(message: types.Message):
    # список файлов из первой группы
    pdf_files = ['Легкий_способ_выучить_Python_3.pdf', 'ООП_в_Python.pdf', 'Словари_в_python.pdf', 'Циклы и условия в Python.pdf', 'Шпаргалка по python для начинающих.pdf']

    # отправляем первое сообщение
    text1 = "Загрузка..."
    await bot.send_message(chat_id=message.chat.id, text=text1)

    # отправляем каждый файл в отдельном сообщении
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as f:
            pdf_input_file = InputFile(f)
            await bot.send_document(chat_id=message.chat.id, document=pdf_input_file)

    # отправляем сообщение о загрузке
    text2 = "Загруженно"
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Переменные и типы данных/Операторы и выражения",url='https://clck.ru/34HC4M', callback_data="topic1"),
        InlineKeyboardButton("Условные операторы (if/else)/Циклы (for/while)",url='https://clck.ru/34HCAP', callback_data="topic2"),
        InlineKeyboardButton("Функции",url='https://clck.ru/34HCCL', callback_data="topic3"),
        InlineKeyboardButton("Списки и кортежи/Словари/Множества",url='https://clck.ru/34HCDm', callback_data="topic4"),
        InlineKeyboardButton("Строки/Ввод и вывод данных",url='https://clck.ru/34HCFH', callback_data="topic5"),
        InlineKeyboardButton("Обработка исключений",url='https://clck.ru/34HCHT', callback_data="topic6"),
        InlineKeyboardButton("Скачать PDF-python", callback_data="send_Python_pdfs"),
        InlineKeyboardButton("Назад", callback_data="back")
    )
    await bot.send_message(chat_id=message.chat.id, text=text2,reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data == 'send_Html_pdfs')
async def send_Html_pdfs_callback(callback_query: types.CallbackQuery):
    # Отправляем сообщение со статусом загрузки
    text1 = "Загрузка..."
    await bot.send_message(chat_id=callback_query.message.chat.id, text=text1)

    # список файлов из первой группы
    pdf_files = pdf_files = ['Учебник HTML для начинающих.pdf', 'HTMLCSSBootstrapJavaScriptjQuery.pdf', 'HTML5. Разработка приложений для мобильных устройств.pdf', 'HTML5 для веб-дизайнеров.pdf']

    # отправляем каждый файл в отдельном сообщении
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as f:
            pdf_input_file = InputFile(f)
            await bot.send_document(chat_id=callback_query.message.chat.id, document=pdf_input_file)

    # Отправляем сообщение со статусом загрузки
    text2 = "Загружено"
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Синтаксис и структура HTML",url='https://clck.ru/34HCPc', callback_data="topichtml1"),
        InlineKeyboardButton("Формы и элементы управления",url='https://clck.ru/34HCRi', callback_data="topichtml2"),
        InlineKeyboardButton("Таблицы и списки",url='https://clck.ru/34HCSq', callback_data="topichtml3"),
        InlineKeyboardButton("Гиперссылки и изображения",url='https://clck.ru/34HCVE', callback_data="topichtml4"),
        InlineKeyboardButton("Стили и форматирование",url='https://clck.ru/34HCW4', callback_data="topichtml5"),
        InlineKeyboardButton("Мультимедиа и аудио",url='https://clck.ru/34HCWf', callback_data="topichtml6"),
        InlineKeyboardButton("Фреймы и iframe",url='https://clck.ru/34HCYA', callback_data="topichtml7"),
        InlineKeyboardButton("Скачать PDF-Html", callback_data="send_Html_pdfs"),
        InlineKeyboardButton("Назад", callback_data="back")
    )
    await bot.send_message(chat_id=callback_query.message.chat.id, text=text2,reply_markup=markup)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)