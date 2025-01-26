import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "29177925"))
    API_HASH = os.environ.get("API_HASH", "87321aacec520ac75d7d7694e476ad0e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7741257106:AAEZKg-ixVU0HZBebbApwya0-R3XFgJNn14")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "redline_2025_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
