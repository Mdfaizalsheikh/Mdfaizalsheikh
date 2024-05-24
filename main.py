import re

def interpret(code):
    variables = {}
    lines = code.split('\n')

    for line in lines:
        line = line.strip()
        if line.startswith('giggle'):
            text = re.findall(r'giggle\("([^"]*)"\)', line)
            if text:
                print(text[0])
        elif line.startswith('bloop'):
            match = re.match(r'bloop (\w+) = (.+)', line)
            if match:
                var_name, value = match.groups()
                variables[var_name] = eval(value, {}, variables)
        elif any(op in line for op in ['twiddle', 'wiggle', 'flip', 'flop']):
            var_name, expression = line.split(' = ')
            var_name = var_name.replace('bloop ', '').strip()
            expression = expression.replace('twiddle', '+').replace('wiggle', '-').replace('flip', '*').replace('flop', '/')
            variables[var_name] = eval(expression, {}, variables)
        elif line.startswith('if'):
            condition = re.findall(r'if \((.*)\) then \{', line)[0]
            condition = condition.replace('flop', '/')
            if eval(condition, {}, variables):
                body = re.findall(r'\{(.*)\}', line, re.DOTALL)[0].strip()
                interpret(body)
        elif line.startswith('loopy'):
            match = re.match(r'loopy (\d+) times \{(.*)\}', line, re.DOTALL)
            if match:
                times, body = match.groups()
                for _ in range(int(times)):
                    interpret(body.strip())
        elif line.startswith('#'):
            continue
        else:
            raise ValueError(f"Unrecognized command: {line}")

# Example usage
quirk_code = """
giggle("Welcome to QuirkLang!")
# Declare variables
bloop count = 10
bloop step = 2
# Arithmetic operations
bloop total = count twiddle step
giggle("Total is: " + str(total))
# Conditional
if (total flop 2 > 5) then {
    giggle("Total is greater than 5")
} else {
    giggle("Total is not greater than 5")
}
# Loop
loopy 5 times {
    giggle("This is loop iteration")
}
"""

interpret(quirk_code)
