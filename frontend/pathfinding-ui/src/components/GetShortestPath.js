// src/components/GetShortestPath.js

import React, { useState } from "react";
import { getShortestPath } from "../apiService";

const GetShortestPath = () => {
  const [startLocationId, setStartLocationId] = useState("");
  const [endLocationId, setEndLocationId] = useState("");
  const [path, setPath] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await getShortestPath(startLocationId, endLocationId);
    setPath(result);
  };

  return (
    <div>
      <h2>Get Shortest Path</h2>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Start Location ID"
          value={startLocationId}
          onChange={(e) => setStartLocationId(e.target.value)}
        />
        <input
          placeholder="End Location ID"
          value={endLocationId}
          onChange={(e) => setEndLocationId(e.target.value)}
        />
        <button type="submit">Get Path</button>
      </form>
      {path && (
        <div>
          <h3>Path Info</h3>
          <p>Path: {path.path.join(" -> ")}</p>
          <p>Total Distance: {path.total_distance}</p>
          <p>Estimated Time: {path.estimated_time}</p>
        </div>
      )}
    </div>
  );
};

export default GetShortestPath;
