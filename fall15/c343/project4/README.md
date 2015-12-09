Kyle Nealy
C343
Project 4
10/16/15

Program seq_align.py uses a function named seq_align to algorithmically determine the most optimal alignments of two given strings.  The function seq_align takes 3 parameters; two sequences, or strings, to be aligned, and enable_graphics, which is a boolean set to default to True. The function sets up a Dot board mapping the two given sequences and their possible alignments and records each board location in a dictionary with the location coordinate pair as the keys, and the max possible score for the board location as its value. The function then uses the resulting dictionary containing the coordinate pair and value of all positions on the board in combination with a separate dictionary containing the coordinate pair and direction of the previous position for all the locations on the board.    

###########################
UPDATE 12:42AM 10/20/15

Just saw that my assignment said 0 and a feedback said that the code wouldn't execute. After looking through the code and doing a hand trace I noticed a small typo at line 140 where the variable used should have been an i instead of j. 
I have now fixed the typo and reuploaded. Everything should be working.

