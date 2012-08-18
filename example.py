import storyteller


class ExampleStory(storyteller.Story):
    @storyteller.chapter
    def foo(self):
        pass

    @storyteller.chapter
    def bar(self):
        pass

    @storyteller.chapter
    def baz(self):
        pass


if __name__ == '__main__':
    storyteller.main()
