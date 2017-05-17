This is a simple procedure for setting up anonymous peer grading for classroom projects. 
The idea is to make a coverpage for tests (written in LaTeX) with clear and codes for students. The instructor will have a list of all authors and referees.

Overall Procedure
=================

    1. Obtain your class roster as a plain `txt` (or `tsv` or `csv` file), one student name per line.  This is easy to get from D2L, Blackboard, WeBWorK, etc. 
    2. Write a test or assignment, preferably in LaTeX.  Make sure the front page has appropriate blanks for *AuthorCode* (5 digits) and *RefereeCode* (4 digits), and that students are discouraged from writing their name on it.  See the example in `example-test.tex`.  Also, write a thorough grading rubric for referees to use. 
    3. *Key Step*. Run `python makecodes.py your-classlist.txt (name-of-assignment)-coversheets.tex (name-of-assignment)-codes.tsv`
    4. Do not lose the `tsv` file, or you can never track down students!
    5. Compile the coversheets with `pdflatex (name-of-assignment)-coversheets.tex`.  Or, you can use your favorite (La)TeX editor to compile it.
    6. Before class, lay out all of the tests.  Put a cover sheet over each test, with the name up.  When students come in to class, they have to find their seat by looking for their name.  (You could do this alphabetically, randomly, or some other way.)
    7. Students do the test, writing *only* their *AuthorCode* (not their name or *RefereeCode*) on the test.
    8. The students *keep* their coversheet, and hand in their test.  
    9. (Optional, but useful) The instructor bulk-scans all the tests.
    10. (Possibly Next Day) The instructor shuffles all the tests, and hands them out again.    The instructor posts the solution guide and grading rubric.
    11. Students check that they didn't get their own test by accident.  They write their *RefereeCode* on the test they receive, using the coversheet they should still have.
    12. Students make comments and grade the test they receive, based on the solution guide and grading rubric.
    13. (Next Day) Students hand in the test they graded.  Instructor reads all the referee comments, and sanity-checks the scores.  Use the `(name-of-assignment)-codes.tsv` file to write the AuthorName on the tests, and to enter the assignment into the gradebook.
    14. (Next Day) Instructor hands back tests to their original authors.

The key step, of generating randomized codes and distributing them to students, is aided by the Python script `makecodes.py` included here.

SCRIPT INPUT
------------
    1. A list of names, as a simple text file line-by-line, like in `example-classlist`

SCRIPT OUTPUT 
-------------
    1. LaTeX source file, which compiles to make one coversheet per student.  These are compiled and printed for the students.
    2. Tab-separated reference sheet of author and referee codes, for reference by the instructor.  This is kept for grade entry, and in case of problems.


General Suggestions
===================

    1. Do this once, in the first week of class, with a completely trivial assignment.  Then, students will understand the referee procedure when a real test occurs. 
    2. Make sure that your grading rubric is clear and provides several reasonable avenues of solutions.  However, the referee should feel free to say "I don't understand what this Author is doing." and defer to the instructor.
    3. Before the test, emphasize that solutions are intended to explain ideas to peers of similar background and intelligence.  Mathematical proofs are not sacred incantations to God; instead, they are a tool to help our fellow citizens understand complicated ideas.
    4. Make sure that there is some incentive to perform a good review.  If someone is deliquient in performing a review (or even worse, never hands it back in!), there will be serious consequences for their grade, etc.   It is  
    5. Bulk-scan the tests before handing them out for review, in case a student drops/disappears and never brings back the test they were assigned to referee.

