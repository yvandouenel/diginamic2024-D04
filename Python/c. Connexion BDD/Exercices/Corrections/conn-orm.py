###########
# IMPORTS #
###########

from typing import Optional
from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

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

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] =  mapped_column(String(30))
    fullname: Mapped[Optional[str]] =  mapped_column(String(50))
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
    # (id=1, name="Robin", fullname="Robin Hotton")

# créer les tables par rapport aux héritage
Base.metadata.create_all(engine)

########
# CRUD #
########

with Session(engine) as session:
    ##### creation #####
    spongebob = User(name="spongebob", fullname="spongebob Squarepants")
    sandy = User(name="sandy", fullname="Sandy Cheeks")
    patrick = User(name="patrick", fullname="Patrick Star")
    
    session.add_all([spongebob, sandy, patrick])
    # session.add(patrick)
    session.commit()
    
    ##### delete #####
    resultat = select(User).where(User.id == 1)
    id_un = session.scalars(resultat).one()
    session.delete(id_un)
    
    ##### update #####
    resultat = select(User).where(User.id == 2)
    id_un = session.scalars(resultat).one()
    id_un.fullname = "pas si carré que ça"
    session.commit()
    
    ##### lecture #####
    result = select(User).where(User.name.in_(["spongebob", "sandy"]))
    # result = select(User).where(User.name == "spongebob")
    # result = select(User).where(User.name == "sandy")
    session.commit()
    
    for user in session.scalars(result):
        print(user)

#############
# FERMETURE #
#############

session.close()