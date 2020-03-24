import logging, os, sys
from WhatsAppManifest.consts import _PACKAGE_NAME_, _LOGGER_LEVEL_


class WhatsAppManifest(object):
    """
    Classe base para uso do Manifest do WhatsApp
    Versão: 2.20.48
    URL: https://www.whatsapp.com/android/ ! https://www.whatsapp.com/business/
    """

    logger = logging.getLogger(__name__)

    def build_logger(self, name: str):

        """
        Method for building the logger that will be used in the package
        :param name: class name
        :type name: str
        :return: None
        :rtype: None
        """

        self.logger = logging.getLogger(name)

        if self.logger.handlers:
            self.logger.handlers = []

        self.logger.setLevel(_LOGGER_LEVEL_)

        if not os.path.exists("logs"):
            os.makedirs("logs", exist_ok=True)

        fileHandler = logging.FileHandler("{0}/{1}.log".format("logs", name))
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)

    def _build_am_start(self, data: dict, app_distinct: bool = True, app_name: str = None) -> str:
        """
        "adb am start" command builder
        :param data: Command dict
        :type data: dict
        :return: Command string
        :rtype: str
        """
        commands = []
        for key in data.keys():

            if isinstance(data[key], list):
                for item in data[key]:
                    value = item["value"]
                    extra = item.get("extra", None)

                    if callable(value):
                        value = value()

                    commands.append(f"-{key} {value} {extra}")

            elif isinstance(data[key], dict):
                extra = data[key].get("extra", None)
                value = data[key]["value"]

                if callable(value):
                    value = value()

                commands.append(f"-{key} {value} {extra}")
            else:
                value = data[key]

                if callable(value):
                    value = value()

                commands.append(f"-{key} {value}")

        return f"am start {' '.join(commands)} {'-p '+_PACKAGE_NAME_ if not app_name else '-p '+app_name if app_distinct else ''}"
