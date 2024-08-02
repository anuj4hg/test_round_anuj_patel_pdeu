// src/components/AddLocation.js

import React, { useState } from "react";
import { addLocation } from "../apiService";

const AddLocation = () => {
  const [location, setLocation] = useState({ name: "", latitude: "", longitude: "" });

  const handleChange = (e) => {
    setLocation({ ...location, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addLocation(location);
    alert("Location added successfully!");
    setLocation({ name: "", latitude: "", longitude: "" });
  };

  return (
    <div>
      <h2>Add Location</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" placeholder="Name" value={location.name} onChange={handleChange} />
        <input name="latitude" placeholder="Latitude" value={location.latitude} onChange={handleChange} />
        <input name="longitude" placeholder="Longitude" value={location.longitude} onChange={handleChange} />
        <button type="submit">Add Location</button>
      </form>
    </div>
  );
};

export default AddLocation;
