import { useState } from "react";
import "./Tabless.css";

const Tabless = ({ errorData }) => {
  const renderTable = () => {
    return errorData.map((log, index) => {
      return (
        <tr key={log[0]}>
          <td>{log[0]}</td>
          <td>{log[1]}</td>
          <td>{log[2]}</td>
          <td>{log[3]}</td>
          <td>{log[4]}</td>
          <td>{log[5]}</td>
          <a href="#" id="edit">
            Edit
          </a>{" "}
        </tr>
      );
    });
  };

  return (
    <div className="error-table">
      <table>
        <thead>
          <tr>
            <th>STATUS</th>
            <th>NAME</th>
            <th>DOMAIN</th>
            <th>MEMEBER CLASS</th>
            <th>DATE JOINED</th>
            <th>LEVEL/ORDER</th>
          </tr>
        </thead>
        <tbody>{renderTable()}</tbody>
      </table>
    </div>
  );
};

export default Tabless;
