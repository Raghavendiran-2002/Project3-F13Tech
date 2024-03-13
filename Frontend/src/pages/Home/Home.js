import React from "react";
import { useNavigate } from "react-router-dom";
import bg from "./bg.png";
const Home = (props) => {
  const { loggedIn, email } = props;
  const navigate = useNavigate();

  const onButtonClick = () => {
    if (loggedIn) {
      localStorage.removeItem("user");
      props.setLoggedIn(false);
    } else {
      navigate("/login");
    }
  };

  return (
    <div className="mainContainer">
      <div className="titleContainer">
        Welcome to F13 Technologies!
        <img className="bg-img" src={bg} alt="hi" />
      </div>
    </div>
  );
};

export default Home;
