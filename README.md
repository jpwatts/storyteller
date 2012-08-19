# Storyteller

It all started because [Eloy][] made me want to write functional tests using
Selenium.

I wanted each test to tell a user's story. So I started writing a unit test and 
pretty soon I was thinking "Wow, this function is getting really long. I should
break it up into more manageable chunks."

Everything went downhill from there. In order to get the smaller functions to
run in the right order, I ended up writing something like this:

    import unittest

    class UserStory(unittest.TestCase):
        def test_1(self):
            pass

        def test_2(self):
            pass

        ...

        def test_n(self):
            pass

    if __name__ == '__main__':
        unittest.main()

But then I wondered what would happen if I decided to move things around. What
if test four should really be test two? That means that test two becomes test
three and test three becomes test four and test four becomes... Uh oh.

Enter Storyteller.

Storyteller solves this problem with explicit test registration.

    import storyteller

    class UserStory(storyteller.Story):
        @storyteller.chapter
        def introduction(self):
            pass

        @storyteller.chapter
        def in_which_something_happens(self):
            pass

        ...

        @storyteller.chapter
        def conclusion(self):
            pass

    if __name__ == '__main__':
        storyteller.main()

Registration has two nice consequences:

  1. No more "test" prefixes. You can call your tests whatever you want.
  2. Your tests will run in the same order as they appear in your code.

And since a `storyteller.Story` is just a `unittest.TestCase` under the hood,
you can still assert to your heart's content. The big difference is that now you
can focus on your user's story and let the computer worry about the bookkeeping.

[Eloy]: http://www.meetup.com/Django-Houston/events/66872662/
