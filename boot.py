from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "SEU_TOKEN_AQUI"  

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🎮 Próximas partidas", callback_data='next_matches')],
        [InlineKeyboardButton("📊 Estatísticas dos jogadores", callback_data='stats')],
        [InlineKeyboardButton("📰 Últimas notícias", callback_data='news')],
        [InlineKeyboardButton("🧠 Quiz da FURIA", callback_data='quiz')],
        [InlineKeyboardButton("🛒 Loja oficial", callback_data='shop')],
        [InlineKeyboardButton("🖼️ Conteúdos exclusivos", callback_data='extras')],
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👊 Bem-vindo ao FURIABOT, torcedor da FURIA! Escolha uma opção:",
        reply_markup=main_menu()
    )

async def handle_menu_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'next_matches':
        text = "📅 Próximas partidas: FURIA vs. THE Mongolz\n💥 Campeonato: PGL Astana 2025"
    elif data == 'stats':
        text = "📊 Stats dos jogadores:\n- KSCERATO: 1.21 rating\n- yuurih: 1.19 rating\n- Yekindar 1.11 rating\n- Fallen: 1.18 rating\n- molodoy 1.24 rating"
    elif data == 'Ranking':
        text = "📊 Ranking valve # 17\n- Ranking Mundial #22"
    elif data == 'news':
        text = "📰 Últimas: FURIA anuncia bootcamp na Europa antes da ESL Pro League!\n- Molodoy Chega como novo Awper.\n- Yekindar estreia como novo ENTRY FRAGGER."
    elif data == 'quiz':
        text = "🧠 Quiz em breve! Fique ligado nas atualizações."
    elif data == 'shop':
        text = "🛒 Confira a loja oficial: https://furia.gg"
    elif data == 'extras':
        text = "🖼️ Baixe stickers e wallpapers aqui: https://furia.gg/midia"
    else:
        text = "❌ Opção inválida."

    await query.edit_message_text(text=text, reply_markup=main_menu())

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_menu_selection))

    print("✅ FURIABOT rodando... (Ctrl+C para encerrar)")
    app.run_polling()