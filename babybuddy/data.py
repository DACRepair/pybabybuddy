import datetime


class BBAPIBaseObject:
    __identifier__ = 'id'

    def __init__(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)
        if not hasattr(self, self.__identifier__):
            raise ValueError(f"Invalid {type(self).__name__} Object: {str(data)}")

    def __str__(self):
        return f"BBAPIObject: {type(self).__name__}"

    def __repr__(self):
        return self.__str__()


class Child(BBAPIBaseObject):
    id: int
    first_name: str
    last_name: str
    birth_date: datetime.date
    slug: str
    picture: str

    def __init__(self, data: dict):
        super(Child, self).__init__(data)

        if hasattr(self, "birth_date"):
            self.birth_date = datetime.date(*[int(x) for x in str(self.birth_date).split("-")])

    def __str__(self):
        return f"<Child ID: {self.id}: {self.first_name} {self.last_name}>"


class Diaper(BBAPIBaseObject):
    id: int
    child: int
    time: datetime.datetime
    wet: bool
    solid: bool
    color: str
    amount: float
    notes: str

    def __init__(self, data: dict):
        super(Diaper, self).__init__(data)
        if hasattr(self, "time"):
            fmttime = "{dt}{tz}".format(dt=str(self.time[0:-6]), tz=str(self.time[-6:]).replace(":", ""))
            self.time = datetime.datetime.strptime(fmttime, "%Y-%m-%dT%H:%M:%S%z")

    def __str__(self):
        return f"<Diaper ID: {self.id}: Child {self.child}, {self.time}>"


class Feeding(BBAPIBaseObject):
    id: int
    child: int
    start: datetime.datetime
    end: datetime.datetime
    duration: int
    type: str
    method: str
    amount: float
    notes: str

    def __init__(self, data: dict):
        super(Feeding, self).__init__(data)
        if hasattr(self, "start"):
            fmttime = "{dt}{tz}".format(dt=str(self.start[0:-6]), tz=str(self.start[-6:]).replace(":", ""))
            self.start = datetime.datetime.strptime(fmttime, "%Y-%m-%dT%H:%M:%S%z")

        if hasattr(self, "end"):
            fmttime = "{dt}{tz}".format(dt=str(self.end[0:-6]), tz=str(self.end[-6:]).replace(":", ""))
            self.end = datetime.datetime.strptime(fmttime, "%Y-%m-%dT%H:%M:%S%z")

        if hasattr(self, "duration"):
            h, m, s = (int(x) for x in str(self.duration).split(":"))
            self.duration = (((h * 60) + m) * 60) + s

    def __str__(self):
        return f"<Feeding ID: {self.id}: Child {self.child}, {self.start}, {self.duration}s>"
