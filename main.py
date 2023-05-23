# теорія
import logging # стардатний бібліотека для логування переігу програм
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - % (message)s")# тут викликаємо дебаг і інфо
logging.debug("debug") # показує стардатний перебіг програми
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")