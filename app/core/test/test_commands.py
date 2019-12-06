from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase
from neobolt.exceptions import ServiceUnavailable


class CammandsTestCase(TestCase):

    def test_wait_for_db_ready(self):
        """Test wait_for_db to check db is up and running"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=None)
    def test_for_db(self, ts):
        """Test for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)

    def test_wait_for_graph_db(self):
        """Test wait_for_graphdb to check neo4j up and running"""
        with patch('neomodel.db.set_connection') as gi:
            gi.side_effect = None
            call_command('wait_for_graphdb')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=None)
    def test_for_graph_db(self, ts):
        """Test for graph db"""
        with patch("neomodel.db.set_connection") as gi:
            gi.side_effect = [ServiceUnavailable] * 5 + [True]
            call_command('wait_for_graphdb')
            self.assertEqual(gi.call_count, 6)
