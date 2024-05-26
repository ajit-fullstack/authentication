import React from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Contact from "./pages/Contact";
import LoginReg from "./pages/auth/LoginReg";
import SendPasswordResetEmail from "./pages/auth/SendPasswordResetEmail";
import ResetPassword from "./pages/auth/ResetPassword";
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />} >
            <Route index element={<Home />}/>
            <Route path="contact" element={<Contact />}/>
            <Route path="login" element={<LoginReg />}/>
            <Route path="sendpasswordresetemail" element={<SendPasswordResetEmail />}/>
            <Route path="passwordreset" element={<ResetPassword />}/>
          </Route>
          <Route path="/dashboard" element={ <Dashboard /> }/>
          <Route path="*" element={<h1>Error 404 Page not found !!</h1>} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
