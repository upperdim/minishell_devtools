import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from parser import  validate_quotes


def quote_validation_tests():
	quote_val_tests = [
		['', True],
		['\'', False],
		['\"', False],
		['\'\'', True],
		['""', True],
		['\'\'\'', False],
		['"""', False],
		[' " \' " ', True],
		[' " \' " \' " ', False],
	]

	print(f'Running {len(quote_val_tests)} quote validation tests...')

	failed_count = 0
	for i, test in enumerate(quote_val_tests):
		# print(f'i={i} test case = {test[0]}')
		actual = validate_quotes(test[0])
		expected = test[1]
		if actual != expected:
			failed_count += 1
			print(f'\nFailed test {i + 1}')
			print(f'Test case = {test[0]}')
			print(f'Actual    = {actual}')
			print(f'Expected  = {expected}')
	if failed_count == 0:
		print(f'OK')
	else:
		print(f'\nFailed {failed_count} tests.')
