from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

# Import new classes so they are registered with FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review