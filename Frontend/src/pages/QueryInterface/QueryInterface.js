import React, { useState } from "react";
import axios from "axios";
import "./QueryInterface.css";
import LogTable from "../LogTable/LogTable";

const options = [
  "level",
  "message",
  "resourceId",
  "timestamp",
  "traceId",
  "spanId",
  "commit",
  "parentResourceId",
];
const users = ["admin", "customer"];
const QueryInterface = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [getlog, setData] = useState([]);
  const [selectedOption, setSelectedOption] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [datetime, setDateTime] = useState(false);
  const [user, setUser] = useState("admin");
  const handleOptionChange = (e) => {
    if (e.target.value === "timestamp") setDateTime(true);
    else {
      setDateTime(false);
    }
    setSelectedOption(e.target.value);
  };

  const handleUserChange = (e) => {
    setUser(e.target.value);
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };
  const handleStartDateChange = (e) => {
    setStartDate(e.target.value);
  };

  const handleEndDateChange = (e) => {
    setEndDate(e.target.value);
  };

  const handleSubmit = async (e) => {
    setData([]);
    e.preventDefault();
    console.log(user);
    if (selectedOption === "") {
      alert("Select any option !");
      return;
    }
    if (!datetime && searchTerm === "") {
      alert("Enter Search Term !");
      return;
    }
    if (datetime && startDate === "") {
      alert("Enter Start date !");
      return;
    }
    if (datetime && endDate === "") {
      alert("Enter End date !");
      return;
    }
    try {
      var response = "";
      if (selectedOption === "timestamp") {
        response = await axios({
          method: "get",
          url: `https://f13api.raghavendiran.tech/query-interface?filter=${selectedOption}&start=${startDate}&end=${endDate}&user=${user}`,
        });
      } else {
        response = await axios({
          method: "get",
          url: `https://f13api.raghavendiran.tech/query-interface?search=${searchTerm}&filter=${selectedOption}&user=${user}`,
        });
      }
      setData(response.data.logs);
    } catch (error) {
      console.error("API Error:", error);
      alert("API Error:", error);
    }
  };

  return (
    <div className="container">
      <div className="searchcontiner">
        <form className="formss" onSubmit={handleSubmit}>
          {/* <select value={user} onChange={handleUserChange}>
            {users.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select> */}
          <select value={selectedOption} onChange={handleOptionChange}>
            <option value="">Select an option to be searched</option>
            {options.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
          {datetime ? (
            <p></p>
          ) : (
            <input
              type="text"
              placeholder="Search..."
              value={searchTerm}
              onChange={handleSearchChange}
            />
          )}
          {datetime === true ? (
            <div>
              <label className="from">From :</label>
              <input
                type="text"
                value={startDate}
                placeholder="2023-09-15T08:00:00Z"
                onChange={handleStartDateChange}
              />
              <br />
              <label className="to">To &nbsp;&nbsp;:</label>
              <input
                type="text"
                value={endDate}
                placeholder="2023-09-15T08:00:00Z"
                onChange={handleEndDateChange}
              />
            </div>
          ) : (
            <p></p>
          )}
          <input className={"submit-button"} type="submit" />
        </form>
      </div>

      <div className="error-table">
        <LogTable errorData={getlog} />
      </div>
    </div>
  );
};

export default QueryInterface;
