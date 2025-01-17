import unittest
import numpy as np

from tinygrad.helpers import BEAM
from tinygrad.shape.symbolic import Variable
from tinygrad.tensor import Tensor

class TestBeamSearch(unittest.TestCase):
  def setUp(self):
    self.old_beam = BEAM.value
    BEAM.value = 2
  def tearDown(self):
    BEAM.value = self.old_beam

  def test_variable_ast_no_beam(self):
    a = Tensor.rand(3, 3).reshape((Variable("a", 1, 10).bind(3), 3))
    a = (a+1).realize()

  def test_no_mutate_rawbuffers(self):
    a = Tensor.rand(3, 3).realize()
    desired = a.numpy() + 1
    a.assign(a+1)
    actual = a.numpy()
    np.testing.assert_allclose(actual, desired)
