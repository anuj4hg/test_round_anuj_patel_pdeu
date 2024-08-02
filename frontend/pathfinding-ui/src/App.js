// src/components/App.js

import React from "react";
import AddLocation from "./components/AddLocation";
import AddRoad from "./components/AddRoad";
import UpdateTrafficCondition from "./components/UpdateTrafficCondition";
import GetShortestPath from "./components/GetShortestPath";

const App = () => {
  return (
    <div>
      <h1>Pathfinding API</h1>
      <nav>
        <a href="#add-location">Add Location</a> | <a href="#add-road">Add Road</a> |{" "}
        <a href="#update-traffic">Update Traffic Condition</a> | <a href="#get-path">Get Shortest Path</a>
      </nav>
      <div id="add-location">
        <AddLocation />
      </div>
      <div id="add-road">
        <AddRoad />
      </div>
      <div id="update-traffic">
        <UpdateTrafficCondition />
      </div>
      <div id="get-path">
        <GetShortestPath />
      </div>
    </div>
  );
};

export default App;
