from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

questions = [
    "Why are you going to the USA?",
    "Why did you choose this university?",
    "How will you fund your education?",
    "What will you do after graduation?"
]

user_states = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_states[update.effective_chat.id] = 0
    await update.message.reply_text("Welcome to the F1 Visa Interview Bot! Type 'start' to begin.")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = update.message.text.lower()

    if user_id not in user_states or text == "start":
        user_states[user_id] = 0
        await update.message.reply_text(questions[0])
        return

    state = user_states[user_id]
    if state < len(questions) - 1:
        user_states[user_id] += 1
        await update.message.reply_text(questions[user_states[user_id]])
    else:
        await update.message.reply_text("Interview completed! Thanks for practicing. 🎓🇺🇸")

app = ApplicationBuilder().token("7766789282:AAGS4jQceOyKeWPvws-XAESNOuvZ00OdEGE").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler))

app.run_polling()
