class TestSuite

	def __init__(self):
		self.tests = []

	def add(self, test):
		self.test.append(test)

	def run(self):
		result = TestResult()
		
		for test in tests:
			test.run(result)

		return result