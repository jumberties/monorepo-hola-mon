from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import os
import time

# --- Connexió flexible per Clever Cloud o local ---
DATABASE_URL = (
    os.getenv("POSTGRESQL_ADDON_URI")  # Clever Cloud
    or os.getenv("DATABASE_URL")          # Altres entorns (Heroku, etc.)
    or "postgresql://user:password@localhost:5432/testdb"  # Local
)

# --- Configuració SQLAlchemy ---
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Model senzill ---
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)


# --- Inicialització de la base de dades ---
def init_db(retries: int = 5, delay: int = 3):
    """Crea taules i registre inicial. Torna a provar si la BD encara no està llesta."""
    for attempt in range(retries):
        try:
            Base.metadata.create_all(bind=engine)
            db = SessionLocal()
            if db.query(Message).count() == 0:
                db.add(Message(text="Hola món des de PostgreSQL!"))
                db.commit()
                print("✅ Base de dades inicialitzada correctament.")
            db.close()
            return
        except OperationalError as e:
            print(f"⚠️ Error connectant a la BD (intent {attempt+1}/{retries}): {e}")
            time.sleep(delay)
    print("❌ No s'ha pogut inicialitzar la base de dades després de diversos intents.")

