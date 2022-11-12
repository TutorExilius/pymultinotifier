"""The config management stuff"""

from pathlib import Path

import toml
from serde.toml import from_toml

from pymultinotifier.config.models import (DBManagerConfig,
                                           PyMultiNotifierConfig)


class ConfigManager:  # pylint: disable=R0903
    """The Configmanager to handle read the config.toml file."""

    def __init__(self) -> None:
        self.all_config = toml.load(Path(__file__).parent / "config.toml")
        self.db_manager_config = from_toml(
            DBManagerConfig, toml.dumps(self.all_config["db_manager"])
        )
        self.pymultinotifier_config = from_toml(
            PyMultiNotifierConfig, toml.dumps(self.all_config["pymultinotifier"])
        )
