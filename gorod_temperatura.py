import telebot
import requests

bot = telebot.TeleBot("7987537445:AAFK1Hd7ZV9l_oipP9gfhWibbY1YQieMAFk")
API = "4e89aa55a888bc5ae5dca8c3a9ecc624"

# Список російських міст (у нижньому регістрі)
russian_cities = [
    "москва", "санкт-петербург", "новосибірськ", "єкатеринбург", "казань", "нижній новгород",
    "челябінськ", "самара", "омськ", "ростов-на-дону", "уфа", "волгоград", "перм", "красноярськ",
    "воронеж", "саратов", "тольятті", "краснодар", "іркутськ", "ульяновськ", "ярославль",
    "владивосток", "ставрополь", "хабаровськ", "тюмень", "барнаул", "іжевськ", "томськ",
    "кемерово", "рязань", "астрахань", "пенза", "липецьк", "калуга", "курган", "магнітогорськ",
    "сочі", "череповець", "тверь", "смоленськ", "архангельськ", "саранськ"
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет рад тебя видеить, напиши название города")

@bot.message_handler(content_types=['text'])
def get_weather_messages(message):
    city = message.text.strip().lower()
    # Якщо місто з російського списку
    if city in russian_cities:
        bot.reply_to(message, "пішов звідси москаль")
        return
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    data = res.json()
    if data.get("cod") != 200:
        bot.reply_to(message, "Город не найден. Попробуйте еще раз.")
        return
    temp = data["main"]["temp"]
    bot.reply_to(message, f"Погода в городе {city}: {temp}°C")

bot.polling(none_stop=True)