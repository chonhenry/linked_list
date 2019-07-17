#Implementation of a singly linked list
class node:
	def __init__(self, value, nextnode = None):
		self.value = value
		self.nextnode = nextnode

	def getvalue(self):
		return self.value

	def getnextnode(self):
		return self.nextnode

class linkedlist:
	def __init__(self, head=None):
		self.head = head
		self.tail = head

	def append(self, newvalue): #add a node at the end of the linked list
		newnode = node(newvalue)
		if (self.head == None):
			self.head = newnode
			self.tail = newnode
		else:
			self.tail.nextnode = newnode
			self.tail = newnode

	def push(self, newvalue): #add a node at the beginning of the linked list
		newnode = node(newvalue)
		if (self.head == None):
			self.head = newnode
			self.tail = newnode
		else:
			newnode.nextnode = self.head
			self.head = newnode

	def printlist(self): #print the whole linked list
		current = self.head
		lst = []
		while(current != None):
			lst.append(current.value)
			current = current.nextnode
		print(lst)

	def insert(self, position, value): # insert a node to a given position
		newnode = node(value)
		current = self.head
		index = 0

		while(index!=position-1):
			current = current.nextnode
			index+=1
		newnode.nextnode = current.nextnode
		current.nextnode = newnode

	def remove_position(self, position): #remove node with a given position
		current = self.head
		index = 0

		if (position==0):
			del_node = self.head
			self.head = del_node.nextnode
			del del_node
		else:
			while(index!=position-1):
				current = current.nextnode
				index+=1
			del_node = current.nextnode
			current.nextnode = del_node.nextnode
			del del_node

	def remove_value(self, del_value): #remove the first node that has the del_value
		current = self.head
		if (self.head.value == del_value):
			del_node = self.head
			self.head = self.head.nextnode
			del del_node
		else:
			while(current.nextnode.value != del_value):
				current = current.nextnode
			del_node = current.nextnode
			current.nextnode = del_node.nextnode
			del del_node

	def remove_all_value(self, del_value): #remove all the node that has the del_value
		current = self.head
		while(current.nextnode!=None):
			#print(current.value)
			if(self.head.value == del_value):
				current = current.nextnode
				del_node = self.head
				self.head = current
				del del_node
			elif (current.nextnode.value == del_value):
				del_node = current.nextnode
				if(del_node != self.tail):
					current.nextnode = del_node.nextnode
				else:
					current.nextnode = None
				del del_node
			else:
				current = current.nextnode

		self.tail = current

	def length(self): #return the length if the linked list
		current = self.head
		length = 0
		while (current != None):
			length+=1
			current = current.nextnode
		return length

	def reverse(self): #reverse the linked list
		prevn = None
		current = self.head
		while(current != None):
			nextn = current.nextnode
			current.nextnode = prevn
			prevn = current
			current = nextn
		temp = self.head
		self.head = self.tail
		self.tail = temp

ll = linkedlist()
ll.push(1)
ll.push(0)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

ll.insert(3,'a')
ll.append('a')
ll.push('a')
ll.insert(7,'a')
ll.append('a')
ll.push('a')
ll.append('a')
ll.printlist()

ll.reverse()
ll.printlist()

ll.remove_all_value('a')
ll.printlist()

ll.reverse()
ll.printlist()
