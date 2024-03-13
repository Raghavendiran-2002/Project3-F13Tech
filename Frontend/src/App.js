import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import { useState, useEffect } from "react";
import Home from "./pages/Home/Home";
import Login from "./pages/Login/Login";
import Welcome from "./pages/Welcome/Welcome";
import Form from "./pages/Form/Form";
import Graph from "./pages/Graphs/Graphs";
import FileUpload from "./pages/File/File";
import ImageUpload from "./pages/ImageUploader/ImageUploader";
import Navbar from "./components/Navbar/Navbar";
import ViewFormData from "./pages/ViewFormData/ViewFormData";
import QueryInterface from "./pages/QueryInterface/QueryInterface";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [email, setEmail] = useState("");

  useEffect(() => {
    // Fetch the user email and token from local storage
    const user = JSON.parse(localStorage.getItem("user"));

    // If the token/email does not exist, mark the user as logged out
    if (!user || !user.token) {
      setLoggedIn(true);
      return;
    }

    // If the token exists, verify it with the auth server to see if it is valid
    fetch("http://localhost:3080/verify", {
      method: "POST",
      headers: {
        "jwt-token": user.token,
      },
    })
      .then((r) => r.json())
      .then((r) => {
        setLoggedIn("success" === r.message);
        setEmail(user.email || "");
      });
  }, []);

  return (
    <div className="App">
      <BrowserRouter>
        <Navbar />

        <Routes>
          <Route
            path="/"
            element={
              <Home
                email={email}
                loggedIn={loggedIn}
                setLoggedIn={setLoggedIn}
              />
            }
          />
          <Route
            path="/login"
            element={<Login setLoggedIn={setLoggedIn} setEmail={setEmail} />}
          />
          <Route path="/welcome" element={<Welcome />} />
          <Route path="/auth" element={<QueryInterface />} />

          <Route path="/product" element={<Form />} />
          <Route path="/technology" element={<Graph />} />
          <Route path="/services" element={<FileUpload />} />
          <Route path="/company" element={<ImageUpload />} />
          <Route
            path="/resouces"
            element={
              <ViewFormData
                itemsPerPage={4}
                items={[1, 2, 3, 4, 5, 6, 7, 8, 9]}
              />
            }
          />

          {/* <Route
            path="/admin"
            element={<Admin setLoggedIn={setLoggedIn} setEmail={setEmail} />}
          /> */}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
