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

class Point3d:
  def __init__(self, x, y, z) -> None:
    self.x = x
    self.y = y
    self.z = z

  def isFront(self, point):
    pass

  def isBack(self, point):
    pass

  def isLeft(self, point):
    pass

  def isRight(self, point):
    pass

  def __str__(self) -> str:
    return "Point3d x: {}, y: {}, z: {}".format(self.x, self.y, self.z)
