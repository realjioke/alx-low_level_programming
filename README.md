# ALX Low-Level Programming

## Overview

This repository contains a series of projects developed as part of the ALX Software Engineering program, focusing on low-level programming using the C language. These projects cover fundamental concepts and advanced topics, providing a solid foundation in system programming and algorithm development.

## Table of Contents

- [Projects](#projects)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Projects

1. **0x00-hello_world**: Introduction to C programming; setting up the environment, understanding the compilation process, and writing simple programs.
2. **0x01-variables_if_else_while**: Exploring variables, conditional statements, and loops in C.
3. **0x02-functions_nested_loops**: Delving into function definitions, prototypes, and nested loops.
4. **0x03-debugging**: Techniques and strategies for debugging C programs.
5. **0x04-more_functions_nested_loops**: Advanced use of functions and nested loops.
6. **0x05-pointers_arrays_strings**: Understanding pointers, arrays, and string manipulations.
7. **0x06-pointers_arrays_strings**: Continued exploration of pointers and arrays.
8. **0x07-pointers_arrays_strings**: Further studies on pointers, arrays, and strings.
9. **0x08-recursion**: Implementing recursive functions and understanding their applications.
10. **0x09-static_libraries**: Creating and using static libraries in C.
11. **0x0A-argc_argv**: Handling command-line arguments in C programs.
12. **0x0B-malloc_free**: Dynamic memory allocation and deallocation using `malloc` and `free`.
13. **0x0C-more_malloc_free**: Advanced dynamic memory management techniques.
14. **0x0D-preprocessor**: Understanding the C preprocessor and macros.
15. **0x0E-structures_typedef**: Defining and using structures and `typedef` in C.
16. **0x0F-function_pointers**: Exploring pointers to functions and their uses.
17. **0x10-variadic_functions**: Implementing functions with variable numbers of arguments.
18. **0x12-singly_linked_lists**: Creating and manipulating singly linked lists.
19. **0x13-more_singly_linked_lists**: Advanced operations on singly linked lists.
20. **0x14-bit_manipulation**: Performing bitwise operations and understanding bit manipulation.
21. **0x15-file_io**: File input/output operations in C.
22. **0x17-doubly_linked_lists**: Implementing and managing doubly linked lists.
23. **0x18-dynamic_libraries**: Creating and using dynamic libraries in C.

Each project directory includes:

- **README.md**: Detailed descriptions of the project's objectives, concepts covered, and specific instructions.
- **Source Code**: C files implementing the project's tasks.
- **Header Files**: Header files (`.h`) containing function prototypes and macros.
- **Test Files**: Scripts or programs to test the implemented functions.

## Installation

To set up the projects locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/realjioke/alx-low_level_programming.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd alx-low_level_programming
   ```
3. **Compile the code**:
   - Each project may have multiple C files. To compile a specific file:
     ```bash
     gcc -Wall -Werror -Wextra -pedantic <filename>.c -o <output_name>
     ```
   - For projects with multiple files, a `Makefile` may be provided. Use:
     ```bash
     make
     ```

## Usage

To run a specific program:

1. **Compile the program** (if not already compiled):
   ```bash
   gcc -Wall -Werror -Wextra -pedantic <filename>.c -o <output_name>
   ```
2. **Execute the compiled program**:
   ```bash
   ./<output_name>
   ```

For example, to compile and run `main.c`:

```bash
gcc -Wall -Werror -Wextra -pedantic main.c -o main
./main
```

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Description of changes"
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature-branch
   ```
5. **Open a Pull Request** detailing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.
