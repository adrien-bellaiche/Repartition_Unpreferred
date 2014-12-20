Repartition_Unpreferred
=======================

This is an implementation of the Ford-Fulkerson algorithm, to csv files.

The context of this project is fairly simple : I wanted to organize a party in which each guest would offer a 
present to another guest. The problem was that most of the guest didn't know each other well enough to find a specific 
present. So I sent to all of them a csv file containing the guest list, with the simple instruction to rename it to their 
own name (the one in the file), to remove all of the guest they don't know well enough, and to send me the result back.

How to use this implementation :
- Create a csv folder containing all the csv files
    -> CSV file requirement : filename for guest FULL NAME is "FULL NAME.csv", and contains a vertical list of "OTHERS_FIRST_NAME, OTHERS_FAMILY_NAME"
- Run main.py

Output :
- correspondance.txt : contains the guest "sender" number (their "receiver" number is (sender number + amount of guests))
- ex.graph : displays the connections. Uses only numbers.
- out.txt : the most important one, containing who is matched to who.

A later release will contain possibilities for matching two different lists (for example, a repartition of students on
projects given their possibilities to be in said project)

Special thanks to Roderic Moitié who wrote most of the ford_fulkerson.py & Tools.py.

Fell free to send a message on any bug you may have encountered