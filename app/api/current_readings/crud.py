from app.api.base.functions import BaseCRUD
from app.models import CurrentReadings


class CurrentReadingsCRUD(BaseCRUD):
    model = CurrentReadings
