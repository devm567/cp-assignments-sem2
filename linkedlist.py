class Node:
  def __init__(self, data, prev=None, next=None):
      self.data = data
      self.prev = prev
      self.next = next

class dll:
  def __init__(self):
      self.__head = None
      self.__tail = None
      self.__size = 0

  def size(self):
      return self.__size

  def isEmpty(self):
      return self.size() == 0

  def append(self, data):
      newNode = Node(data)
      if self.isEmpty():
          self.__head = newNode
          self.__tail = newNode
      else:
          self.__tail.next = newNode
          newNode.prev = self.__tail
          self.__tail = newNode
      self.__size += 1

  def prepend(self, data):
      newNode = Node(data)
      if self.isEmpty():
          self.__head = newNode
          self.__tail = newNode
      else:
          self.__head.prev = newNode
          newNode.next = self.__head
          self.__head = newNode
      self.__size += 1

  def add(self, data, index):
      if index < 0 or index > self.__size:
          raise IndexError("Index out of range")

      if index == 0:
          self.prepend(data)
      elif index == self.__size:
          self.append(data)
      else:
          id = 0
          trav = self.__head
          while id != index - 1:
              trav = trav.next
              id += 1
          newNode = Node(data, trav, trav.next)
          trav.next.prev = newNode
          trav.next = newNode
          self.__size += 1

  def removeFirst(self):
      if self.isEmpty():
          raise IndexError("List is empty")

      else:
          temp = self.__head
          self.__head = self.__head.next
          if self.__head is not None:
              self.__head.prev = None
          else:
              self.__tail = None
          del temp

      self.__size -= 1

  def removeLast(self):
      if self.isEmpty():
          raise IndexError("List is empty")
      else:
          temp = self.__tail
          self.__tail = self.__tail.prev
          if self.__tail is not None:
              self.__tail.next = None
          else:
              self.__head = None
          del temp

      self.__size -= 1

  def __iter__(self):
      self.__trav = self.__head
      return self

  def __next__(self):

      if self.__trav is None:
          raise StopIteration

      x = self.__trav.data
      self.__trav = self.__trav.next
      return x

  def __str__(self):
      li = []
      trav = self.__head
      while trav is not None:
          li.append(str(trav.data))
          trav = trav.next
      return '<---->'.join(li)

  def insert_at_index(self, index, data):
      self.add(data, index)

  def delete_at_index(self, index):
      if index < 0 or index >= self.__size:
          raise IndexError("Index out of range")
      if index == 0:
          self.removeFirst()
      elif index == self.__size - 1:
          self.removeLast()
      else:
          id = 0
          trav = self.__head
          while id != index:
              trav = trav.next
              id += 1
          trav.prev.next = trav.next
          trav.next.prev = trav.prev
          del trav
          self.__size -= 1

  def rotate_right(self, k):
      if self.__size == 0:
          return
      k = k % self.__size
      if k == 0:
          return
      for _ in range(k):
          last_node = self.__tail
          self.__tail = last_node.prev
          self.__tail.next = None
          last_node.next = self.__head
          self.__head.prev = last_node
          self.__head = last_node

  def reverse(self):
      current = self.__head
      while current:
          temp = current.prev
          current.prev = current.next
          current.next = temp
          current = current.prev
      if temp:
          self.__head = temp.prev

  def merges(self, other_list):
      if not other_list.isEmpty():
          if self.isEmpty():
              self.__head = other_list.__head
              self.__tail = other_list.__tail
          else:
              self.__tail.next = other_list.__head
              other_list.__head.prev = self.__tail
              self.__tail = other_list.__tail
          self.__size += other_list.size()
          other_list.__size = 0
          other_list.__head = None
          other_list.__tail = None

  def interleaves(self, other_list):
      if not other_list.isEmpty():
          trav1 = self.__head
          trav2 = other_list.__head
          while trav1 and trav2:
              temp1 = trav1.next
              temp2 = trav2.next
              trav1.next = trav2
              trav2.prev = trav1
              trav2.next = temp1
              if temp1:
                  temp1.prev = trav2
              trav1 = temp1
              trav2 = temp2
          other_list.__head = None
          other_list.__tail = None
          other_list.__size = 0

  def get_middle(self):
      if self.isEmpty():
          return None
      slow = self.__head
      fast = self.__head
      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
      return slow.data

  def index_of(self, data):
      index = 0
      current = self.__head
      while current:
          if current.data == data:
              return index
          current = current.next
          index += 1
      return -1

  def split_at_index(self, index):
      if index < 0 or index >= self.__size:
          raise IndexError("Index out of range")
      if index == 0:
          new_list = dll()
          new_list.__head = self.__head
          new_list.__tail = self.__tail
          self.__head = None
          self.__tail = None
          self.__size = 0
          return new_list
      id = 0
      trav = self.__head
      while id != index:
          trav = trav.next
          id += 1
      new_list = dll()
      new_list.__head = trav
      new_list.__tail = self.__tail
      trav.prev.next = None
      self.__tail = trav.prev
      trav.prev = None
      self.__size = index
      new_list.__size = self.size() - index
      return new_list



l = dll()
l.append(1)
l.append(2)
l.prepend(0)
print("List after append and prepend:", [node for node in l])
print("Size of list:", l.size())
print("Is list empty?:", l.isEmpty())

l.insert_at_index(2, 1.5)
print("List after insertion:", [node for node in l])
