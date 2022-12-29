# Introduction to Python

ASDF

## Table of contents

Chapter 1: [Python Basics]()

## Chapter 1: Python Basics

### Expressions & Operations

The Python programming language has a wide range of syntactical constructions, standard library functions, and interactive.


Table 1-1: Math Operators from the Highest to Lowest Precedence

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

Table 1-2: Common Data Types

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

When `+` is used on two string values, it joins the strings as the *string concatenation* operator.\
Example

```python
'This' + 'is' + 'text' = 'Thisistext'
```

When `*` operator is used on one string value and one integer value, it becomes the *string replication* operator.\
Example

```python
'Alice' * 5 = 'AliceAliceAliceAliceAlice'
```

### Storing Values in Variables

A *variable* is like a box in the computer's memory where you can store a single value.\
You'll store values in variables with an *assignment statement*.
An assignment statement consists of a variable name, an equal sign (called the assignment operator), and the value to be stored.

A variable is initialized (or created) the first time a value is stored in it.
After that, you can use it in expressions with other variables and values.
When a variable is assigned a new value, the old value is forgotten.
This is called *overwriting* the variable.

### Variable Names

1. It can be only one word
2. It can use only letter, numbers, and an underscore (_)

Table 1-3: Valid and Invalid Variable Names

|   Valid variable names | Invalid variable names                                |
| ---------------------- | ------------------------                              |
|                balance | current-balance (hyphens are not allowed)             |
|         currentBalance | current balance (spaces are not allowed)              |
|        current_balance | 4account (can't begin with a number)                  |
|                  _spam | 42 (can't begin with a number)                        |
|                   SPAM | total_$um (special characters like $ are not allowed) |
|               account4 | 'hello' (special characters like ' are not allowed)   |

Variable names are case-sensitive, meaning that `spam`, `SPAM`, `Spam`, and `sPaM` are four different variables.
There is the camelcase for variable names (lookingLikeThis) vs the underscores (looking_like_this).


