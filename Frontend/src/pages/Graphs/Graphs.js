import { useState } from "react";
import BarChart from "../../components/Graph/BarChart";
import LineChart from "../../components/Graph/LineChart";
import PieChart from "../../components/Graph/PieChart";
import { UserData } from "../../data/Data";

function Graph() {
  const [userData, setUserData] = useState({
    labels: UserData.map((data) => data.year),
    datasets: [
      {
        label: "Users Gained",
        data: UserData.map((data) => data.userGain),
        backgroundColor: [
          "rgba(75,192,192,1)",
          "#ecf0f1",
          "#50AF95",
          "#f3ba2f",
          "#2a71d0",
        ],
        borderColor: "black",
        borderWidth: 2,
      },
    ],
  });

  return (
    <div className="parent">
      <div className="child">
        <BarChart chartData={userData} />
      </div>
      <div className="child">
        <LineChart chartData={userData} />
      </div>
      <div className="child">
        <PieChart chartData={userData} />
      </div>
    </div>
  );
}

export default Graph;
