import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler(".\\Logs\\automation.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)     # filehandler object
        logger.setLevel(logging.INFO)      # this will skip debug
        return logger
