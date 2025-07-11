from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine("postgresql://postgres.neixxnuamvgetnmyanbz:Gxo2lMla4Stur9vq@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres")

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()