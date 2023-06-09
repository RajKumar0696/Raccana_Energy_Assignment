import logging
import os


class Logger:

    def __init__(self, filename="automation"):
        self.logger = logging.getLogger("__name__")
        self.formatter = logging.Formatter("%(asctime)s %(levelname)s:%(message)s")
        file_handler = logging.FileHandler(
            str(os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../"))) + "/Logs/" + filename + ".log", 'w')
        file_handler.setFormatter(self.formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

    def log_critical(self, msg):
        self.logger.setLevel(logging.CRITICAL)
        self.logger.critical(msg)

    def log_error(self, msg):
        self.logger.setLevel(logging.ERROR)
        self.logger.error(msg)

    def log_warning(self, msg):
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(msg)

    def log_info(self, text):
        self.logger.setLevel(logging.INFO)
        self.logger.info(text)

    def log_debug(self, text):
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(text)