from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import calc

#Hello
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!')


#Help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'Hello, {update.effective_user.first_name}!\n'
        f'Main avialable commands:\n'
        f'/hello - see yours welcome\n'
        f'/calculate - calculate your simple math expression\n')


#Calculation
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input = update.message.text
    expression = input.split('', maxsplit=1)[1:]
    result = float(calc.calculation(*expression))
    if result == int(result):  # Clearing float .0
        result = int(result)
    output = ''.join(calc.clearing_expression(*expression)), "=", round(result, 12)
    await update.message.reply_text(' '.join(map(str, output)))
