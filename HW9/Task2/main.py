from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_model

app = ApplicationBuilder().token("").build()

#Hello
app.add_handler(CommandHandler("hello", bot_model.hello))

#Help
app.add_handler(CommandHandler("help", bot_model.help))

#Calculation
app.add_handler(CommandHandler("calculate", bot_model.calculate)) 


print("Bot started")
app.run_polling()
