The main program is the python file “HW6.py”. These instructions are only for that. All the other python files are references and not to be ran individually.
When the user starts the program they will be presented with 3 choices and 1 exit command.
The choices are:
1: The user is asked for the size of the sequence to be sorted. They must enter a number > 0.
	After entering the size of the sequence, the user will enter a loop that asks them to enter the key. Key values must be an integer. Once finished entering values, the user is shown the sequence they just entered. Then it will print out the user sequence in sorted order based on the numeric value of the keys.
2: The user will enter an unsorted list of keys to be sorted via in-place heap-sort. The user will continuously be asked to enter keys until the user indicates they are finished entering values. Again, keys must be an integer.
After the user enters each value they will be asked if they are finished. If the user is finished, they should enter either “Y” or “y”. Should anything else be entered, the loop will continue.
After the loop has finished gathering all the values for the heap, it will print out the user’s heap. Then it will sort and print out the sorted heap in ascending order based on key value.
3: This will take the user to the submenu that handles creating and altering a min heap. The new menu has several options.
1: Creates a new min heap. Will continue to ask user to enter key values to be added to this new heap. After each value is entered it will ask the user if they are finished. If the User answers “y” or “Y” the loop will end and the heap will be created.
2: Similar to 1, however it only adds a single new key to the heap.
3: Returns how many items the current heap contains.
4: Will return the smallest key in the current heap without removing it
5: Deletes the smallest key in the current heap
6: Prints out all the contents, in order, of the current heap
If the user selects 0, they will be sent back to the main menu.
0: This will exit the program.
