# Assemble string

 - URL:[https://www.codewars.com/kata/6210fb7aabf047000f3a3ad6](https://www.codewars.com/kata/6210fb7aabf047000f3a3ad6)
 - Id: 6210fb7aabf047000f3a3ad6
 - Language: python
 - Completed on: 2022-02-25T02:13:11.227Z
 - Tags: Strings,Arrays,Fundamentals
 - Description:
## Task

In this task, you need to restore a string from a list of its copies.

You will receive an array of strings. All of them are supposed to be the same as the original but, unfortunately, they were corrupted which means some of the characters were replaced with asterisks (`"*"`).

You have to restore the original string based on non-corrupted information you have. If in some cases it is not possible to determine what the original character was, use `"#"` character as a special marker for that.

If the array is empty, then return an empty string.


### Examples:

```
input = [
  "a*cde",
  "*bcde",
  "abc*e"
]
result = "abcde"


input = [
  "a*c**",
  "**cd*",
  "a*cd*"
]
result = "a#cd#"
```
