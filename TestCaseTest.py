from TestCase import TestCase
from WasRun	import WasRun

class TestCaseTest(TestCase):
	def setUp(self):
		self.test = WasRun("testMethod")

	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod tearDown " == test.log)

	def testResult(self):
		test = WasRun("testMethod")
		result = test.run()
		assert("1 run, 0 failed" == result.summary())

	def testFailedResult(self):
		test = WasRun("testBrokenMethod")
		result = test.run()
		assert("1 run, 1 failed" == result.summary())

	def testFailedResultFormmatting(self):
		result = TestResult()
		result.testStarted()
		result.testFailed()
		assert("1 run, 1 failed" == result.summary())

	def testSuite(self):
		suite = TestSuite()
		suite.add(WasRun("testMethod"))
		suite.add(WasRun("testBrokenMethod"))
		result = TestResult()
		suite.run(result)
		assert("2 run, 1 failed" == result.summary())


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResultFormmatting").run()
TestCaseTest("testFailedResult").run()
TestCaseTest("testSuite").run()