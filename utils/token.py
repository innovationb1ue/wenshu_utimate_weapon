import random


class RequestVerificationToken(str):
    def __new__(cls, size: int):
        arr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        string = "".join(arr[round(random.random() * (len(arr) - 1))] for _ in range(size))
        return super(RequestVerificationToken, cls).__new__(cls, string)

if __name__ == '__main__':
    print(RequestVerificationToken(24))
