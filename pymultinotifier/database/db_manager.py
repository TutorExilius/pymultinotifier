"""The DB Manager class + definitions"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app_globals
from pymultinotifier.database.models import Platform, Post, Profile
from pymultinotifier.types import PlatformType

engine = create_engine(app_globals.config.db_manager_config.database_url)
Session = sessionmaker(engine)


class DBManager:
    """The DB Manager class"""

    def create_profile(self, name: str) -> None:
        """Create a new profile in database.

        :param name: Name of the profile.
        :type name: str
        """

        with Session() as session:
            new_profile = Profile(name=name)
            session.add(new_profile)
            session.commit()

    def create_platform(
        self, name: str, platform_type: PlatformType, profile_id: int
    ) -> None:
        """Create a new platform in database.

        :param name: Name of the platform.
        :type name: str
        :param platform_type: The platform type.
        :type platform_type: PlatformType
        :param profile_id: ID of the profile, where the new
            platform entry should be added in.
        :type profile_id: int
        """

        with Session() as session:
            new_platform = Platform(name=name, platform_type=platform_type)

            profile = session.get(Profile, profile_id)
            profile.platforms.append(new_platform)

            session.commit()

    def create_post(self, message: str, platform_id: int) -> None:
        """Create a new post in database.

        :param message: The post message.
        :type message: str
        :param platform_id: ID of the platform, where the new
            post entry should be added in.
        :type platform_id: int
        """

        with Session() as session:
            new_post = Post(message=message)

            platform = session.get(Platform, platform_id)
            platform.post_history.append(new_post)

            session.commit()
