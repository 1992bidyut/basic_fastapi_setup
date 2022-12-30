from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from app.models.parties.parties_models import Parties
from app.models.parties.parties_address_model import PartiesAddress
from app.models.mokam.mokam_model import Mokam
