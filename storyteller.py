import unittest


__all__ = [
    'Story',
    'StoryLoader',
    'chapter',
    'main',
]


class _Registry(object):
    def __init__(self):
        self.chapter = 0

    def register(self, func):
        self.chapter += 1
        func.chapter = self.chapter
        return func

chapter = _Registry().register


class Story(unittest.TestCase):
    pass


class StoryLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        chapters = []
        for attr_name in dir(testCaseClass):
            attr = getattr(testCaseClass, attr_name)
            if getattr(attr, 'chapter', None):
                chapters.append((attr.chapter, attr_name))
        return [c[1] for c in sorted(chapters)]


def main(*args, **kwargs):
    if 'testLoader' not in kwargs:
        kwargs['testLoader'] = StoryLoader()
    unittest.main(*args, **kwargs)


if __name__ == '__main__':
    main()
