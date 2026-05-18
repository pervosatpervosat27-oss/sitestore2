import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "ВАШ_ТОКЕН_ТУТ"

bot = telebot.TeleBot(TOKEN)

def get_keyboard():
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add(InlineKeyboardButton("👤 Мій акаунт", url="https://t.me/Favzzet_6542"))
    keyboard.add(InlineKeyboardButton("🌐 Сайт", url=""))
    keyboard.add(InlineKeyboardButton("💳 Оплата", url="https://send.monobank.ua/jar/87EpSZgx3t"))
    
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    
    text = (
        f"Привіт, {name}! 👋\n\n"
        "🏢 *Ласкаво просимо до нашої команди!*\n\n"
        "Ми займаємося:\n"
        "📊 Продажем презентацій на різні теми\n"
        "🤝 Працюємо з великими компаніями\n"
        "🎬 Створюємо прев'ю для відео\n"
        "🌐 Розробкою сайтів\n\n"
        "💼 Якість — наш пріоритет!\n\n"
        "👇 Вибери що тебе цікавить:"
    )
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=get_keyboard())

@bot.message_handler(func=lambda m: True)
def any_message(message):
    bot.send_message(
        message.chat.id,
        "Скористайся кнопками нижче 👇",
        reply_markup=get_keyboard()
    )

print("Бот запущено ✅")
bot.polling(none_stop=True)