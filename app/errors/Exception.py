class NotFoundException(Exception):
    def __init__(self, model=None, field=None, item_id=None):
        self.model = model
        self.field = field
        self.item_id = item_id


class UniqueException(Exception):
    def __init__(self, model=None, field=None, item_id=None):
        self.model = model
        self.field = field
        self.item_id = item_id


class Unauthorized(Exception):
    pass
