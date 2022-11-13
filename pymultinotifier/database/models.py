"""SQLAlchemy database models"""

from typing import Any

from sqlalchemy import (JSON, Column, DateTime, Enum, ForeignKey, Integer,
                        MetaData, String, func)
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import relationship

from pymultinotifier.type_definitions import PlatformType
from pymultinotifier.utils import helper

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

Base: DeclarativeMeta = declarative_base(metadata=meta)


class BaseModel(Base):  # pylint: disable=too-few-public-methods
    """The base model for all SQLAlchemy database models."""

    __abstract__ = True

    created_at = Column(
        DateTime,
        default=func.now(),
        nullable=False,
        doc="The datetime of the objects creation.",
    )
    notes = Column(String, nullable=True, doc="Field for some notes.")

    def __init_subclass__(cls, **kwargs: dict[Any, Any]) -> None:
        cls.__tablename__ = helper.camel_to_snake_case(cls.__name__)


class BaseModelWithID(BaseModel):  # pylint: disable=R0903
    """The base model for all SQLAlchemy database models,
    where an id shall be used as primary key."""

    __abstract__ = True

    id = Column(Integer, primary_key=True, doc="The unique object ID.")


class Post(BaseModelWithID):  # pylint: disable=R0903
    """The Post database model."""

    message = Column(String, nullable=False)
    platform_id = Column(
        Integer, ForeignKey("platform.id", ondelete="cascade"), nullable=False
    )
    platform = relationship("Platform", backref="post_history", lazy="subquery")


class Platform(BaseModelWithID):  # pylint: disable=R0903
    """The Platform database model."""

    name = Column(String, nullable=False)
    platform_type = Column(Enum(PlatformType), nullable=False)
    credentials = Column(JSON, nullable=False)

    profile_id = Column(
        Integer, ForeignKey("profile.id", ondelete="cascade"), nullable=False
    )
    profile = relationship("Profile", backref="platforms", lazy="subquery")


class Profile(BaseModelWithID):  # pylint: disable=R0903
    """The Profile database model."""

    name = Column(String, nullable=False)
