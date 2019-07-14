#Implementation of a doubly linked list
class node:
	def __init__(self, value, nextnode = None, prevnode = None):
		self.value = value
		self.nextnode = nextnode
		self.prevnode = prevnode

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
			newnode.prevnode = self.tail
			self.tail.nextnode = newnode
			self.tail = newnode
	
	def prepend(self, newvalue): #add a node at the beginning of the linked list
		newnode = node(newvalue)
		if (self.head == None):
			self.head = newnode
			self.tail = newnode
		else:
			newnode.nextnode = self.head
			self.head.prevnode = newnode
			self.head = newnode

	def printlist(self, reverse=False): # print the whole linked list
		lst = []
		if (not reverse):				# print the list from head to tail
			current = self.head
			while(current != None):
				lst.append(current.value)
				current = current.nextnode
		else:							# print the list from tail to head
			current = self.tail
			while(current != None):
				lst.append(current.value)
				current = current.prevnode
		print(lst)

	
	def insert(self, position, value): # insert a node to a given position
		newnode = node(value)
		current = self.head
		index = 0

		while(index!=position):
			current = current.nextnode
			index+=1
		newnode.nextnode = current
		newnode.prevnode = current.prevnode
		current.prevnode = newnode
		newnode.prevnode.nextnode = newnode
	
	def remove_position(self, position): #remove node with a given position
		current = self.head
		index = 0

		if (position==0):
			del_node = self.head
			self.head = del_node.nextnode
			self.head.prevnode = None
			del del_node
		else:
			while(current!=None and index!=position):
				current = current.nextnode
				index+=1
			if current!=None:
				del_node = current.nextnode
				current.prevnode.nextnode = current.nextnode
				current.nextnode.prevnode = current.prevnode
				del del_node

	def remove_value(self, del_value): #remove the first node that has the del_value
		current = self.head
		if (self.head.value == del_value):
			del_node = self.head
			self.head = del_node.nextnode
			self.head.prevnode = None
			del del_node
		else:
			while(current!=None and current.value != del_value):
				current = current.nextnode
			if current != None:
				del_node = current.nextnode
				current.prevnode.nextnode = current.nextnode
				current.nextnode = del_node.nextnode
				current.nextnode.prevnode = current.prevnode
				del del_node

	def remove_all_value(self, del_value): #remove all the node that has the del_value
		current = self.head
		while(current!=None):
			if(self.head.value == del_value):
				del_node = self.head
				self.head = del_node.nextnode
				self.head.prevnode = None
				del del_node
			elif (current.value == del_value):
				del_node = current.nextnode
				current.prevnode.nextnode = current.nextnode
				current.nextnode = del_node.nextnode
				current.nextnode.prevnode = current.prevnode
				del del_node
			current = current.nextnode
	
	def length(self): #return the length if the linked list
		current = self.head
		length = 0
		while (current != None):
			length+=1
			current = current.nextnode
		return length

ll = linkedlist()
ll.append(0)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.prepend('a')
ll.insert(3,'a')
ll.prepend('b')
ll.printlist()
ll.remove_all_value('a')
ll.printlist()
ll.remove_value('b')
ll.printlist()
