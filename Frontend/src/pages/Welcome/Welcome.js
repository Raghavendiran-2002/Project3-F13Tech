import { useNavigate } from "react-router-dom";

function Welcome() {
  const navigate = useNavigate();

  return (
    <div>
      <div className="title">
        {" "}
        <h1>You have successfully logged in!!!</h1>
      </div>
      <div className="welcome-page">
        <div className="buttons">
          <input
            className={"inputButton"}
            type="button"
            onClick={() => {
              navigate("/form");
            }}
            value={"User Form"}
          />
        </div>
        <div className="buttons">
          <input
            className={"inputButton"}
            type="button"
            onClick={() => {
              navigate("/graph");
            }}
            value={"Graph"}
          />
        </div>{" "}
      </div>
      <div className="welcome-page">
        <div className="buttons">
          <input
            className={"inputButton"}
            type="button"
            onClick={() => {
              navigate("/file");
            }}
            value={"File"}
          />
        </div>{" "}
        <div className="buttons">
          <input
            className={"inputButton"}
            type="button"
            onClick={() => {
              navigate("/image");
            }}
            value={"Image"}
          />
        </div>{" "}
      </div>
    </div>
  );
}

export default Welcome;
