import { useState } from "react";
import "./LogTable.css";

const LogTable = ({ errorData }) => {
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
          <td>{log[6]}</td>
          <td>{log[7]}</td>
        </tr>
      );
    });
  };

  return (
    <div className="error-table">
      <table>
        <thead>
          <tr>
            <th>Level</th>
            <th>Message</th>
            <th>Resource ID</th>
            <th>Timestamp</th>
            <th>Trace ID</th>
            <th>Span ID</th>
            <th>Commit</th>
            <th>Parent Resource ID</th>
          </tr>
        </thead>
        <tbody>{renderTable()}</tbody>
      </table>
    </div>
  );
};

export default LogTable;
