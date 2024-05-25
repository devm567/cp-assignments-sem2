class DynamicArray:
  def __init__(self, capacity=10, resize_factor=2):
      self.capacity = capacity
      self.resize_factor = resize_factor
      self.size = 0
      self.data = [None] * capacity

  def __resize(self, new_capacity):
      new_data = [None] * new_capacity
      for i in range(self.size):
          new_data[i] = self.data[i]
      self.data = new_data
      self.capacity = new_capacity

  def insert_at_index(self, index, element):
      if index < 0 or index > self.size:
          raise IndexError("Index out of range")

      if self.size == self.capacity:
          self.__resize(self.capacity * self.resize_factor)

      for i in range(self.size, index, -1):
          self.data[i] = self.data[i - 1]

      self.data[index] = element
      self.size += 1

  def delete_at_index(self, index):
      if index < 0 or index >= self.size:
          raise IndexError("Index out of range")

      for i in range(index, self.size - 1):
          self.data[i] = self.data[i + 1]

      self.data[self.size - 1] = None
      self.size -= 1

      if self.size < self.capacity // self.resize_factor:
          self.__resize(self.capacity // self.resize_factor)

  def get_size(self):
      return self.size

  def is_empty(self):
      return self.size == 0

  def rotate_right(self, k):
      k %= self.size
      self.data = self.data[-k:] + self.data[:-k]

  def reverse(self):
      self.data = self.data[::-1]

  def append(self, element):
      if self.size == self.capacity:
          self.__resize(self.capacity * self.resize_factor)
      self.data[self.size] = element
      self.size += 1

  def prepend(self, element):
      self.insert_at_index(0, element)

  def merge(self, other_array):
      new_capacity = self.size + other_array.size
      while new_capacity > self.capacity:
          new_capacity *= self.resize_factor
      self.__resize(new_capacity)
      for i in range(other_array.size):
          self.data[self.size + i] = other_array.data[i]
      self.size += other_array.size

  def interleave(self, other_array):
      new_capacity = (self.size + other_array.size) * self.resize_factor
      new_data = [None] * new_capacity
      i = 0
      j = 0
      for k in range(self.size + other_array.size):
          if k % 2 == 0 and i < self.size:
              new_data[k] = self.data[i]
              i += 1
          elif j < other_array.size:
              new_data[k] = other_array.data[j]
              j += 1
      self.data = new_data
      self.size = self.size + other_array.size

  def get_middle(self):
      if self.size == 0:
          return None
      return self.data[self.size // 2]

  def index_of(self, element):
      for i in range(self.size):
          if self.data[i] == element:
              return i
      return -1

  def split_at_index(self, index):
      if index < 0 or index >= self.size:
          raise IndexError("Index out of range")
      new_array = DynamicArray(self.capacity, self.resize_factor)
      for i in range(index, self.size):
          new_array.append(self.data[i])
      self.size = index
      return new_array

  def resize_with_custom_factor(self, new_resize_factor):
      if new_resize_factor <= 1:
          raise ValueError("Resize factor should be greater than 1")
      self.resize_factor = new_resize_factor
