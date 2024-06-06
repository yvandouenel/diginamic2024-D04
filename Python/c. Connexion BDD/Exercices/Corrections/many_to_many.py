###########
# IMPORTS #
###########

from typing import Optional
from sqlalchemy import create_engine, ForeignKey, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

########################
# Établir la connexion #
########################

connector = "mysql+pymysql"
user = "root"
password = "root"
host = "localhost"
database = "ma_base_de_donnees"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")
conn = engine.connect()

##########################
# Déclaration des Models #
##########################

class Base(DeclarativeBase):
    pass

"""
## mono-directionnel
class Parent(Base):
    __tablename__ = "t_parent"
    id: Mapped[int] = mapped_column(primary_key=True)
    les_enfants: Mapped["Child"] = relationship(secondary="association_table", back_populates="les_parents")
    child_associations: Mapped[list["Association"]] = relationship(
        back_populates="parent"
    )

class Association(Base):
    __tablename__ = "association_table"
    id_parent: Mapped[int] = mapped_column(ForeignKey("t_parent.id"), primary_key=True)
    id_enfant: Mapped[int] = mapped_column(ForeignKey("t_child.id"), primary_key=True)
    # association between Assocation -> Child
    les_enfants: Mapped["Child"] = relationship(back_populates="parent_associations")

    # association between Assocation -> Parent
    les_parents: Mapped["Parent"] = relationship(back_populates="child_associations")


class Child(Base):
    __tablename__ = "t_child"
    id: Mapped[int] = mapped_column(primary_key=True)
    les_parents: Mapped[list["Parent"]] = relationship(secondary="association_table", back_populates="les_enfants")
    parent_associations: Mapped[list["Association"]] = relationship(
        back_populates="les_enfants"
    )
    """
    
class Association(Base):
    __tablename__ = "association_table"

    left_id: Mapped[int] = mapped_column(
	    ForeignKey("left_table.id"), primary_key=True
	)
    right_id: Mapped[int] = mapped_column(
        ForeignKey("right_table.id"), primary_key=True
    )

    # association between Assocation -> Child
    child: Mapped["Child"] = relationship(back_populates="parent_associations")

    # association between Assocation -> Parent
    parent: Mapped["Parent"] = relationship(back_populates="child_associations")


class Parent(Base):
    __tablename__ = "left_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    # many-to-many relationship to Child, bypassing the `Association` class
    children: Mapped[list["Child"]] = relationship(
        secondary="association_table", back_populates="parents"
    )

    # association between Parent -> Association -> Child
    child_associations: Mapped[list["Association"]] = relationship(
        back_populates="parent"
    )


class Child(Base):
    __tablename__ = "right_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    # many-to-many relationship to Parent, bypassing the `Association` class
    parents: Mapped[list["Parent"]] = relationship(
        secondary="association_table", back_populates="children"
    )

    # association between Child -> Association -> Parent
    parent_associations: Mapped[list["Association"]] = relationship(
        back_populates="child"
    )