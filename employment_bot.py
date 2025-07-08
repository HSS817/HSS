
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Replace with your actual bot token and recruiter group chat ID
BOT_TOKEN = "7987372609:AAFKLWiauSRE9s7OlvYwQnVmEFLDxWwWxqM"
RECRUITER_GROUP_ID = -1002824178936

# Supported languages
LANGUAGES = {
    "pl": "Polski 🇵🇱",
    "ru": "Русский 🇷🇺",
    "ua": "Українська 🇺🇦",
    "en": "English 🇬🇧"
}

# Job listings (descriptions can be updated later)
JOBS = {
    "TRUVANT LODZ": "ПАКУВАННЯ ПРОДУКЦІІ ДЖІЛЕТ (БРИТВИ, НАСАДКИ, ПОДАРУНКОВІ НАБОРИ)  
🕋 Адреса: Nowy Józefów 70, 94-406 Łódź  
🏘 Місто проживання: Łódź 
📑 Тип договору: Umowa zlecenie 
Потрібні : ЖІНКИ, ЧОЛОВІКИ.  
Вік : 18-60  
 
Робота не є фізично важкою, більшість процесів виконуються у сидячому положенні. Основні завдання здійснюються при виробничій лінії. 

Умови праці: 

Чисте та сухе складське приміщення 

Комфортна кімнатна температура 

Безпечні та організовані робочі зони 

Середня кількість робочих годин на місяць: 150–168 годин 

У несезонний період (грудень – березень) кількість годин може зменшуватись до 100 і менше годин 

Графік може бути нестабільним, залежить від виробничої потреби 

Особливості: 

Підходить для тих, хто шукає легку, неважку фізично роботу 

Важливо враховувати можливу змінність графіка та сезонні коливання навантаження 

 
💵 Оплата праці 

•	Для студентів до 26 років: 30.50 zł/год 

•	Основна ставка: 24.60 zł/год 

•	Аванс: 300 zł - після 2 тижнів роботи можна подати заявку , +2/3 дні на нарахування на картку.  

•	Зарплата: виплачується 15 числа за відпрацьований місяць на банківський рахунок.  

❗️ Допомагаємо отримати статус студента до 26 років. 
 
⏰ Графік роботи 

•	5-6 днів на тиждень, 3 зміни (переважно по 8 годин, можливі 12-годинні зміни). 

•	Час зміни: 

Основні: 5:30–13:30, 13:30–21:30, 21:30–5:30 

Додаткові: 6:00–14:00, 14:00–22:00, 22:00–6:00 

•	Робочі години на місяць: 140–170 годин при 8-годинних змінах. 

 
🚌 Транспорт 

•	Безкоштовний транспорт: з міст Ozorków, Zgierz, Sieradz, Łęczyca 

•	Платний громадський транспорт: маршрути в Łódź (Retkinia, G1, G2) 

Більшість працівників добираються до місця роботи пішки — в середньому дорога займає 30–40 хвилин від місця проживання. Також є можливість дістатися громадським транспортом (платним). 

🔹 Компенсація за проїзд не передбачена. 
 
Важливо! Обов'язкове навчання з охорони праці : 

Перед початком роботи всі кандидати проходять обов’язковий інструктаж з охорони праці та техніки безпеки. Навчання проводиться російською  мовою та включає: 

Ознайомлення з правилами безпеки 

Презентацію з поясненням суті роботи 

Можливість занотовувати важливу інформацію (будуть підказки до тесту) 

Після навчання ви проходите тестування у письмовій формі: 
 🔹 Вам буде видано аркуш із запитаннями та варіантами відповідей 
 🔹 Необхідно обрати правильні відповіді 

✅ У разі успішного складання тесту — до роботи можна приступати вже наступного дня або через день. 
🖌 Тестування перед початком роботи (школеніє).  

1.	Тест на знання стандартів безпеки та якості: 

•	Простий тест, включає правила безпеки та стандарти якості. 

•	Кандидати, які уважно слухають та записують інформацію під час навчання, проходять без труднощів (надаються підказки та приклади). 

2.	Тест на БХП (Охорону праці) та стандарти якості: 

•	Складається з 2 частин. 

•	Перевіряється знання коду продукції, правил безпеки та стандартів матеріалів. 
 
🚫 Важливо: на склад заборонено приносити біжутерію, носити спідниці та відкрите взуття. 

✅ Обов’язки 
🔹 Для жінок: 

Робота при виробничій лінії 

Пакування продукції 

Візуальний контроль якості та виявлення браку 

Робота за столами: складання коробок згідно з наданими схемами 

🔹 Для чоловіків: 

Робота при лінії та пакування готової продукції 

Виконання допоміжних складських операцій: 

Робота зі сканером 

Використання ручної палечаки  

Доставка продукції зі складу до виробничої лінії 

Фолювання та підготовка продукції до відправки 

🏠 Умови проживання 

•	Проживання: 430 zł/місяць 
Проживання організовано у квартирах, розташованих у місті Лодзь, район Реткінія — неподалік від місця роботи. 

Кімнати розраховані на 2–3 особи 

Квартири оснащені всім необхідним для комфортного проживання (меблі, побутова техніка, кухня, ванна кімната тощо) 

З собою необхідно мати: 

Постільну білизну 

Особистий посуд: чашку, ложку, вилку, миску 

📌 Додатково 

👕 Одяг та взуття: одноразова оплата 30 zł із зарплати за футболку.  

🩺 Медогляд: за рахунок роботодавця.  
 ",
    "FLEX WOLA RAKOWA": "СКЛАД КОМПЛЕКТАЦІІ ТОВАРІВ (НАВУШНИКИ)   

🌍 Локація: Wola Rakowa (20 км від Łódź) 

🕋 Адреса роботи: Brzezińska 3, 95-006 Wola Rakowa 

🏘 Місто проживання: Łódź 
 

Кандидати: чоловіки, жінки, пари 

Вікові обмеження: від 18 до 45 років 
 
Важливо ! Кандидат повинен мати досвід роботи зі сканером та компютером!  
 

📑 Тип договору: Umowa zlecenie 

✅ Обов’язки працівника 

1.	Робота на виробництві електроніки: 

•	Комплектація та упаковка продукції. 

•	Збір та комплектація палет для відділу продукції. 

2.	Робота з обладнанням: 

•	Використання комп’ютера, сканера, рохлі. 

3.	Процеси роботи: 

•	Працівники можуть бути залучені до різних етапів виробництва. 

📌 Умови роботи: 

•	Відсутність шкідливих факторів. 

•	Робота у комфортній кімнатній температурі без шуму. 

☕ Додатково: працівникам надають безкоштовно чай, каву та яблука без обмежень. 

⏰ Графік роботи 

•	5 днів на тиждень (залежить від замовлень). 

•	Робочі зміни: 

6:00–14:00, 14:00–22:00 (8 годин). 

                 6:00-16:00, 12:00-22:00 (10 год).  

6:00–18:00, 10:00–22:00 (12 годин).  
Можуть бути нічні, але рідко!  

💵 Оплата праці 

•	Для студентів до 26 років: 32.00 zł/год (нетто). 

•	Основна ставка: 25.80 zł/год (нетто). 

💰 Аванс: 300 zł .Після 2 відпрацьованих тижнів можна податись на отримання + 2\3 дні на нарахування на картку.  

💳 Зарплата: виплачується 15 числа за відпрацьований місяць на банківський рахунок.  

📢 Додатково допомагаємо оформити статус студента до 26 років. 

🏠 Умови проживання 

•	Житло безкоштовне: по 3-4 особи в кімнаті. 

•	Для пар: надається окрема кімната. 
Долпати за своє житло – НЕ МАЄ. 

🚌 Транспорт: 

•	Роботодавець надає безкоштовний проїзний по м. Łódź (мігавка).  

•	Відправлення на склад із aleja Ofiar Terroryzmu 11 Września 17, 92-410 Łódź. Робочий транспорт доставляє працівників до складу. Уся дорога займає близько 40 хвилин. 

📌 Додаткові умови 

👕 Одяг і взуття: надаються безкоштовно. 

🩺 Медогляд: за рахунок роботодавця. 

❗️ Для оформлення документів візьміть фото 3×4 для безкоштовного проїзного квитка. "
}

