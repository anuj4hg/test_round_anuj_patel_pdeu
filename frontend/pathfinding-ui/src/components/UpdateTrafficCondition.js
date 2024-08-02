// src/components/UpdateTrafficCondition.js

import React, { useState } from "react";
import { updateTrafficCondition } from "../apiService";

const UpdateTrafficCondition = () => {
  const [trafficUpdate, setTrafficUpdate] = useState({ road_id: "", timestamp: "", traffic_condition: "" });

  const handleChange = (e) => {
    setTrafficUpdate({ ...trafficUpdate, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await updateTrafficCondition(trafficUpdate);
    alert("Traffic condition updated successfully!");
    setTrafficUpdate({ road_id: "", timestamp: "", traffic_condition: "" });
  };

  return (
    <div>
      <h2>Update Traffic Condition</h2>
      <form onSubmit={handleSubmit}>
        <input name="road_id" placeholder="Road ID" value={trafficUpdate.road_id} onChange={handleChange} />
        <input name="timestamp" placeholder="Timestamp" value={trafficUpdate.timestamp} onChange={handleChange} />
        <input name="traffic_condition" placeholder="Traffic Condition" value={trafficUpdate.traffic_condition} onChange={handleChange} />
        <button type="submit">Update Traffic Condition</button>
      </form>
    </div>
  );
};

export default UpdateTrafficCondition;
