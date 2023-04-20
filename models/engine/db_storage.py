from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage():
    """
    DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Creates the engine and links it to the MySQL database and user created before (hbnb_dev and hbnb_dev_db).
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """
        Query on the current database session (self.__session) all objects depending of the class name (argument cls).
        """
        obj_dict = {}
        classes = [State, City, User, Place, Review, Amenity]
        if cls:
            if cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj
        else:
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """
        Add the object to the current database session (self.__session).
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session (self.__session).
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database (feature of SQLAlchemy).
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
