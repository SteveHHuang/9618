# Processor Fundemantals

## Von neumon model:

-a central processor

-fast access time of memory

-which stores current running programs

-instructions are executed in sequence 



## Stored program concept:

-data and instructions are stored in the same memory location



## IAS Immediate access store

-holds all the data that is currently being used


-volatile 


-fast access time



## Register

### Differences between special purpose registers and general purpose registers:

-special purporse register stores the status of the program, whereas the general purpose register stores the temporary data of the program



-special purpose register is spacialized for spacific tasks, general purpose register can be used for any purposes



-special purpose register stores can be used by certain instructions, while general purpose register can be used by any instructions

### PC

Stores the next address of the insturction to be fetched



### MAR

stores the memory location that is currently being read from or written to



### MDR

stores the data that is just read from the memory



### IX

stores a value, adding to a given address to give a new address



### CIR

stores the current instruction that is being encoded and executed



### SR

stores the flags set by events

contains bits that can be set or cleared, depends on the instructions



## Addressing mode

### Immediate addressing:

-When the operand is the data



### Direct addressing:

-When the operand holds the memory address of the data



### Indirect addressing:

-When the operand holds a memory address that stores the memory address of the data 



### Index addressing:

-The content of IX adds to the operand, access data to the calculated address



### Relative addressing:

-Allow re-locatable code

-as the target address can be specified by the base address+offset



## FE cycle:



Program counter(PC) holds the address of the next instruction to be executed



The address is sent to the memory address register(MAR) and PC is incremented



then it is sent to memory to fetch the data at that address



the data is transferred to memory data register(MDR)



and then sent to current instruction register to be encoded and executed



## Interrupt:



### features:

-signal that is sent by devices or programs

-seek the attention of the processor



### reasons:

-Caused by: 

  -Timing signal 

  -Input or output processes 

  -Hardware fault (Eg. Paper jam) 

  -User interaction 

 -Software interrupt: 

   -Division by zero 

   -Runtime error 

   -Out of memory bounds

   -Program requesting an external device / input

   -Buffer overflow

   -Stack overflow 

   -Attempt to access invalid memory location 

   -Array index out of bounds 



### How a computer handle an interrupt?



-An interrupt flag is raise in the interrupt register



-After each FE cycle, the processor check the interrupt register whether or not there is interrupt



-if detects interrupt, check the priority



-If has lower priority, continue FE cycle



-if has greater priority than the current process, then store the current process in the stack, otherwise continue FE cycle



-an appropriate interrupt service routine(ISR) is called to handle the interrput



-After the interrupt is completed, check the further interrupts



-if lower priority, load the process from the stack and continue to run



