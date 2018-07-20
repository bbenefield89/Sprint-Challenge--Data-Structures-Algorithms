class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    done = False
    stack = []
    stack_map = {}
    output = []
    current_node = self
    parent_node = None
    

    while not done:
      # check if we have already seen this node
      if not stack_map.get(current_node):
        stack.append(current_node)
        stack_map[ current_node ] = current_node
        cb(current_node.value)

      # if left exists and has not been hashed
      if current_node.left and not stack_map.get(current_node.left):
        current_node = current_node.left
        continue
      # if right exists and has not been hashed
      elif current_node.right and not stack_map.get(current_node.right):
        current_node = current_node.right
        continue
      else:
        del stack[-1] # remove last index of stack

        # break loop condition
        if len(stack) == 0:
          break
          
        # after removing the current node from our stack we can now traverse back up to our parent node
        current_node = stack[-1]

  def breadth_first_for_each(self, cb):
    done = False
    queue = []
    queue_map = {}
    current_node = self

    queue.append(current_node)
    queue_map[ current_node ] = current_node
    cb(current_node.value)

    while not done:
      if current_node.left:
        if not queue_map.get(current_node.left):
          queue.append(current_node.left)
          queue_map[ current_node.left ] = current_node.left

          cb(current_node.left.value)
          
      if current_node.right:
        if not queue_map.get(current_node.right):
          queue.append(current_node.right)
          queue_map[ current_node.right ] = current_node.right

          cb(current_node.right.value)
      
      del queue[0]

      if len(queue) == 0:
        break

      current_node = queue[0]

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
