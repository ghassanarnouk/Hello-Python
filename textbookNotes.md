# Introduction to Python

ASDF

## Table of contents

Chapter 1: [Python Basics]()

## Chapter 1: Python Basics

### Expressions & Operations

The Python programming language has a wide range of syntactical constructions, standard library functions, and interactive.


Table 1-1 Math Operators from the Highest to Lowest Precedence

|   Operator | Operation                         |   Example | Evaluates to ...
| ---------- | -----------                       | --------- | -----------------
|         ** | Exponent                          |    2 ** 3 | 8
|          % | Modulus/Remainder                 |    22 % 8 | 6
|         // | Integer division/floored quotient |   22 // 8 | 2
|          / | Division                          |    22 / 8 | 2.75
|          * | Multiplication                    |     3 * 5 | 15
|          - | Subtraction                       |     5 - 2 | 3
|          + | Addition                          |     2 + 2 | 4

**Note:** (8 * 2) + 6 = 22

It is always possible to write the precedence of operations using ().

### Data Types

A *data type* is a category for values, and every value belongs to exactly one data type.
The most common data types in Python are listed in Table 1-2 below.

Table 1-2 Common Data Types

|      Data Type | Examples                 |
|    ----------- | ----------               |
|       Integers | -16, -1, 0, 1, 5         |
| Floating-point | -1.25, -0.05, 0.0, 3.0   |
|        Strings | 'a', 'Hello!', '11 cats' |

Python programs can also have text values called *strings*, *strs* (pronounced "stirs").
Always surround your string in single quote (') character so that Python knows where the string begins and ends.\
It is also possible to have a string with no characters in it ''.
It is called *blank string*.\
A common error message for forgetting the final single quote character at the end of the string is: `SyntaxError: EOL while scanning string literal`

### String Concatenation and Replication

