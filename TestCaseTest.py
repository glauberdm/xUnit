from TestCase	import TestCase
from WasRun	import WasRun

class TestCaseTest(TestCase):
	def setUp(self):
		self.test = WasRun("testMethod")

	def testTemplateMethod(self):
		self.test.run()
		assert("setUp testMethod " == self.test.log)

	def testTemplateMethod(self):
		self.test.run()
		assert("setUp testMethod " == self.test.log)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
