from datetime import datetime


class Element:

    def __init__(self, value):
        self.__value = value
        self.__count = 0
        self.now()

    def now(self):
        time = datetime.now()
        self.__hour = time.hour
        self.__minute = time.minute
        self.__seconds = time.second

    def __str__(self):
        return (f'{self.__value}--{self.__hour}:{self.__minute}:{self.__seconds}({self.__count})')

    def set(self, value):
        self.__value = value
        self.now()
        self.__count += 1

    def get_value(self):
        self.now()
        self.__count += 1
        return self.__value

    def get_count(self):
        return self.__count

    def get_hour(self):
        return self.__hour

    def print_time(self):
        print(f'{self.__hour}:{self.__minute}:{self.__seconds}')

    def __eq__(self, obj):
        self.now()
        obj.now()
        self.__count += 1
        if self.__value == obj.__value:
            return True
        return False

    def __gt__(self, obj):
        self.now()
        obj.now()
        self.__count += 1
        obj.__count += 1
        if self.value > obj.value:
            return True
        return False

    def __lt__(self, obj):
        self.now()
        obj.now()
        self.__count += 1
        obj.__count += 1
        if self.value < obj.value:
            return True
        return False

    def increment_by(self, n):
        self.now()
        self.__count += 1
        self.__value += n

    def is_older(self, obj):
        if self.__hour <= obj.__hour and self.__minute <= obj.__minute and self.__seconds < obj.__seconds:
            return True
        return False

    def is_equal_time(self, obj):
        if self.__hour == obj.__hour and self.__minute == obj.__minute and self.__seconds == obj.__seconds:
            return True
        return False

    def is_more_frequent(self, obj):
        if self.__count > obj.__count:
            return True
        return False


def main():
    e1 = Element(234)
    e1.now()
    e1.set(234)
    print(e1.get_value())
    e2 = Element(234)
    # print(e1==e2)

    print(e1)
    print(e2)


main()
