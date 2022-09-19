# Blackwater Annual Concert
Write a program that helps organize the Blackwater Annual Concert.
The main menu allows the user add performers to the concert and eventually it is used to generate a schedule for the concert based on all the information entered and stored in a file performers.txt
 
Write a program that offers two choices to the user:
1. Add performers to the concert
2. Generate concert details
 
Here are the details on how each of these options should be implemented:
 
1. Adding performers
The program allows the user to add a list of performers. For each performer entered they must give:
• their first name and last name
• the type of performance
• the duration in minutes for their performance.
  
All the performers information is stored in a file called performers.txt. After performers are added a summary of the performers just added is given:
 
• the number of musicians, singers, and dancers
• the longest act
• the total time required for all performances
 
 
 
 
 
A sample run:
 
Blackwater Annual Music Concert
-------------------------------
1. Adding Performers
2. Generate Concert Details
3. Quit
==> 1
 
(1) Adding Performers ---------------------
How many performers are you adding: 3
 
Performer 1/3:
Enter your name: Fred
Enter your surname: Walsh
Type of Performance
1. Musical
2. Singer
3. Dancer
==>: 1
Time slot required (mins): 15
 
Performer 2/3:
Enter your name: Harry
Enter your surname: Ford
Type of Performance
1. Musical
2. Singer
3. Dancer
==>: 3
Time slot required (mins): 25
 
Booking 3/3:
Enter your name: Sam
Enter your surname: Murphy
Type of Performance
1. Musician
2. Singer
3. Dancer
==>: 1
Time slot required (mins)? twenty
 
The following information has been added.
1. Walsh, Fred Musician 15 minutes
2. Ford, Harry Dancer 25 minutes
3. Murphy, Sam Musician 20 minutes
 
Summary Notes:
-------------
2 Musicians
0 Singers
1 Dancer
Total time required: 1 hour (s) 0 min (s).
The longest act added is Harry Ford (Dancer) 25 minutes.
 
Blackwater Annual Music Concert
-------------------------------
1. Adding performers
2. Generate Concert Details
3. Quit
==> 1
 
(1) Adding Performers ---------------------
How many performers are you adding: 1
 
Booking 1/1:
Enter your name: Mary
Enter your surname: Murphy
Type of Performance
1. Musical
2. Singer
3. Dance
==>: 3
Time slot required (mins): 19
 
The following information has been added.
 
1. Murphy, Mary Dancer 19 minutes
 
Summary Notes:
-------------
0 Musicians
0 Singers
1 Dancer
Total time required: 0 hours, 19 mins
The longest act added is Mary Murphy (Dancer) 19 minutes.
 
 
Blackwater Annual Music Concert
-------------------------------
1. Adding performers
2. Generate Concert Details
3. Quit
==> 3
 
And performers.txt becomes
Walsh Fred Musician 15
Ford Harry Dancer 25 Murphy Sam Musician 20
Murphy Mary Dancer 19
2. Generate Concert Details
 
The program will read performers.txt and display the details of the concert on the screen.
 
An asterisk should be placed after each performer’s name whose act is longer than 15 minutes.
 
Sample Run
 
Blackwater Annual Music Concert
--------------------------------
1. Adding performers
2. Generate Concert Schedule 3. Quit ==> 2.
 
 
1: Fred Walsh (Musician) 15 minutes
2: Harry Ford * (Dancer) 25 minutes
3: Sam Murphy * (Musician) 20 minutes
4: Mary Murphy * (Dancer) 19 minutes
 
 
Blackwater Annual Music Concert
--------------------------------
1. Adding performers
2. Generate Concert Schedule
3. Quit ==> 3