Test.describe("Basic tests") do
Test.assert_equals(basic_op('+', 4, 7), 11)
Test.assert_equals(basic_op('-', 15, 18), -3)
Test.assert_equals(basic_op('*', 5, 5), 25)
Test.assert_equals(basic_op('/', 49, 7), 7)
end