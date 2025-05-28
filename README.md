# Serial-bond-Yield-rate-Calculator
My first "real" repository. A simple python program that calculates the yield rate of a serial bond using binary search. I'll, of course, still need to implement a GUI for the program so it's a bit more, stylistically, elegant. 

Issues:
- User inputs may be "destructive", no guards to check if a number is actually being typed or something else. While, arguably, important, for now i'll stimply ignore it as I still have bigger issues to handle.
- Takes too many iterations to converge. I'll need to test the program more if it's either because I'm using bisection (binary search) to find the yield rate, or it could be that my initial "guesses" in the range_setter function are either too wildly large or small depending on how big the initial nominal rate is. An initial educated heuristic guess based on user input may be needed.


