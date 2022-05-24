The filter for Pandoc as a current task in the course.
___
### How it works:
1. Finds the same headings in the document and gives the user a warning about it.
2. Replaces all headings at level 3 and below with uppercase headings.
3. Finds the word "bold" in the text and makes it bold
___
### How to use:
```
pandoc -s input.md --filter filter.py -o output.md
```
There are some examples in the repository