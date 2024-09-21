class LinkedStack:
	def __init__(self):
		self._top = None
		self._count = 0

	class Node:
		def __init__(self, data, next=None):
			self.data = data
			self.next = next
   
	def count(self):
		return self._count

	def isEmpty(self):
		return self._count == 0

	def isFull(self):
		raise NotImplementedError("isFull is not implemented as in-approprite for Linked Nodes")

	def push(self, val):
		tmp = self.Node(val)
		if not self.isEmpty():
			tmp.next = self._top
		self._top = tmp
		self._count = self._count + 1

	def pop(self):
		if self.isEmpty():
			raise Exception("Stack empty")
		else:
			tmp = self._top
			self._top = tmp.next
			tmp.next = None
			self._count = self._count - 1
			return tmp.data

	def printStack(self):
		tmp = self._top
		while tmp:
			print(tmp.data)
			tmp = tmp.next