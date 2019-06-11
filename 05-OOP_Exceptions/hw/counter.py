"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    per = 0
    original_init = cls.__init__

    def inner(*args, **kwargs):
        nonlocal per
        per += 1
        original_init(*args, **kwargs)

    def get_created_instances(*args, **kwargs):
        print(per)
        return per

    def reset_instances_counter(*args, **kwargs):
        nonlocal per
        temp = per
        per = 0
        print(temp)
        return temp

    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    cls.__init__ = inner
    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
