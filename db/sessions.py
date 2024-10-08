import sqlalchemy as sa
import core.settings
from typing import Generator
from enum import Enum


class SessionType(Enum):
    WRITER = "writer"
    READER = "reader"


_engine = None


def get_engine() -> sa.engine.base.Engine:
    global _engine
    if _engine is not None:
        return _engine
    return sa.create_engine(core.settings.DATABASE_URL)


def create_session(
    *, session_type: SessionType, autocommit: bool = False, autoflush: bool = True
) -> sa.orm.sessionmaker:
    return sa.orm.sessionmaker(
        bind=get_engine(),
        autoflush=autoflush,
        autocommit=autocommit,
        info={"type": session_type.value},
    )


def get_db_writer(
    *, autocommit: bool = False, autoflush: bool = True
) -> Generator[sa.orm.Session]:
    db = create_session(SessionType.WRITER, autocommit, autoflush)()
    try:
        yield db
    finally:
        db.close()


def get_db_reader(
    *, autocommit: bool = False, autoflush: bool = True
) -> Generator[sa.orm.Session]:
    db = create_session(SessionType.READER, autocommit, autoflush)()
    try:
        yield db
    finally:
        db.close()


def get_dbs(
    *,
    reader_autocommit: bool = False,
    reader_autoflush: bool = True,
    writer_autocommit: bool = False,
    writer_autoflush: bool = True
) -> Generator[tuple[sa.orm.Session, sa.orm.Session]]:
    reader = create_session(SessionType.READER, reader_autocommit, reader_autoflush)()
    writer = create_session(SessionType.WRITER, writer_autocommit, writer_autoflush)()
    try:
        yield reader, writer
    finally:
        reader.close()
        writer.close()
