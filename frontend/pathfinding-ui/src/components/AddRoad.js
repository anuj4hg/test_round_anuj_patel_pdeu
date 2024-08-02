// src/components/AddRoad.js

import React, { useState } from "react";
import { addRoad } from "../apiService";

const AddRoad = () => {
  const [road, setRoad] = useState({ start_location_id: "", end_location_id: "", distance: "", traffic_condition: "" });

  const handleChange = (e) => {
    setRoad({ ...road, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addRoad(road);
    alert("Road added successfully!");
    setRoad({ start_location_id: "", end_location_id: "", distance: "", traffic_condition: "" });
  };

  return (
    <div>
      <h2>Add Road</h2>
      <form onSubmit={handleSubmit}>
        <input name="start_location_id" placeholder="Start Location ID" value={road.start_location_id} onChange={handleChange} />
        <input name="end_location_id" placeholder="End Location ID" value={road.end_location_id} onChange={handleChange} />
        <input name="distance" placeholder="Distance" value={road.distance} onChange={handleChange} />
        <input name="traffic_condition" placeholder="Traffic Condition" value={road.traffic_condition} onChange={handleChange} />
        <button type="submit">Add Road</button>
      </form>
    </div>
  );
};

export default AddRoad;
