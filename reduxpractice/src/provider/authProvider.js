import axios from 'axios';
import React, {
    createContext,
    useContext,
    useEffect,
    useMemo,
    useState
} from 'react';

function authProvider() {

    const AuthContext = createContext();
    const AuthProvider = ({childeren}) =>{
        
    }

  return (
    <div>authProvider</div>
  )
}

export default authProvider