from lexer import Lexer
from parser import Parser
from code_generator import CodeGenerator

def compile_expression(x, y, z, generator):
    # Fixed expression: result = x + y * z
    expression = f"result = {x} + {y} * {z}"
    
    try:
        lexer = Lexer(expression)
        parser = Parser(lexer)
        ast = parser.parse()
        result_reg = generator.generate(ast)
        
        instructions = generator.get_instructions()
        return instructions
    except Exception as e:
        print(f"Error during compilation: {str(e)}")
        return []

def main():
    print("\nFixed Expression Compiler: result = x + y * z")
    print("=" * 50)
    
    try:
        # Get input values
        x = int(input("Enter value for x: "))
        y = int(input("Enter value for y: "))
        z = int(input("Enter value for z: "))
        
        generator = CodeGenerator()
        
        print("\nCompiling: result = x + y * z")
        print("-" * 40)
        
        instructions = compile_expression(x, y, z, generator)
        
        if instructions:
            print("\nGenerated Instructions:")
            print("-" * 40)
            for instruction in instructions:
                print(instruction)
            
            # Show final result
            if 'result' in generator.var_values:
                print(f"\nFinal Result: {generator.var_values['result']}")
                
    except ValueError:
        print("Error: Please enter valid integer values")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()