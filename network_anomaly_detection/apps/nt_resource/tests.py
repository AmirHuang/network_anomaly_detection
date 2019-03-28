# def count(n):
#     print("cunting")
#     while n > 0:
#         yield n  # 生成值：n
#         n -= 1
#
#
# c = count(10)
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())


# def count(n):
#     print("cunting")
#     while n > 0:
#         print('before yield')
#         yield n  # 生成值：n
#         n -= 1
#         print('after yield')
#
#
# for i in count(5):
#     print(i),

# list = [1, 2, 3, 4]
# it = iter(list)
#
# try:
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration as e:
#     print('xx')

# list = [1, 2, 3, 4]
# it = iter(list)
# for x in it:
#     print(x)

# list = [1, 2, 3, 4]
# it = iter(list)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break


# class mynumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
# myclass = mynumber()
#
# it = iter(myclass)
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
