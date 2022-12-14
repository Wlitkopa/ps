
import sys
sys.path.append("/home/przemek/PycharmProjects/ps/lab3_4")
from DeanerySystem import day
from DeanerySystem.day import Day, nthDayFrom, Action
from DeanerySystem import term
from DeanerySystem.term import Term, DayToStr
from enum import Enum, IntEnum

# from DeanerySystem import Break
# from lab3_4.DeanerySystem.Break import Break

# if __name__ == "__main__":
#     from DeanerySystem.TimetableWithoutBreaks import TimetableWithoutBreaks
#     from DeanerySystem.TimetableWithoutBreaks import *
# import DeanerySystem.TimetableWithoutBreaks


def yeartoString(year):
    if int(year) == 1:
        return "Pierwszy"
    elif int(year) == 2:
        return "Drugi"
    elif int(year) == 3:
        return "Trzeci"
    elif int(year) == 4:
        return "Czwarty"
    elif int(year) == 5:
        return "Piąty"
    elif int(year) == 6:
        return "Szósty"
    elif int(year) == 7:
        return "Siódmy"


def sctoStrign(sc):  # sc - studies category (fulltime, parttime)
    if sc:
        return "stacjonarnych"
    else:
        return "niesacjonarnych"


class Lesson:

    #                                              hours for friday
    ft_limit = [Day.MON, Day.THU, [8, 0], [20, 0], [8, 0], [17, 0]]
    pt_limit = [Day.SAT, Day.SUN, [8, 0], [20, 0], [17, 0], [20, 0]]
    entries = []

    def __init__(self, timetable, termin, name, teacherName, year, fulltime=None):

        self.termin = termin
        self.name = name
        self.teacherName = str(teacherName)
        self.year = year
        self.fulltime = fulltime
        self.timetable = timetable


        # if timetable.put(self):
        #     # print("Lesson was added")
        #     self.timetable = timetable
        # else:
        #     self.timetable = timetable

    @property
    def timetable(self):
        return self.__timetable

    @timetable.setter
    def timetable(self, timetable):

        try:
            if timetable.secret == 10:
                timetable.put(self)
                self.__timetable = timetable
            else:
                raise TypeError("Timetable powinien być obiektem klasy timetable")

        except AttributeError:
            raise TypeError("Timetable powinien być obiektem klasy timetable")

        self.__timetable = timetable


    @property
    def termin(self):
        return self.__termin

    @termin.setter
    def termin(self, termin):

        if isinstance(termin, Term):
            self.__termin = termin
        else:
            raise TypeError("Termin powinien być obiektem klasy Term")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def teacherName(self):
        return self.__teacherName

    @teacherName.setter
    def teacherName(self, teacherName):
        self.__teacherName = teacherName

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):

        try:
            if 0 < int(year) < 5:
                self.__year = year
            else:
                raise TypeError("Rok powinien mieć wartość 1, 2, 3 lub 4")
        except ValueError:
            raise ValueError("Rok powinien być liczbą")

        self.__year = year

    @property
    def fulltime(self):
        return self.__fulltime

    @fulltime.setter
    def fulltime(self, fulltime):
        if fulltime is not None:
            self.__fulltime = False
        else:
            self.__fulltime = True

    def __str__(self):
        minutes = int(int(self.termin.duration) % 60)
        hours = int((int(self.termin.duration) - minutes)/60)
        new_minute = (int(self.termin.minute) + minutes) % 60
        new_hour = int(self.termin.hour) + hours + int((int(self.termin.minute) + minutes - new_minute)/60)

        if new_minute == 0:
            new_minute = str('00')

        return f"{self.name} ({DayToStr(self.termin.day)} {self.termin.hour}:{self.termin.minute} - {new_hour}:{new_minute})" \
               f"\n{yeartoString(self.year)} rok studiów {sctoStrign(self.fulltime)}" \
               f"\nProwadzący: {self.teacherName}"

    # @staticmethod
    # def busy(termin):
    #     t_min_start = termin.hour*60 + termin.minute  # godzina rozpoczęcia terminu w minutach
    #     t_min_end = t_min_start + termin.duration  # godzina zakończenia terminu w minutach
    #
    #     for lesson in Lesson.entries:
    #         # print("lesson: ", lesson)
    #         if termin._Term__day == lesson.termin._Term__day:
    #             # print("t_min_start: ", t_min_start)
    #             # print("t_min_end: ", t_min_end)
    #             l_min_start = lesson.termin.hour * 60 + lesson.termin.minute  # godzina rozpoczęcia lekcji w minutach
    #             l_min_end = l_min_start + lesson.termin.duration  # godzina zakończenia lekcji w minutach
    #             # print("l_min_start: ", l_min_start)
    #             # print("l_min_end: ", l_min_end)
    #             if t_min_start < l_min_start or t_min_start >= l_min_end:
    #                 if t_min_end <= l_min_start or t_min_end > l_min_end:
    #                     if not (t_min_start < l_min_start and t_min_end > l_min_end):
    #                         pass
    #                     else:
    #                         return False
    #                     pass
    #                 else:
    #                     return False
    #             else:
    #                 return False
    #     return True
    #
    # @staticmethod
    # def fit(termin, fulltime):
    #     limit = []
    #     if fulltime:
    #         limit = Lesson.ft_limit
    #     else:
    #         limit = Lesson.pt_limit
    #     t_min_start = termin.hour * 60 + termin.minute  # godzina rozpoczęcia terminu w minutach
    #     t_min_end = t_min_start + termin.duration  # godzina zakończenia terminu w minutach
    #     # print("\n\nLesson.ft_limit[0].value (czyli monday): ", limit[0].value)
    #     # print("termin._Term__day: ", termin._Term__day)
    #     # print("Lesson.ft_limit[0].value: ", limit[0].value)
    #     # print("Lesson.ft_limit[1].value: ", limit[1].value)
    #     # print("\n\n")
    #
    #     if limit[0].value <= termin.day <= limit[1].value:
    #         # print("Zaszedł if")
    #         z_min_start = limit[2][0]*60 + limit[2][1]  # godzina rozpoczęcia zajęć pn-czw w minutach
    #         z_min_end = limit[3][0]*60 + limit[3][1]  # godzina zakończenia zajęć pn-czw w minutach
    #         if z_min_start <= t_min_start < z_min_end and z_min_start < t_min_end <= z_min_end:
    #             return True
    #     elif termin.day == Day.FRI.value:
    #         # print("Zaszedł elif")
    #         z_min_start = limit[4][0] * 60 + limit[4][1]  # godzina rozpoczęcia zajęć pt w minutach
    #         z_min_end = limit[5][0] * 60 + limit[5][1]  # godzina zakończenia zajęć pt w minutach
    #         if z_min_start <= t_min_start < z_min_end and z_min_start < t_min_end <= z_min_end:
    #             return True
    #     return False

    def earlierDay(self):
        # print("dir(self.term): ", dir(self.termin))
        Day.new_day = (self.termin.day + 6) % 7


        # print(f"\nself.term._Term__day: {self.termin.day}")
        # print("self: ", self)

        temp_term = Term(Day.new_day, self.termin.hour, self.termin.minute, self.termin.duration)

        # print("Nowy potencjalny termin: ", temp_term)


        # print("temp_term: ", temp_term)
        # print("\n")
        #
        # if self.fulltime:
        #     state = "fulltime"
        # else:
        #     state = "parttime"
        #
        # if Lesson.busy(temp_term):
        #     print("\nTermin jest wolny\n")
        # else:
        #     print("\nTermin jest zajęty\n")
        #
        # if Lesson.fit(temp_term, self.fulltime):
        #     print(f"\nTen termin zawiera się w ograniczeniu czasowym {state}\n")
        # else:
        #     print(f"\nTen termin nie jest w ograniczeniu czasowym {state}\n")

        if self.timetable.can_be_transferred_to(temp_term, self.fulltime):
            del self.timetable.dictionary[self.termin]
            self.timetable.dictionary[temp_term] = self
            self.termin = temp_term
            # print(f"\n\nPo zmianach: {self}\n\n")
            return True
        else:
            return False

    def laterDay(self):
        Day.new_day = (self.termin.day + 1) % 7

        temp_term = Term(Day.new_day, self.termin.hour, self.termin.minute, self.termin.duration)

        # print("temp_term: ", temp_term)
        #
        # if self.fulltime:
        #     state = "fulltime"
        # else:
        #     state = "parttime"
        #
        # if Lesson.busy(temp_term):
        #     print("Termin jest wolny")
        # else:
        #     print("Termin jest zajęty")
        #
        # if Lesson.fit(temp_term, self.fulltime):
        #     print(f"Ten termin zawiera się w ograniczeniu czasowym {state}")
        # else:
        #     print(f"Ten termin nie jest w ograniczeniu czasowym {state}")

        if self.timetable.can_be_transferred_to(temp_term, self.fulltime):
            del self.timetable.dictionary[self.termin]
            self.timetable.dictionary[temp_term] = self
            self.termin = temp_term
            # print(f"\n\nPo zmianach: {self}\n\n")
            return True
        else:
            return False

    def earlierTime(self):
        # print("\n\n EARLIER TIME\n\n")
        minutes = int(int(self.termin.duration) % 60)
        hours = int((int(self.termin.duration) - minutes) / 60)
        new_minute = int(self.termin.minute) - minutes
        if new_minute < 0:
            hours += 1
            new_minute += 60
        new_hour = int(self.termin.hour) - hours

        temp_term = Term(self.termin.day, new_hour, new_minute, self.termin.duration)

        # print("temp_term: ", temp_term)

        # if self.fulltime:
        #     state = "fulltime"
        # else:
        #     state = "parttime"
        #
        # if Lesson.busy(temp_term):
        #     print("\nTermin jest wolny")
        # else:
        #     print("\nTermin jest zajęty")
        #
        # if Lesson.fit(temp_term, self.fulltime):
        #     print(f"Ten termin zawiera się w ograniczeniu czasowym {state}\n")
        # else:
        #     print(f"Ten termin nie jest w ograniczeniu czasowym {state}\n")

        if self.timetable.can_be_transferred_to(temp_term, self.fulltime, False):
            del self.timetable.dictionary[self.termin]
            self.timetable.dictionary[temp_term] = self
            self.termin = temp_term
            # print(f"\n\nPo zmianach: {self}\n\n")
            return True
        else:
            return False

    def laterTime(self):
        minutes = int(int(self.termin.duration) % 60)
        hours = int((int(self.termin.duration) - minutes) / 60)
        new_minute = (int(self.termin.minute) + minutes) % 60
        new_hour = int(self.termin.hour) + hours + int((int(self.termin.minute) + minutes - new_minute) / 60)

        temp_term = Term(self.termin.day, new_hour, new_minute, self.termin.duration)

        # print("temp_term: ", temp_term)

        # if self.fulltime:
        #     state = "fulltime"
        # else:
        #     state = "parttime"
        #
        # if Lesson.busy(temp_term):
        #     print("\nTermin jest wolny")
        # else:
        #     print("\nTermin jest zajęty")
        #
        # if Lesson.fit(temp_term, self.fulltime):
        #     print(f"Ten termin zawiera się w ograniczeniu czasowym {state}\n")
        # else:
        #     print(f"Ten termin nie jest w ograniczeniu czasowym {state}\n")
        #
        # print("Termin przed zmianą: ", temp_term)

        if self.timetable.can_be_transferred_to(temp_term, self.fulltime, True):
            # print("Termin po sprawdzeniu: ", temp_term)
            del self.timetable.dictionary[self.termin]
            self.timetable.dictionary[temp_term] = self
            self.termin = temp_term
            # print(f"\n\nPo zmianach: {self}\n\n")
            return True
        else:
            return False


# timetable = TimetableWithoutBreaks()
# term1 = Term(Day.MON, 8, 0)
# lesson = Lesson(timetable, term1, "Podstawy programowania", "Stanisław Polak", 2)

