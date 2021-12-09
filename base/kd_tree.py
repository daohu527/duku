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


MAX_INT = 2**31 - 1


def get_k_median(arr, axis):
  arr.sort(key=itemgetter(axis))
  return len(arr) // 2

def euclidean_distance(arr1, arr2):
  assert len(arr1) == len(arr2), "Elements are not equal in size!"
  sum_square = 0
  for x1, x2 in zip(arr1, arr2):
    sum_square += pow(x1 - x2, 2)
  return pow(sum_square, 0.5)

class Node:
  def __init__(self, element, axis) -> None:
    self.element = element
    self.axis = axis
    self.value = element[axis]
    self.left = None
    self.right = None

# Return the nearest node, if there are multiple, only return the first node.
def _query_nearest(point, node, nearest, distance):
  if not node:
    return

  if point[node.axis] <= node.value:
    _query_nearest(point, node.left, nearest, distance)
  else:
    _query_nearest(point, node.right, nearest, distance)

  if point[node.axis] <= node.value:
    if point[node.axis] + distance[0] > node.value:
      # check parent node
      t_distance = euclidean_distance(node.element, point)
      if t_distance < distance[0]:
        distance[0] = t_distance
        nearest[0] = node.element

      _query_nearest(point, node.right, nearest, distance)
  else:
    if point[node.axis] - distance[0] < node.value:
      # check parent node
      t_distance = euclidean_distance(node.element, point)
      if t_distance < distance[0]:
        distance[0] = t_distance
        nearest[0] = node.element

      _query_nearest(point, node.left, nearest, distance)

def insert(nn, ele) -> None:
  nn.append(ele)
  nn.sort(key=itemgetter(1))
  del nn[-1]

def _query_knn(point, node, nn):
  if not node:
    return

  if point[node.axis] <= node.value:
    _query_knn(point, node.left, nn)
  else:
    _query_knn(point, node.right, nn)

  if point[node.axis] <= node.value:
    if point[node.axis] + nn[-1][1] > node.value:
      t_distance = euclidean_distance(node.element, point)
      if t_distance < nn[-1][1]:
        insert(nn, (node.element, t_distance))
      _query_knn(point, node.right, nn)
  else:
    if point[node.axis] - nn[-1][1] < node.value:
      t_distance = euclidean_distance(node.element, point)
      if t_distance < nn[-1][1]:
        insert(nn, (node.element, t_distance))
      _query_knn(point, node.left, nn)

def _query_radius(point, node, plist, radius):
  if not node:
    return

  if point[node.axis] <= node.value:
    _query_radius(point, node.left, plist, radius)
  else:
    _query_radius(point, node.right, plist, radius)

  if point[node.axis] <= node.value:
    if point[node.axis] + radius >= node.value:
      t_distance = euclidean_distance(node.element, point)
      if t_distance <= radius:
        plist.append(node.element)
      _query_radius(point, node.right, plist, radius)
  else:
    if point[node.axis] - radius <= node.value:
      t_distance = euclidean_distance(node.element, point)
      if t_distance <= radius:
        plist.append(node.element)
      _query_radius(point, node.left, plist, radius)


class KdTree:
  def __init__(self, points = None) -> None:
    if points:
      assert len(points[0]) != 0, "Element is empty!"
      self._k = len(points[0])
      self._root = self._construct(points, 0)
    else:
      self._root = None

  def _construct(self, points, depth) -> Node:
    if not points:
        return None
    axis = depth % self._k
    median = get_k_median(points, axis)
    node = Node(points[median], axis)
    node.left = self._construct(points[:median], depth + 1)
    node.right = self._construct(points[median+1:], depth + 1)
    return node

  def add(self, point) -> bool:
    assert self._root, "KdTree is empty!"
    pass

  def delete(self, point) -> bool:
    assert self._root, "KdTree is empty!"
    pass

  def balance(self) -> None:
    pass

  def query_knn(self, point, k) -> List[tuple]:
    assert self._root, "KdTree is empty!"

    nn = [(None, MAX_INT)] * k
    _query_knn(point, self._root, nn)
    return [n[0] for n in nn]

  def query_nearest(self, point) -> tuple:
    assert self._root, "KdTree is empty!"

    # Need to pass by ref, so we pass a list
    nearest = [None]
    distance = [MAX_INT] # init max value
    _query_nearest(point, self._root, nearest, distance)
    return nearest[0], distance[0]

  def query_radius(self, point, radius) -> List[tuple]:
    assert self._root, "KdTree is empty!"
    plist = []
    _query_radius(point, self._root, plist, radius)
    return plist

  def display(self) -> None:
    assert self._root, "KdTree is empty!"
    cur_s = [self._root]
    while cur_s:
      next_s = []
      for c in cur_s:
        print(c.element, c.axis)
        if c.left:
          next_s.append(c.left)
        if c.right:
          next_s.append(c.right)
      cur_s = next_s


if __name__ == '__main__':
  points = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
  tree = KdTree(points)
  print(tree.display())

  print(euclidean_distance((1,2),(3,4)))

  nearest, distance = tree.query_nearest((7,6))
  print(nearest, distance)

  knn = tree.query_knn((7,6), 2)
  print(knn)

  r = tree.query_radius((7,6), 1)
  print(r)

  r = tree.query_radius((7,6), 4)
  print(r)
