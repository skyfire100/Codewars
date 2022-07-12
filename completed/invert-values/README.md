# Invert values

 - URL:[https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad](https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad)
 - Id: 5899dc03bc95b1bf1b0000ad
 - Language: python
 - Completed on: 2020-05-13T17:59:20.031Z
 - Tags: Lists,Fundamentals
 - Description:
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

~~~if-not:racket
```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```
~~~

```if:javascript,python,ruby,php,elixir,dart
You can assume that all values are integers. Do not mutate the input array/list.
```

```if:c
### Notes:
- All values are greater than `INT_MIN`
- The input should be modified, not returned.
```
~~~if:racket
```racket
(invert '(1 2 3 4 5))   ; '(-1 -2 -3 -4 -5)
(invert '(1 -2 3 -4 5)) ; '(-1 2 -3 4 -5)
(invert '())            ; '()
```
~~~
