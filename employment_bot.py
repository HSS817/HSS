
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7987372609:AAFKLWiauSRE9s7OlvYwQnVmEFLDxWwWxqM"
RECRUITER_GROUP_ID = -1002824178936

LANGUAGES = {
    "pl": "Polski 🇵🇱",
    "ru": "Русский 🇷🇺",
    "ua": "Українська 🇺🇦",
    "en": "English 🇬🇧"
}

with open("jobs (5).json", "r", encoding="utf-8") as f:
    JOBS = json.load(f)

user_languages = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(name, callback_data=f"lang_{code}")] for code, name in LANGUAGES.items()]
    await update.message.reply_text("Wybierz język / Choose your language:", reply_markup=InlineKeyboardMarkup(keyboard))

async def language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang_code = query.data.split("_")[1]
    user_languages[query.from_user.id] = lang_code

    keyboard = [[InlineKeyboardButton(job, callback_data=f"job_{job}")] for job in JOBS]
    keyboard.append([InlineKeyboardButton("📩 Skontaktuj się z rekruterem / Contact recruiter", callback_data="contact")])
    await query.edit_message_text("Wybierz ofertę pracy / Choose a job offer:", reply_markup=InlineKeyboardMarkup(keyboard))

async def job_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    job_name = query.data.split("_", 1)[1]
    description = JOBS.get(job_name, "Brak opisu / No description available.")

    keyboard = [[InlineKeyboardButton("⬅️ Назад к списку вакансий", callback_data="back_to_jobs")]]
    await query.edit_message_text(f"📄 {job_name}{description}", reply_markup=InlineKeyboardMarkup(keyboard))

async def back_to_jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [[InlineKeyboardButton(job, callback_data=f"job_{job}")] for job in JOBS]
    keyboard.append([InlineKeyboardButton("📩 Skontaktuj się z rekruterem / Contact recruiter", callback_data="contact")])
    await query.edit_message_text("Wybierz ofertę pracy / Choose a job offer:", reply_markup=InlineKeyboardMarkup(keyboard))

async def contact_recruiter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("✍️ Napisz wiadomość, którą chcesz wysłać rekruterowi. \ Write a message to send to the recruiter.")
    context.user_data["awaiting_message"] = True

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("awaiting_message"):
        context.user_data["awaiting_message"] = False
        user = update.message.from_user
        message_text = update.message.text
        await context.bot.send_message(RECRUITER_GROUP_ID, f"📨 Wiadomość od @{user.username or user.id}:{message_text}")
        await update.message.reply_text("✅ Wiadomość została wysłana do rekrutera. / Your message has been sent to the recruiter.")
    elif update.message.chat.id == RECRUITER_GROUP_ID and update.message.reply_to_message:
        lines = update.message.reply_to_message.text.split("
")
        if lines and "@" in lines[0]:
            user_identifier = lines[0].split("@")[1].split(":")[0]
            try:
                user_id = int(user_identifier)
                await context.bot.send_message(user_id, f"📬 Odpowiedź od rekrutera:
{update.message.text}")
            except:
                pass

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(language_selection, pattern="^lang_"))
    app.add_handler(CallbackQueryHandler(job_selection, pattern="^job_"))
    app.add_handler(CallbackQueryHandler(contact_recruiter, pattern="^contact$"))
    app.add_handler(CallbackQueryHandler(back_to_jobs, pattern="^back_to_jobs$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
