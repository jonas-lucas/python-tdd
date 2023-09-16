# 2. The TDD Cycle - Red-Green-Refactor

Test-driven development is:

![Test-Driven Development Flowchart](test-driven-development-flowchart.webp)

**Red:** Firstly write a test.

**Green:** Write a code to pass the test.

**Refactor:** Improve the code.

### Steps of Refactor

**Arrange:** Set up the context for the test.

**Act:** Perform the action that we want to test.

**Assert:** Assert that the outcome was an expected.

### SetUp Method

Can instance only one object for all tests.

```python
import unittest

class ClassTest(unittest.TestCase):
    def setUp(self):
        self.obj = Class()

    def test_something(self):
        self.assertIsNone(self.obj.something)
```
