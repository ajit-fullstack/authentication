import axios from 'axios';
import React, {
    createContext,
    useContext,
    useEffect,
    useMemo,
    useState
} from 'react';

const AuthContext = createContext();

const AuthProvider = ({childeren}) =>{

  // State to hold the authentication token
  const [token, setToken_] = useState(localStorage.getItem("token"));

  // Function to set the authentication token
  const setToken = (newToken) => {
    setToken_(newToken);
  };


  return (
    <div>authProvider</div>
  )
}

export default AuthProvider