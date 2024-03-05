import {BrowserRouter,Routes,Route,Navigate} from "react-router-dom";
import {LoginPage} from "./pages/LoginPage/LoginPage.jsx";
import {RegisterPage} from "./pages/RegisterPage/RegisterPage.jsx";
import {HomePage} from "./pages/HomePage/HomePage.jsx";

export default function App(){

  return(
    <BrowserRouter>
      <Routes>
      <Route path="/" element={<Navigate to="/login"/>}/>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/register" element={<RegisterPage/>}/>
        <Route path="/home" element={<HomePage/>}/>
      </Routes>
    </BrowserRouter>
  );
}