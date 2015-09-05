from TestCase	import TestCase
from WasRun	import WasRun

class TestCaseTest(TestCase):
	def testRunning(self):
		test = WasRun("testMethod")
		test.run()
		assert(test.wasRun)
	
	def testSetUp(self):
		test = WasRun("testMethod")
		test.run()
		assert(test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
