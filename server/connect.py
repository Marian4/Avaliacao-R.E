from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    
    def session():
        connection_string = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
            "root",
            "ladossifpb",
            "127.0.0.1",
            "3306",
            "nutrif"
        )

        engine = create_engine(connection_string, echo=False)
        Session = sessionmaker(bind=engine)

        return Session()
