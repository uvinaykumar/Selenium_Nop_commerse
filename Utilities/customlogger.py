import logging
import logging.config

class LogGen:
    @staticmethod
    def loggen(logg=logging.INFO):
        logging.basicConfig(filename= "D:\\Local Disk\\Selenium practice v4\\Selenium Nop commerse\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        #logging.basicConfig(filename="automation.log",
        #                    format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        #logging.config.fileConfig('logging.conf')
        logger = logging.getLogger()
        logger.setLevel(logg)
        return logger
