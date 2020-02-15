# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError('input error!')
        elif self.score >= 80 and self.score <=100:
            return 'A'
        elif self.score >= 60 and self.score <=80:
            return 'B'
        return 'C'
