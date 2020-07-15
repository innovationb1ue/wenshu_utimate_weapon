from datetime import datetime
import pandas as pd

# discarded but not removed now
def date_handler(year, month, day):
    max_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for y in range(year, 2021):
        # check lunar year
        if y % 4 == 0:
            max_day[1] = 29
        else:
            max_day[1] = 28
        # loop to yield result
        for m in range(1, 13):
            if y == year and m < month:
                continue
            for d in range(1, max_day[m-1] + 1):
                if y == year and m == month and d < day:
                    continue
                yield datetime(y, m, d).isoformat().split('T')[0]

def date_handler2(y1, m1, d1, y2, m2, d2):
    stamps = pd.date_range(f'{m1}/{d1}/{y1}', f'{m2}/{d2}/{y2}')
    res = [i.isoformat().split('T')[0] for i in stamps]
    return res


if __name__ == '__main__':
    a = date_handler2(2005, 1, 1, 2006, 1, 1)


