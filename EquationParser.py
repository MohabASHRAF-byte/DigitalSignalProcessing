import operator
import re

from Signal import Signal

ops = {
    '+': (1, operator.add, 'left'),
    '-': (1, operator.sub, 'left'),
    '*': (2, operator.mul, 'left'),
    '/': (2, operator.truediv, 'left'),
}

class EquationParser:

    def __init__(self, variables: dict = None):
        self.variables = variables if variables else {}

    def add_variable(self, key: str, value: float):
        """Add or update a variable in the dictionary."""
        self.variables[key] = value

    def remove_variable(self, key: str):
        """Remove a variable from the dictionary."""
        if key in self.variables:
            del self.variables[key]

    def clear_variables(self):
        """Clear all variables from the dictionary."""
        self.variables.clear()

    @staticmethod
    def __tokenize(expression: str) -> list[str]:
        """Tokenize the input expression."""
        pattern = r'\d+\.\d+|\d+|[a-zA-Z_]\w*|[()+\-*/]'
        tokens = re.findall(pattern, expression)
        return tokens
    @staticmethod
    def __convert(tokens: list[str]) -> list[str]:
        """Convert the token list into postfix notation using the Shunting-yard algorithm."""
        output = []
        operators = []

        for token in tokens:
            if token.isalnum():  # Variables or numbers
                output.append(token)
            elif re.match(r"^\d+\.\d+$", token):  # Handle floating-point numbers
                output.append(float(token))
            elif token == '(':  # Left parenthesis
                operators.append(token)
            elif token == ')':  # Right parenthesis
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove the '(' from operators
            else:  # Operators (+, -, *, /)
                while operators and operators[-1] != '(' and (
                        ops[token][0] < ops[operators[-1]][0] or
                        (ops[token][0] == ops[operators[-1]][0] and ops[token][2] == 'left')
                ):
                    output.append(operators.pop())
                operators.append(token)

        # Append remaining operators
        while operators:
            output.append(operators.pop())

        return output

    def __evaluate_postfix(self, postfix: list[str]) -> float:
        """Evaluate the postfix expression."""
        stack = []

        for token in postfix:
            if re.match(r"^\d+\.\d+$", str(token)):  # Handle floating-point numbers
                stack.append(float(token))
            elif token.isdigit():  # Handle integer numbers
                stack.append(int(token))
            elif token in ops:  # Apply operators
                b = stack.pop()
                a = stack.pop()
                result = ops[token][1](a, b)
                stack.append(result)
            else:  # Handle variables (Signal or float)
                variable = self.variables.get(token, 0)
                stack.append(variable)

        return stack[0]

    def evaluate(self, expression: str):
        """Public method to evaluate a mathematical expression."""
        tokens = self.__tokenize(expression)
        postfix = self.__convert(tokens)
        result = self.__evaluate_postfix(postfix)
        return result

    # New methods for managing the variables dictionary