# Store user language preferences
user_languages = {}

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(name, callback_data=f"lang_{code}")] for code, name in LANGUAGES.items()]
    await update.message.reply_text("Wybierz język / Choose your language:", reply_markup=InlineKeyboardMarkup(keyboard))

# Language selection handler
async def language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang_code = query.data.split("_")[1]
    user_languages[query.from_user.id] = lang_code

    keyboard = [[InlineKeyboardButton(job, callback_data=f"job_{job}")] for job in JOBS]
    keyboard.append([InlineKeyboardButton("📩 Skontaktuj się z rekruterem / Contact recruiter", callback_data="contact")])
    await query.edit_message_text("Wybierz ofertę pracy / Choose a job offer:", reply_markup=InlineKeyboardMarkup(keyboard))

# Job selection handler
async def job_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    job_name = query.data.split("_")[1]
    description = JOBS.get(job_name, "Brak opisu / No description available.")
    await query.edit_message_text(f"📄 {job_name}\n\n{description}")

# Contact recruiter handler
async def contact_recruiter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("✍️ Napisz wiadomość, którą chcesz wysłać rekruterowi.\nWrite a message to send to the recruiter.")
    context.user_data["awaiting_message"] = True

# Message handler for user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("awaiting_message"):
        context.user_data["awaiting_message"] = False
        user = update.message.from_user
        message_text = update.message.text
        await context.bot.send_message(RECRUITER_GROUP_ID, f"📨 Wiadomość od @{user.username or user.id}:\n{message_text}")
        await update.message.reply_text("✅ Wiadomość została wysłana do rekrutera.\nYour message has been sent to the recruiter.")
    elif update.message.chat.id == RECRUITER_GROUP_ID and update.message.reply_to_message:
        lines = update.message.reply_to_message.text.split("\n")
        if lines and "@" in lines[0]:
            user_identifier = lines[0].split("@")[1].split(":")[0]
            try:
                user_id = int(user_identifier)
                await context.bot.send_message(user_id, f"📬 Odpowiedź od rekrutera:\n{update.message.text}")
            except:
                pass

# Main application setup
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(language_selection, pattern="^lang_"))
    app.add_handler(CallbackQueryHandler(job_selection, pattern="^job_"))
    app.add_handler(CallbackQueryHandler(contact_recruiter, pattern="^contact$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
