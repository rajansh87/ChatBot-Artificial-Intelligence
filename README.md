# ChatBot-Artificial-Intelligence
A fully working ChatBot made in Python3 as my Artificial Intelligence Lab Project.
### Project Features 

- A Simple Reflex Agent Artificial Intelligence Model.
- Complete Commented Documentation.
- Based on Object Oriented Programming Concepts.
- Artificial Intelligence.
- Query Solving Ability.
- Can be converted to Table Driven Agent too.
- Created in Python 3.7.3.
- GUI (ChatBot 2.0.py)



### Simple Reflex

###### Simple reflex agents ignore the rest of the percept history and act only on the basis of the current percept. Percept history is the history of all that an agent has perceived till date. 
###### The agent function is based on the condition-action rule. A condition-action rule is a rule that maps a state i.e, condition to an action. If the condition is true, then the action is taken, else not.
###### This agent function only succeeds when the environment is fully observable. 
###### For simple reflex agents operating in partially observable environments, infinite loops are often unavoidable. 
###### It may be possible to escape from infinite loops if the agent can randomize its actions. Problems with Simple reflex agents are :

![](https://www.geeksforgeeks.org/wp-content/uploads/ai3-1.png)
- Very limited intelligence.
- No knowledge of non-perceptual parts of state.
- Usually too big to generate and store.
- If there occurs any change in the environment, then the collection of rules need to be updated.
                
### Requirements 

- Python 3.
- utils

### Python Idle Code


#### Install 
`pip install utils`
 
 
 ### Imports
``` 
from utils import *
import random, copy
from datetime import datetime
```
Indented 8 spaces
#### Object Class
    def __repr__(self):
		return '<%s>' % getattr(self, '__name__', self.__class__.__name__)

	def is_alive(self):
		return hasattr(self, 'alive') and self.alive

#### Reflex Agent
def __init__(self):

        Agent.__init__(self)
        	def program(query):
            	if query == 'hello':
                	return('hi')
					
				elif query == 'did you know hindi':
					return('No,I cant understand')
					
				elif query == 'can you speak':
					return ('No')
					
				elif query == 'where are you from':
					return ('I belong to AI')
					
				elif query == 'where are you':
					return ('Im on top ')
					
				elif query =='time':
					now = datetime.now()
					current_time = now.strftime("%H:%M:%S")
					return("Current Time =", current_time)
					
				elif query == 'price':
					return ('Fetching')
					
				else:
					return('Oh Oh I cant understand try again')
					
			self.program = program


### Table Driven 
	def TableDrivenVacuumAgent():
		table = {((query, 'hello'),):'hi',
				 ((query, 'how are you'),):'I m fine',
				 ((query, 'how am i looking'),):'awesome',
				 ((query, 'where are you from'),):'From Your PC',
				 ((query, 'where are you'),):'In your front ',
				 ((query, 'what is time now'),):'00:00',
				 ((query, 'what is the price of product A'),):'Fetching',
				 ((query, 'can you display price of product A'),):'Fetching',
				 ((query, 'can you display description of product'),):'Fetching',
				 ((query, 'what is the description of product'),):'Fetching',
				 ((query, 'what about my product price of product'),):'Fetching',
				 }
		return TableDrivenAgent(table)
### Table Driven 
	def __init__(self,):
			self.objects = []; self.agents = []
			object_classes = [] ## List of classes that can go into environment

	def percept(self, agent):
			query=input("write your query ")
			return self.execute_action(agent,query)

### Main Function
	if __name__=="__main__":
    	e1=Environment()
    	ragent=ReflexVacuumAgent()
     	while(1):
        	e1.percept(ragent)
    
		def execute_action(self, agent, action):
			return print("ChatBot:",agent.program(action))
			#abstract



### End
