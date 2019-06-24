"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые, я бы смог бы проверить их корректность
"""
import pytest
import task1
import task2
import task3


@pytest.mark.parametrize('a, expected', [
    (task1.file1 in task1.folder1, True),
    (task1.file2 in task1.folder1, True),
    (task1.file3 in task1.folder1, True),
    (task1.file4 in task1.folder1, False),
    (task1.file1 in task1.folder3, False)
])
def test_task1_1(a, expected):
    assert a == expected


@pytest.mark.parametrize('a, expected', [
    (str(task1.folder1), 'V folder1\n'
                         '|-> V folder2\n'
                         '|   |-> V folder3\n'
                         '|   |   |-> file3\n'
                         '|   |-> file2\n'
                         '|-> file1'),
    (str(task1.folder2), 'V folder2\n'
                         '|-> V folder3\n'
                         '|   |-> file3\n'
                         '|-> file2')
])
def test_task1_2(a, expected):
    assert a == expected


def test_task2():
    assert task2.vertices == ['A', 'B', 'C', 'D']


@pytest.mark.parametrize('a, expected', [
    (task3.a.message, 'efg'),
    (task3.a.another_message, 'olssv'),
    (task3.a.mesg, 'same'),
])
def test_task3(a, expected):
    assert a == expected
