class Voter(object):
    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            d['id'], 
            d['priority'],
            d['first_name'],
            d['last_name'],
            d['address'],
            d['was_sent_postcard'],
        )

    def __init__(self, id: str, priority: int, first_name: str, last_name: str, address: str, was_sent_postcard: bool):
        self._id = id
        self._priority = priority
        self._first_name = first_name
        self._last_name = last_name
        self._address = address
        self._was_sent_postcard = was_sent_postcard

    def to_dict(self) -> dict:
        return dict(
            id=self.id,
            priority=self._priority,
            first_name=self.first_name,
            last_name=self.last_name,
            address=self.address,
            was_sent_postcard=self.was_sent_postcard,
        )

    @property
    def id(self) -> str:
        return self._id

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def address(self) -> str:
        return self._address

    @property
    def priority(self) -> int:
        return self._priority

    @property
    def was_sent_postcard(self) -> str:
        return self._was_sent_postcard

    def __repr__(self):
        return 'Voter<%s, %s, %d>' % (self.last_name, self.first_name, self._priority)
