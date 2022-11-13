"""The DB Manager class + definitions"""

from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker

import app_globals
from pymultinotifier.database.models import Platform, Post, Profile
from pymultinotifier.type_definitions import PlatformType

engine = create_engine(app_globals.config.db_manager_config.database_url)
Session = sessionmaker(engine)


class DBManager:
    """The DB Manager class"""

    def create_profile(self, name: str) -> int:
        """Create a new profile in database.

        :param name: Name of the profile.
        :type name: str
        :return: The ID of the created profile.
        :rtype: int
        """

        with Session() as session:
            new_profile = Profile(name=name)
            session.add(new_profile)
            session.commit()

            return new_profile.id

    def create_platform(
        self,
        name: str,
        platform_type: PlatformType,
        credentials: dict[str, str],
        profile_id: int,
    ) -> int:
        """Create a new platform in database.

        :param name: Name of the platform.
        :type name: str
        :param platform_type: The platform type.
        :type platform_type: PlatformType
        :param credentials: The platform specific credentials.
        :type credentials: dict[str, str]
        :param profile_id: ID of the profile, where the new
            platform entry should be added in.
        :type profile_id: int
        :return: The ID of the created platform.
        :rtype: int
        """

        with Session() as session:
            new_platform = Platform(
                name=name,
                platform_type=platform_type,
                credentials=credentials,
            )
            profile = session.get(Profile, profile_id)
            profile.platforms.append(new_platform)
            session.commit()

            return new_platform.id

    def create_post(self, message: str, platform_id: int) -> None:
        """Create a new post in database.

        :param message: The post message.
        :type message: str
        :param platform_id: ID of the platform, where the new
            post entry should be added in.
        :type platform_id: int
        :return: The ID of the created post.
        :rtype: int
        """

        with Session() as session:
            new_post = Post(message=message)
            platform = session.get(Platform, platform_id)
            platform.post_history.append(new_post)
            session.commit()

            return new_post.id

    def get_posts(self, platform_id: int) -> list[Post]:
        with Session() as session:
            posts = session.query(Post).filter(Post.platform_id == platform_id).all()
            return posts

    def get_platforms(self, profile_id: int) -> list[Platform]:
        with Session() as session:
            platforms = (
                session.query(Platform)
                .filter(Platform.profile_id == profile_id)
                .options(joinedload(Platform.post_history))
                .all()
            )
            return platforms

    def get_profiles(self) -> list[Profile]:
        with Session() as session:
            profiles = (
                session.query(Profile)
                .options(
                    joinedload(Profile.platforms).joinedload(Platform.post_history)
                )
                .all()
            )
            return profiles
