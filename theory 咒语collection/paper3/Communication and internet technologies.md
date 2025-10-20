## Definition of protocol:
	A set of rules governing communication across a network: the rules are agreed by both sender and recipient.

## Explain why a protocol is used in communication between computers.[2] w22 32 Q3
	- Protocols set a standard for communication 
	- Protocols enable communication between devices from different manufacturers/platforms 
	- If two devices were sending messages to each other but using different protocols, they would not be able to communicate properly

## TCP/IP


## HTTP


## FTP


## Email protocols: POP3, IMAP & SMTP
***前两个用于接收邮件。***

***SMTP(Simple Mail Transfer Protocol)用于发送邮件。***

***POP3（Post Office Protocol 3）不会储存在服务器中，而IMAP（Internet Message Access Protocol）会。***

### Describe the purpose of the IMAP protocol.[2] w22 32 Q3
	• used by email clients to retrieve email messages
	• from a mail server (over a TCP/IP connection) 
	• keeps the server and client in sync (by not deleting the original email). 

 

## BitTorrent
### State the use of BitTorrent[1]
	File sharing.

### Tracker
	Stores details of other computer.

### Swarm 
	Connected peers (clients) that share a tracker. 

### Seed 
	Peer computer that has 100% of file.

### Leech
	A peer with negative feedback from swarm members. 

### Lurker
	User/client that downloads files but does not supply any new content to the community.


### Pros and Cons


## Circuit switching & Packet switching


### Describe both methods of data transmission. Include a different advantage and disadvantage for each method. [8] s22 31 Q3
#### Circuit switching
	- a dedicated circuit 
	- circuit is established before transmission starts and is released after transmission ends 
	- data is transferred using the whole bandwidth 
	- all data is transferred over the same route

##### Pros:
	– Data arrive in order and do not need to be reassembled

##### Cons:
	- Nobody else can use the same circuit even if it is idle 
	- Less secure as only one route used


#### Packet switching
	- data is split into packets 
	- each packet is given its own route 
	- the routing for a packet depends on the congestion 
	- packets may not arrive in the order sent

##### Pros:
	- Packets can be rerouted if there are problems
	- More secure as harder to intercept messages

##### Cons:
	- Time needed to reassemble packets at the destination
