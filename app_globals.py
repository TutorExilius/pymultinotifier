from pymultinotifier.config.manager import ConfigManager

config = ConfigManager()

PRODUCT_NAME = config.pymultinotifier_config.app_name
PRODUCT_VERSION = config.pymultinotifier_config.app_version

