from unittest import TestCase
from unittest.mock import patch

import arrow

from utils.templatetags.moment import moment

class TestMomentFunction(TestCase):

    def test_method(self):
        with patch('arrow.get') as mock_get:
            moment('2019-08-14T23:24:42.327000+08:00')
            mock_get.assert_called_once()
