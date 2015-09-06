from TestCase	import TestCase
from WasRun	import WasRun

class TestCaseTest(TestCase):
	def setUp(self):
		self.test = WasRun("testMethod")

	def testTemplateMethod(self):
		self.test.run()
		assert("setUp testMethod " == self.test.log)

	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod " == test.log)

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testSetUp").run()
