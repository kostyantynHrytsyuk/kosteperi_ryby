"""Shoty"""

class DrinkLimitException(Exception):
    pass

class NoShotsException(Exception):
    pass

class TooManyPeopleException(Exception):
    pass

class ShotyTam:
    """main shoty class"""
    __queue = []
    def __init__(self, people, shots, cocktails) -> None:
        self.people = people
        self.shots = shots
        self.cocktails = cocktails

    @classmethod
    def add_to_queue(cls, drink):
        """
        adds to queue
        """
        cls._ShotyTam__queue.append(drink)

    def __str__(self) -> str:
        if self.people != 0:
            return f"Bar contains {self.people} people, has {self.shots}\
 availabe shots and {self.cocktails} cocktails"
        return f"Bar is full of people, has {self.shots} availabe shots and\
 {self.cocktails} cocktails"


class Drink:
    """drink"""
    def __init__(self, taste, label) -> None:
        self.taste = taste
        self.label = label

    def __str__(self) -> str:
        return f"{self.taste} {self.__class__.__name__.lower()} with {self.label} label"

    def __eq__(self, __value: object) -> bool:
        if self.label == __value.label and self.taste == __value.taste:
            return True
        return False

class Shot(Drink):
    """Student can drink it"""
    def __init__(self, taste, label) -> None:
        super().__init__(taste, label)

class Cocktail(Drink):
    """Student can drink it"""
    def __init__(self, taste, label) -> None:
        super().__init__(taste, label)

class Student:
    """Parent class for students"""
    def __init__(self, barr) -> None:
        self.barr = barr
        if self.barr.people == 0:
            raise TooManyPeopleException
        self.barr.people -= 1
        self.shots = 0
        self.cocktails = 0
        self.can_drink = True
        self.can_dance = True

    def __str__(self) -> str:
        return f"{self.__class__.__name__.split('s')[0]} student wants to \
drink {self.shots} shots and {self.cocktails} cocktails"

class LNUstudent(Student):
    """can drink 6 shots 1 cocktail"""
    def __init__(self, barr) -> None:
        super().__init__(barr)

    def set_drinks(self, drinks):
        """
        set drinks to the student
        """
        for elm in drinks:
            if isinstance(elm, Shot):
                if self.shots != 6:
                    if self.barr.shots == 0:
                        raise NoShotsException
                    self.shots += 1
                    self.barr.shots -= 1
                    ShotyTam.add_to_queue(elm)
            if isinstance(elm, Cocktail):
                if self.cocktails != 1:
                    self.cocktails += 1
                    self.barr.cocktails -= 1
                    ShotyTam.add_to_queue(elm)
        self.can_drink = self.shots != 6 | self.cocktails != 1
        self.can_dance = self.can_drink

class NULPstudent(Student):
    """can drink 4 shots 4 cocktails"""
    def __init__(self, barr) -> None:
        super().__init__(barr)

    def set_drinks(self, drinks):
        """
        set drinks to the student
        """
        for elm in drinks:
            if isinstance(elm, Shot):
                if self.shots != 4:
                    if self.barr.shots == 0:
                        raise NoShotsException
                    self.shots += 1
                    self.barr.shots -= 1
                    ShotyTam.add_to_queue(elm)
            if isinstance(elm, Cocktail):
                if self.cocktails != 4:
                    self.cocktails += 1
                    self.barr.cocktails -= 1
                    ShotyTam.add_to_queue(elm)
        self.can_drink = self.shots != 4 or self.cocktails != 4
        self.can_dance = self.can_drink


class UCUstudent(Student):
    """can drink 10 shots"""
    def __init__(self, barr) -> None:
        super().__init__(barr)

    def set_drinks(self, drinks):
        """
        set drinks to the student
        """
        for elm in drinks:
            if isinstance(elm, Shot):
                if self.shots != 10:
                    if self.barr.shots == 0:
                        raise NoShotsException
                    self.shots += 1
                    self.barr.shots -=1
                    ShotyTam.add_to_queue(elm)
        self.can_drink = self.shots != 10
        self.can_dance = self.can_drink
