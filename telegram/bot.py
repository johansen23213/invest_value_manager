import asyncio
import subprocess
import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters

load_dotenv()
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
WORKDIR = "/home/angel/value_invest2"
ALLOWED = [998346625]

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger(__name__)

new_session = False
bot_username = None


async def run_claude(msg, use_continue=True):
    cmd = ["claude", "-p", "--permission-mode", "bypassPermissions"]
    if use_continue:
        cmd.append("--continue")
    cmd.append(msg)

    log.info(f"Ejecutando: {' '.join(cmd[:5])}... [{len(msg)} chars]")

    result = await asyncio.to_thread(
        subprocess.run, cmd,
        capture_output=True, text=True,
        cwd=WORKDIR, timeout=600
    )
    return result.stdout or result.stderr or "Sin respuesta"


async def send_response(update, text):
    """Envía respuesta partida en trozos si supera límite Telegram."""
    if not text.strip():
        text = "Sin respuesta"
    for i in range(0, len(text), 4000):
        await update.message.reply_text(text[i:i+4000])


def is_directed_at_bot(update):
    """En privado siempre responde. En grupo solo si mencionan al bot o responden a él."""
    if update.effective_chat.type == "private":
        return True

    # Responde si es reply a un mensaje del bot
    if update.message.reply_to_message and update.message.reply_to_message.from_user:
        if update.message.reply_to_message.from_user.id == update.get_bot().id:
            return True

    # Responde si mencionan al bot (@username)
    if bot_username and f"@{bot_username}" in (update.message.text or ""):
        return True

    return False


async def on_message(update, context):
    if update.effective_user.id not in ALLOWED:
        return

    if not is_directed_at_bot(update):
        return

    global new_session
    use_continue = not new_session
    new_session = False

    # Limpiar la mención del bot del texto si existe
    text = update.message.text or ""
    if bot_username:
        text = text.replace(f"@{bot_username}", "").strip()

    if not text:
        return

    waiting = await update.message.reply_text("Procesando...")

    try:
        response = await run_claude(text, use_continue)
        await waiting.delete()
        await send_response(update, response)
    except subprocess.TimeoutExpired:
        await waiting.edit_text("Timeout (10 min). Intenta algo más corto.")
    except Exception as e:
        await waiting.edit_text(f"Error: {e}")
        log.error(f"Error: {e}")


async def on_nueva(update, context):
    if update.effective_user.id not in ALLOWED:
        return
    global new_session
    new_session = True
    await update.message.reply_text("Nueva sesion. El proximo mensaje arranca de cero.")


async def on_status(update, context):
    if update.effective_user.id not in ALLOWED:
        return
    await update.message.reply_text("Bot activo")


async def post_init(application):
    global bot_username
    bot_info = await application.bot.get_me()
    bot_username = bot_info.username
    log.info(f"Bot username: @{bot_username}")


def main():
    app = Application.builder().token(TOKEN).build()
    app.post_init = post_init
    app.add_handler(CommandHandler("nueva", on_nueva))
    app.add_handler(CommandHandler("status", on_status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    log.info("Bot iniciado. Esperando mensajes...")
    app.run_polling()


if __name__ == "__main__":
    main()
