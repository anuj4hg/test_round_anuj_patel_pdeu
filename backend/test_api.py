# test_api.py
import unittest
from flask_testing import TestCase
from backend import app, db
from backend.models import Location, Road

class APITestCase(TestCase):
    def create_app(self):
        app.config.from_object('config_test.TestConfig')
        return app

    def setUp(self):
        db.create_all()

        # Add some initial data
        location1 = Location(name="Location A", latitude=37.7749, longitude=-122.4194)
        location2 = Location(name="Location B", latitude=34.0522, longitude=-118.2437)
        db.session.add_all([location1, location2])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_location(self):
        response = self.client.post('/locations', json={"name": "Location C", "latitude": 40.7128, "longitude": -74.0060})
        self.assertEqual(response.status_code, 201)

    def test_add_road(self):
        response = self.client.post('/roads', json={"start_location_id": 1, "end_location_id": 2, "distance": 5, "traffic_condition": "clear"})
        self.assertEqual(response.status_code, 201)

    def test_update_traffic(self):
        self.client.post('/roads', json={"start_location_id": 1, "end_location_id": 2, "distance": 5, "traffic_condition": "clear"})
        response = self.client.post('/traffic-updates', json={"road_id": 1, "timestamp": "2024-06-25T14:00:00Z", "traffic_condition": "heavy"})
        self.assertEqual(response.status_code, 201)

    def test_get_shortest_path(self):
        self.client.post('/roads', json={"start_location_id": 1, "end_location_id": 2, "distance": 5, "traffic_condition": "clear"})
        response = self.client.get('/shortest-path?start_location_id=1&end_location_id=2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('path', response.json)

    def test_get_traffic_condition(self):
        self.client.post('/roads', json={"start_location_id": 1, "end_location_id": 2, "distance": 5, "traffic_condition": "clear"})
        response = self.client.get('/roads/1/traffic-condition')
        self.assertEqual(response.status_code, 200)
        self.assertIn('traffic_condition', response.json)

if __name__ == '__main__':
    unittest.main()
