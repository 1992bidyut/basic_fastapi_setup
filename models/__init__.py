from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from models.parties.parties_models import Parties
from models.parties.parties_address_model import PartiesAddress