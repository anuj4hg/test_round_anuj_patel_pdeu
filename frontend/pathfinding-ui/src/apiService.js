// src/apiService.js

const API_BASE_URL = "http://127.0.0.1:5000";

export const addLocation = async (location) => {
  const response = await fetch(`${API_BASE_URL}/locations`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(location),
  });
  return response.json();
};

export const addRoad = async (road) => {
  const response = await fetch(`${API_BASE_URL}/roads`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(road),
  });
  return response.json();
};

export const updateTrafficCondition = async (trafficUpdate) => {
  const response = await fetch(`${API_BASE_URL}/traffic-updates`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(trafficUpdate),
  });
  return response.json();
};

export const getShortestPath = async (startLocationId, endLocationId) => {
  const response = await fetch(
    `${API_BASE_URL}/shortest-path?start_location_id=${startLocationId}&end_location_id=${endLocationId}`
  );
  return response.json();
};
