def convert_cpp_to_python(cpp_code):
    # Replace basic syntax
    cpp_code = cpp_code.replace(";", "")  # Remove semicolons
    cpp_code = cpp_code.replace("cout <<", "print(").replace("<<", ",").replace("endl", ")")
    
    # Replace data types
    cpp_code = cpp_code.replace("int", "")
    cpp_code = cpp_code.replace("float", "")
    cpp_code = cpp_code.replace("double", "")
    cpp_code = cpp_code.replace("char", "")
    cpp_code = cpp_code.replace("string", "")
    
    # Replace loops and conditionals
    cpp_code = cpp_code.replace("for (", "for ")
    cpp_code = cpp_code.replace("while (", "while ")
    cpp_code = cpp_code.replace("if (", "if ")
    cpp_code = cpp_code.replace("else if (", "elif ")
    cpp_code = cpp_code.replace("else", "else:")
    
    # Replace function definitions
    cpp_code = cpp_code.replace("void", "def")
    cpp_code = cpp_code.replace("main()", "main():")
    
    return cpp_code

def read_cpp_file(file_path):
    try:
        with open(file_path, 'r') as cpp_file:
            cpp_code = cpp_file.read()
        return cpp_code
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def write_python_file(file_path, python_code):
    with open(file_path, 'w') as python_file:
        python_file.write(python_code)

def convert_cpp_file_to_python(cpp_file_path, python_file_path):
    # Read the C++ file
    cpp_code = read_cpp_file(cpp_file_path)
    
    if cpp_code:
        # Convert the C++ code to Python code
        python_code = convert_cpp_to_python(cpp_code)
        
        # Write the converted Python code to the output file
        write_python_file(python_file_path, python_code)
        print(f"Conversion completed. Python code saved to {python_file_path}")

# Example usage:
cpp_file_path = 'main.cpp'  # Input C++ file
python_file_path = 'converted_code.py'  # Output Python file

convert_cpp_file_to_python(cpp_file_path, python_file_path)
