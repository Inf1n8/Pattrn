import { useState, useEffect } from "react";
import axios from "axios";
import { API_URL } from "./Config";

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get(`${API_URL}/hello`).then(function (response) {
      console.log(response.data);
      setUsers(response.data.data);
    });
  }, []);

  return (
    <div className="App">
      <div className="content">
        <h1>App Component</h1>
        <ul>
          {users.map((ele, ind) => {
            return (
              <li key={ind}>
                {ele.name} is {ele.age} years old
              </li>
            );
          })}
        </ul>
      </div>
    </div>
  );
}

export default App;
