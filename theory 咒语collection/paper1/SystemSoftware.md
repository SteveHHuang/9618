# System Software



## Why need operating system?



i. Hide the complexities of the hardwares from user



ii. Provides the platform to run the software



iii. Provide user interface



## Pros of using program libraries:

-more robust, which means free of error and programmer does not need to spending time to debug

-can update when improvements are avaliable

-can be called by programs by importing program library

-reduces duplication of code



## Pros of creating a program library:



-subroutines can be reused so that it need not having to be re-tested and hence reduces programmer's time

-program liberary offers continuity between programs

-programmer can contribute their specilism to the liberary, and they can use other's specialism



## Pros of using DLL:

-main memory requirements for program are reduced as dynamic link library is loaded only once / when required 

-the executable file size is smaller because the executable does not contain all the library routines 

-maintenance not needed to be done by the programmer because the DLL is separate from program 

-no need to recompile the main program when changes are made to DLL because changes to the DLL file code are done independently of the main program

-single DLL file can be made available to several application programs which saves space in memory



## Benefits of modular approach

-reduces duplication of code as modules can be called when needed

-easier to maintain

-modules can be tested once to use, so reduces time to debug

-any subsequent changes can be made once



## State two drawbacks of using a compiler compared to an interpreter during program development.

-larger amounts of source code take time to compile 

-slower to produce the object code than an interpreter 

-code cannot be changed without recompilation 

-the program will not run if there are any errors 

-errors cannot be corrected in real-time

-cannot easily test specific sections of the source code



## Explain why high-level language programs might be partially compiled and partially interpreted.



-partially compiled programs can be used on different platforms as they are interpreted when run 

-code is optimised for the CPU as machine code is generated at run time

