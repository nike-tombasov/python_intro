from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_model

app = ApplicationBuilder().token("5880485971:AAHVZeNVgcCsNfY463ucia1LO2-r9M-60i0").build()

#Hello
app.add_handler(CommandHandler("hello", bot_model.hello))

#Help
app.add_handler(CommandHandler("help", bot_model.help))

#Calculation
app.add_handler(CommandHandler("calculate", bot_model.calculate)) 


print("Bot started")
app.run_polling()
