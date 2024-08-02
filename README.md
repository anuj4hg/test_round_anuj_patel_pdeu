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
Certainly! I'll create a text file with the README content. Here's how you can save this as a file named README.md:

Open a text editor on your computer.
Copy and paste the following content into the text editor:

Copy# Real-Time Traffic Monitoring and Pathfinding System

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

- **Response:** 201 Created with the created location.

### 2. Add Road

- **Endpoint:** POST /roads
- **Request Body:**
  ```json{
  "start_location_id": 1,
  "end_location_id": 2,
  "distance": 5,
  "traffic_condition": "clear"
}

- **Response:** 201 Created with the created road.

### 3. Update Traffic Condition

- **Endpoint:** POST /traffic-updates
- **Request Body:**
  ```json{
  "road_id": 1,
  "timestamp": "2024-06-25T14:00:00Z",
  "traffic_condition": "heavy"
}

 - **Response:** 201 Created with the created traffic update.

### 4. Get Shortest Path

- **Endpoint:** GET /shortest-path
- **Request Parameters:** start_location_id, end_location_id
- **Response:** 200 OK with the calculated path:
  ```json{
  "path": ["a_location_id", "b_location_id", "c_location_id"],
  "total_distance": 10,
  "estimated_time": 15
}


### 5. Get Traffic Condition (BONUS)

- **Endpoint:** GET /roads/{id}/traffic-condition
- **Response:** 200 OK with the traffic condition of the specified road.

### 6. Generate Traffic Report (BONUS)

- **Endpoint:** GET /report/traffic
Response: 200 OK with a CSV report of all roads and their traffic conditions.

### Logic and Algorithms

The shortest path between two locations is calculated using Dijkstra's algorithm, considering the current traffic conditions.
Traffic conditions are updated in real-time, allowing the system to provide dynamic routing recommendations.

### Project Setup
#### Prerequisites

- Python 3
- Flask
- SQLAlchemy

### Installation

Clone the repository:
bashCopygit clone https://github.com/anujtpatel2004codes/test_round_anuj_patel_pdeu.git
cd test_round_anuj_patel_pdeu

Set up the virtual environment and install dependencies:
bashCopypython3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run the Flask application:
flask run


Usage
Use the provided API endpoints to add locations, roads, update traffic conditions, and calculate the shortest path between locations.
