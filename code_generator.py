class CodeGenerator:
    def __init__(self):
        self.instructions = []
        self.register_count = 0
        self.variables = {}  # Store variable locations
        self.var_values = {}  # Store variable values
        
        # Initialize variables with some values
        self.var_values['y'] = 5
        self.var_values['z'] = 3
        self.var_values['a'] = 2
        
        # Create registers for initial variables
        self.variables['y'] = self.new_register()
        self.variables['z'] = self.new_register()
        self.variables['a'] = self.new_register()
        
        # Load initial values
        self.add_instruction(f'LOAD {self.variables["y"]}, {self.var_values["y"]}', f'Initialize y with {self.var_values["y"]}')
        self.add_instruction(f'LOAD {self.variables["z"]}, {self.var_values["z"]}', f'Initialize z with {self.var_values["z"]}')
        self.add_instruction(f'LOAD {self.variables["a"]}, {self.var_values["a"]}', f'Initialize a with {self.var_values["a"]}')

    def new_register(self):
        reg = f'R{self.register_count}'
        self.register_count += 1
        return reg

    def add_instruction(self, instruction, comment):
        formatted_instruction = f"{instruction:<30} ; {comment}"
        self.instructions.append(formatted_instruction)

    def generate(self, node):
        if node['type'] == 'INTEGER':
            reg = self.new_register()
            self.add_instruction(f'LOAD {reg}, {node["value"]}', f'Load constant {node["value"]}')
            return reg, node["value"]

        elif node['type'] == 'VARIABLE':
            reg = self.new_register()
            var_name = node['name']
            if var_name not in self.variables:
                raise Exception(f'Undefined variable: {var_name}')
            var_reg = self.variables[var_name]
            self.add_instruction(f'MOV {reg}, {var_reg}', f'Load variable {var_name}')
            return reg, self.var_values.get(var_name, "undefined")

        elif node['type'] == 'ASSIGNMENT':
            value_reg, value = self.generate(node['value'])
            var_name = node['name']
            if var_name not in self.variables:
                self.variables[var_name] = self.new_register()
            target_reg = self.variables[var_name]
            self.add_instruction(f'MOV {target_reg}, {value_reg}', f'Store into variable {var_name}')
            self.var_values[var_name] = value
            return target_reg, value

        elif node['type'] == 'BINARY_OP':
            left_reg, left_val = self.generate(node['left'])
            right_reg, right_val = self.generate(node['right'])
            result_reg = self.new_register()

            if node['op'] == '+':
                result = left_val + right_val
                self.add_instruction(f'ADD {result_reg}, {left_reg}, {right_reg}', 
                                   f'Add {left_reg} and {right_reg}')
            elif node['op'] == '-':
                result = left_val - right_val
                self.add_instruction(f'SUB {result_reg}, {left_reg}, {right_reg}', 
                                   f'Subtract {right_reg} from {left_reg}')
            elif node['op'] == '*':
                result = left_val * right_val
                self.add_instruction(f'MUL {result_reg}, {left_reg}, {right_reg}', 
                                   f'Multiply {left_reg} by {right_reg}')
            elif node['op'] == '/':
                result = left_val / right_val
                self.add_instruction(f'DIV {result_reg}, {left_reg}, {right_reg}', 
                                   f'Divide {left_reg} by {right_reg}')

            return result_reg, result

    def get_instructions(self):
        return self.instructions

    def evaluate_expression(self):
        # Create AST for x = y + z * a
        ast = {
            'type': 'ASSIGNMENT',
            'name': 'x',
            'value': {
                'type': 'BINARY_OP',
                'op': '+',
                'left': {
                    'type': 'VARIABLE',
                    'name': 'y'
                },
                'right': {
                    'type': 'BINARY_OP',
                    'op': '*',
                    'left': {
                        'type': 'VARIABLE',
                        'name': 'z'
                    },
                    'right': {
                        'type': 'VARIABLE',
                        'name': 'a'
                    }
                }
            }
        }
        
        return self.generate(ast)