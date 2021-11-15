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

from base.aabb_box_tree import AABBBoxTree

class HdmapManager:
  def __init__(self) -> None:
    self._aabb_box_tree = None

  def getNearestLane(point):
    pass

  def getNearestLaneWithHeading(point, heading):
    pass

  def GetSignals(point, distance):
    pass

  def GetFrontNearestSignals(point, distance):
    pass
