"""The config data classes to read module configuration
data like credentials, settings etc."""

from dataclasses import dataclass
from pathlib import Path

from serde import Strict, field, serde


@serde(type_check=Strict)
@dataclass
class DBManagerConfig:
    """DB Manager Config Model."""

    database_file_name: str
    working_dir: Path = field(default=Path())
    database_url: str = field(default="")

    def __init__(
        self,
        database_file_name: str,
        working_dir: Path,
        database_url: str,
    ) -> None:
        self.database_file_name = database_file_name

        if working_dir == Path():
            working_dir = Path(__file__).absolute().parent.parent.parent

        if database_url == "":
            database_url = f"sqlite:///{working_dir}/{database_file_name}"

        self.working_dir = working_dir
        self.database_url = database_url


@serde(type_check=Strict)
@dataclass
class PyMultiNotifierConfig:
    """PyMultiNotifier Config Model."""


@serde(type_check=Strict)
@dataclass
class DiscordConfig:
    """DiscordConfig Config Model."""

    web_hook: str


@serde(type_check=Strict)
@dataclass
class TelegramConfig:
    """TelegramConfig Config Model."""

    token: str
    chat_id: str


@serde(type_check=Strict)
@dataclass
class TwitterConfig:
    """TwitterConfig Config Model."""

    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str
