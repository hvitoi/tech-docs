# Test Double

A Test Double is a general term from software testing (especially unit testing) that refers to any kind of object that replaces a real component in tests. The name comes from the idea of a stunt double in movies, it steps in for the real actor during risky scenes.

There are several types of test doubles, each with a specific purpose:

-`Dummy`: Passed around but never actually used. It just fills a parameter list.
-`Stub`: Provides predefined answers to method calls, usually used to control the test’s environment.
-`Fake`: Has a working implementation, but it’s simpler or unsuitable for production (e.g., an in-memory database).
-`Spy`: Like a stub, but also records information about how it was called (e.g., number of invocations, arguments).
-`Mock`: Pre-programmed with expectations about calls; verifies that the code under test interacts correctly with it.
