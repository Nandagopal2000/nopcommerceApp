import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

        # logger = logging.getLogger()
        # filehandler = logging.FileHandler(filename='.\\Logs\\automation1.log')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # filehandler.setFormatter(formatter)
        # logger.addHandler(filehandler)
        # logger.setLevel(logging.INFO)
        # return logger

