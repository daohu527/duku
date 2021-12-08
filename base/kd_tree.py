# Copyright 2021 daohu527@gmail.com

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Created Date: 2021-11-15
# Author: daohu527

from typing import List
from operator import itemgetter


def get_k_median(arr, axis):
  arr.sort(key=itemgetter(axis))
  return len(arr) // 2

class Node:
  def __init__(self, val) -> None:
    self.val = val
    self.left = None
    self.right = None

class KdTree:
  def __init__(self, points = None) -> None:
    if not points:
      assert len(points[0]) != 0, "Element is empty!"
      self._k = len(points[0])
      self._root = self.construct(points, 0)
    else:
      self._root = None

  def add(self, point) -> bool:
    assert self._root, "KdTree is empty!"
    pass

  def delete(self, point) -> bool:
    assert self._root, "KdTree is empty!"
    pass

  def query(self, n) -> List[Node]:
    assert self._root, "KdTree is empty!"
    pass

  def query_radius(self, radius) -> List[Node]:
    assert self._root, "KdTree is empty!"
    pass

  def display(self) -> None:
    assert self._root, "KdTree is empty!"
    cur_s = [self._root]
    while cur_s:
      next_s = []
      for c in cur_s:
        print(c.val)
        if c.left:
          next_s.append(c.left)
        if c.right:
          next_s.append(c.right)
      cur_s = next_s

  def construct(self, points, depth) -> Node:
    if not points:
        return None
    axis = depth % self._k
    median = get_k_median(points, axis)
    node = Node(points[median])
    node.left = self.construct(points[:median], depth + 1)
    node.right = self.construct(points[median+1:], depth + 1)
    return node


if __name__ == '__main__':
  points = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
  tree = KdTree(points)
  print(tree.display())
