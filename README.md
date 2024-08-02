# Anuj Patel - 21BCP411 - Path Finding Task - Shipmnts

## Project Overview

This project is a backend system designed to monitor real-time traffic conditions and provide optimal pathfinding solutions. The system offers APIs to manage traffic data, calculate the shortest paths between locations, and provide real-time traffic updates.

## Features

- **Add Location:** Register new locations with geographic coordinates.
- **Add Road:** Connect locations with roads and update their traffic conditions.
- **Update Traffic Condition:** Modify the traffic condition of a specific road.
- **Get Shortest Path:** Calculate the shortest path between two locations considering current traffic conditions.
- **Get Traffic Condition:** Retrieve the traffic condition of a specific road.
- **Generate Traffic Report:** Analyze traffic conditions over a period of time and generate reports.

## API Endpoints

### 1. Add Location
- **Endpoint:** `POST /locations`
- **Request Body:**
  ```json
  {
    "name": "Location A",
    "latitude": 37.7749,
    "longitude": -122.4194
  }
