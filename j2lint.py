#!/bin/python
'''
Author: Nick Russo <njrusmc@gmail.com>
Last modified: 4 January 2018
Trivial jinja2 linter. It catches only a subset of errors, mostly those
involving mismatched parenthesis, brackets, brackets, or quotes. It's
more of a syntax validator than a full-blown linter.
Document styling is not, and cannot be, checked in jinja2 since the
language is designed for literal text templating. However, two common
styling things are checked by NOT enforced. If they are found in the
template, a notification prints to stdout but the linter succeeds. This
can serve as a cleanliness warning to the developer.
  * Line contains more than 80 characters
  * Line contains trailing whitespace (leading whitespace is OK)
Return codes:
  * 0: success (warning potentially displayed, but no errors)
  * 1: improper command line arguments (usage guidelines displayed)
  * 2: parsing or syntax check failed (error message displayed)
'''

from __future__ import print_function
import sys
import jinja2

def main():
    '''
    Execution starts here
    '''

    # args must contain at least two elements; the command and at least one
    # filename. If condition fails, print usage guidelines and exit, rc=1
    if len(sys.argv) < 2:
        print("usage: python j2lint.py <filename1> <filename2> ... <filenameN>")
        print("Version 0.04 (4jan2018)")
        sys.exit(1)

    # Lint each file
    rc = 0
    for filename in sys.argv[1:]:
        # Bitwise OR the existing rc with the current rc
        #   * if everything keeps succeeding   -> 0 OR 0 is always 0
        #   * if there is at least one failure -> 0 OR 2 is always 2
        print("perform linting on:  {0}".format(filename))
        cur_rc = perform_linting(filename)
        rc = rc | cur_rc
        print("linting complete on: {0}, rc={1}\n".format(filename, cur_rc))

    # Exit with proper aggregate return code
    print("*** final rc={0} ***".format(rc))
    sys.exit(rc)

def perform_linting(filename):
    '''
    Performs the linting action on a given file. It will return
    code 0 or code 2 as described in the initial docstring.
    '''

    # Define constants
    LINE_LENGTH_LIMIT = 80

    # Open the file and read the second argument (the filename)
    j2env = jinja2.Environment()
    rc = 0
    with open(filename) as template:
        try:
            # Try to read the contents of the file as jinja2
            block = template.read()
            j2env.parse(block)
        except jinja2.TemplateSyntaxError as ex:
            # Parsing failed; print the error message and set failed flag
            print("line {0: <4}: template syntax {1}\n".format(
                ex.lineno, ex.message))
            rc = 2

    # Define list of 2-tuples containing Jinja2 encloser sequences
    enclosers = [
        ('\'', '\''),
        ('\"', '\"'),
        ('(', ')'),
        ('[', ']'),
        ('{', '}'),
        ('{%', '%}'),
        ('{#', '#}')
    ]

    # Run additional testing by splitting the text into lines
    # and iteratively checking for matching encloser sequences
    lines = block.split('\n')
    for i, line in enumerate(lines):
        for start, end in enclosers:
            # Special case: If the word "secret" appears in a line, given that
            # this is normally used to store secret data such as passwords,
            # mismatched special characters can be used. Do not enforce.
            if "secret" in line:
                continue

            # Count the number of start vs end encloser sequences; must match
            # Also ensures the start encloser comes before the end encloser
            # Note that the two could be equal (as -1) which is not an error
            elif (line.count(start) != line.count(end) or
                  line.find(start) > line.find(end)):
                print("line {0: <4}: mismatched {1: <3}{2: <3} '{3}'".format(
                    i + 1, start, end, line))
                rc = 2

        # Test for lines exceeding the length limit
        if len(line) > LINE_LENGTH_LIMIT:
            print("line {0: <4}: (warn) line > {1} chars, saw {2}".format(
                i + 1, LINE_LENGTH_LIMIT, len(line)))

        # Test for trailing whitespace
        if line != line.rstrip():
            print("line {0: <4}: (warn) trailing whitespace".format(i + 1))

    # Return the rc back to the caller
    return rc

if __name__ == "__main__":
    main()