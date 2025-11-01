## Processors
### CISC & RISC
### Describe what is meant by RISC and CISC processors. 
>s22 31 Q4a
#### RISC
	- Uses simple instructions 
	- Uses fixed length instructions 
	- Instructions only require one clock cycle 
	- Uses many registers 
	- Makes use of pipelining 
	- Hardwired CU

#### CISC
	- Uses many instruction formats 
	- Uses variable length instructions 
	- Makes use of different addressing modes 
	- Uses few registers 
	- Has a large instruction set 
	- Requires complex circuits 
	- Frequently uses cache 
	- Instructions (converted to sub-instructions that) may require many clock cycles 
	- Programmable CU


### Identify two differences between RISC and CISC processors. 
>s22 31 Q4b

	- RISC has fewer instructions, while CISC has more instructions 
	- RISC has many registers, whereas CISC has few registers 
	- RISC’s instructions are simpler, whilst CISC’s instructions are more complex 
	- RISC has a few instruction formats, while CISC has many instruction formats
	- RISC usually uses single-cycle instructions, whereas CISC uses multi-cycle instructions
	- RISC uses fixed-length instructions, whilst CISC uses variable-length instructions
	- RISC has better pipelineability, while CISC has poorer pipelineability
	- RISC requires less complex circuits, whereas CISC requires more complex circuits
	- RISC has fewer addressing modes, whilst CISC has more addressing modes
	- RISC makes more use of RAM, while CISC makes more use of cache/less use of RAM
	- RISC has a hard-wired control unit, while CISC has a programmable control unit 
	- RISC only uses load and store instructions to address memory, whereas CISC has many types of instructions to address memory





### Pipelining
For risc only, cisc is hard to implement as the time taken for instructions may be different

A form of parallelism applied to instruction execute

Problems:
可能无法正确加载数据

### Interrupt handling

>CISC更容易实现

### Basic Computer Architectures - Flynn’s Taxonomy 弗林分类法
**四种并行处理类别**

s22 31 Q4a
#### SISD single instruction single data
	Uses one processor execute single instruction using one data set(1)
	

>单核 CPU

#### SIMD single instruction multiple data
	Uses many processors execute the same instruction using different data sets (1)
	

>GPU图像处理

#### MISD multiple instruction single data
	Many processors (using different instructions) use the same data set (1)

>飞控

#### MIMD multiple instruction multiple data
	Many processors (using different instructions) using different data sets (1)

>多核 CPU / 多路 CPU
>会涉及操作系统的management

## Virtual Machine

### The virtual machine software undertakes many tasks. Describe two of these tasks. 
>9608 s16 33 Q3

	- Create / delete virtual machine 
	- Hardware emulation 
	- Ensures each virtual machine is protected from actions of another virtual machine

### Explain the difference between a guest operating system and a host operating system. 
>9608 s16 33 Q3

	Guest OS is running under the Host OS software

#### Guest operating system:
	- An operating system running in a virtual machine 
	- Controls virtual hardware 
	- OS is being emulated 

#### Host operating system:
	- The operating system that is actually controlling the physical hardware 
	- The operating system for the physical machine
	- The OS running the VM software 

### Explain one limitation of VM 

>9608 s16 33 Q3(modified)

	- Using virtual machine means emulation of some hardware …
	- Particular hardware may be difficult to emulate
	- Non-VM installation may not perform in the same way
	- Execution speed slower than non-VM system
	- Problems in judging actual response times at time of maximum traffic needs fastest possible speed
	