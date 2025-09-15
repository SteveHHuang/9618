## Explain how a new element can be added to the queue if it is implemented using two stacks.[4] s23 33 Q11c
	- (Two stacks are required) so that the second stack can reverse the order of the first stack. 
	- Stack 1 operates as the queue with the newest elements at the bottom. Whilst stack 2 is empty. 
	- To add an element, pop all the elements from stack 1 and push onto stack 2. 
	- Push the new element onto either stack. 
	- Pop all the elements of stack 2 back onto stack 1.

## Describe what is meant by recursion.  [2] s23 33 Q12a
	- A process using a function or procedure defined in terms of itself / calls itself. 
	- A recursive process must have a base case 
	- There must also be a general case where the recursive call takes place.


## Explain the reasons why a stack is a suitable Abstract Data Type (ADT) to implement recursion. [3] w21 31 Q10b
	- A stack is a LIFO data structure 
	- Each recursive call is pushed onto the stack 
	- ...and is then popped as the function ends 
	- Enables unwinding 
	- ... to maintain the required order.

## Explain why the properties are private.[2] w18 41 Q5a
	- To restrict direct access to the property to the class 
	- To make the program easier to debug 
	- To ensure data going in is valid// To prevent accidental changes