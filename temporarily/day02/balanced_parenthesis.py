import pytest

class Solution:
    def balanced_parenthesis(self, expression):
        stack = []
        balanced = True
        matching_brackets = {")": "("}

        for n in expression:
            if n in matching_brackets:
                if stack and stack[-1] == matching_brackets[n]:
                    stack.pop()
                else:
                    balanced = False
                    break
            elif n in "(":
                stack.append(n)

        if stack:
            balanced = False

        if balanced:
            return "correct"
        else:
            return "incorrect"

    def balanced_parenthesis_2(self, expression):
        balanced = 0
        for n in expression:
            if n in "(":
                balanced += 1
            if n in ")":
                balanced -= 1
                if balanced < 0:
                    return "incorrect"

        if balanced == 0:
            return "correct"
        else:
            return "incorrect"


@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("(", "incorrect"),
        (")", "incorrect"),
        ("()", "correct"),
        (")(", "incorrect"),
        ("()(", "incorrect"),
        ("())", "incorrect"),
        ("(()", "incorrect"),
        (")()", "incorrect"),
        ("()()", "correct"),
        ("())(", "incorrect"),
        (")(()", "incorrect"),
        ("(())", "correct"),
        ("))((", "incorrect"),
        (")()(", "incorrect"),
        (")(()", "incorrect"),
        ("(()())", "correct"),
    ]
)
def test_balanced_parenthesis(expression, expected, solution):
    assert solution.balanced_parenthesis(expression) == expected

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("(", "incorrect"),
        (")", "incorrect"),
        ("()", "correct"),
        (")(", "incorrect"),
        ("()(", "incorrect"),
        ("())", "incorrect"),
        ("(()", "incorrect"),
        (")()", "incorrect"),
        ("()()", "correct"),
        ("())(", "incorrect"),
        (")(()", "incorrect"),
        ("(())", "correct"),
        ("))((", "incorrect"),
        (")()(", "incorrect"),
        (")(()", "incorrect"),
        ("(()())", "correct"),
    ]
)
def test_balanced_parenthesis_2(expression, expected, solution):
    assert solution.balanced_parenthesis_2(expression) == expected
