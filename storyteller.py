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
    """A story is like a unit test, but different.

    Each story is a collection of chapters. Each chapter builds upon previous
    chapters and develops the plot in preparation for those that follow.

    Yes, you can just use `unittest.TestCase` instead. But this way you don't
    have to listen to people complaining that you're doing unit tests wrong.

    These aren't unit tests, they're stories.
    """
    pass


class StoryLoader(unittest.TestLoader):
    """A test loader that finds tests in the order they appear in your code.

    By default, `unittest` finds tests by looking for method names prefixed
    with the string "test" and then runs them in their lexical sort order.

    This loader instead relies on an explicit registration step. This approach
    has two nice consequences:

      1. You can call your tests whatever you want.
      2. Your tests will run in the order in which you defined them.

    """
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
