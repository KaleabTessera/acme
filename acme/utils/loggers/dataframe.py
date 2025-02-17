# Copyright 2018 DeepMind Technologies Limited. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Logger for writing to an in-memory list.

This is convenient for e.g. interactive usage via Google Colab.
"""

from typing import Sequence

from acme.utils.loggers import base


class InMemoryLogger(base.Logger):
  """A simple logger that keeps all data in memory."""

  def __init__(self):
    self._data = []

  def write(self, data: base.LoggingData):
    self._data.append(data)

  def to_dataframe(self):
    """Builds a Pandas DataFrame from data in memory."""
    raise NotImplementedError(
        'This method has been deprecated. '
        'Please use pandas.DataFrame(InMemoryLogger.data) instead.')

  @property
  def data(self) -> Sequence[base.LoggingData]:
    return self._data
