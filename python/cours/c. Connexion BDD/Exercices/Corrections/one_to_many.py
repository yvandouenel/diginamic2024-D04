###########
# IMPORTS #
###########

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

## bi-directionnel

# one
class Ecole(Base):
    __tablename__ = "t_ecole"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(30))
    eleves: Mapped[list["Eleve"]] = relationship(back_populates="ecole")

    def __repr__(self):
        return f"<Ecole(id={self.id}, nom='{self.nom}')>"

# many
class Eleve(Base):
    __tablename__ = "t_eleve"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(30))
    ecole_id: Mapped[int] = mapped_column(ForeignKey("t_ecole.id"))
    ecole: Mapped["Ecole"] = relationship(back_populates="eleves")
    
    def __repr__(self):
        return f"<Eleve(id={self.id}, nom='{self.nom}', ecole_id={self.ecole_id})>"

    
Base.metadata.create_all(engine)

with Session(engine) as session:
    # CREATE
    diginamic = Ecole(nom="Diginamic")
    benjamin = Eleve(nom="Benjamin", ecole=diginamic)
    session.add_all([diginamic, benjamin])
    session.commit()
    
    # READ
    stmt = select(Eleve).join(Ecole).where(Ecole.nom == "Diginamic").where(Eleve.nom == "benjamin")
        
    eleves = session.scalars(stmt).all()
    print("\nEleves:")
    for eleve in eleves:
        print(eleve)
