import os
import json
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

# Load job listings from jobs.json
with open("jobs.json", "r", encoding="utf-8") as f:
    JOBS = json.load(f)

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
    job_name = query.data.split("_", 1)[1]
    description = JOBS.get(job_name, "Brak opisu / No description available.")
    await query.edit_message_text(f"📄 {job_name}

{description}")

# Contact recruiter handler
async def contact_recruiter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("✍️ Napisz wiadomość, którą chcesz wysłać rekruterowi.
Write a message to send to the recruiter.")
    context.user_data["awaiting_message"] = True

# Message handler for user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("awaiting_message"):
        context.user_data["awaiting_message"] = False
        user = update.message.from_user
        message_text = update.message.text
        await context.bot.send_message(RECRUITER_GROUP_ID, f"📨 Wiadomość od @{user.username or user.id}:
{message_text}")
        await update.message.reply_text("✅ Wiadomość została wysłana do rekrutera.
Your message has been sent to the recruiter.")
    elif update.message.chat.id == RECRUITER_GROUP_ID and update.message.reply_to_message:
        lines = update.message.reply_to_message.text.split("\n")
        if lines and "@" in lines[0]:
            user_identifier = lines[0].split("@")[1].split(":")[0]
            try:
                user_id = int(user_identifier)
                await context.bot.send_message(user_id, f"📬 Odpowiedź od rekrutera:
{update.message.text}")
            except:
                pass

# Main application setup
def main():
    # Only run polling if on Render or explicitly allowed
    if os.environ.get("RENDER", "true").lower() == "true":
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(language_selection, pattern="^lang_"))
        app.add_handler(CallbackQueryHandler(job_selection, pattern="^job_"))
        app.add_handler(CallbackQueryHandler(contact_recruiter, pattern="^contact$"))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        app.run_polling()

if __name__ == "__main__":
    main()
