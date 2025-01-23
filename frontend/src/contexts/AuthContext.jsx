import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [authTokens, setAuthTokens] = useState(() => 
    localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null
  );
  const [user, setUser] = useState(() => 
    localStorage.getItem('authTokens') ? JSON.parse(atob(localStorage.getItem('authTokens').split('.')[1])) : null
  );

  const loginUser = async (username, password) => {
    const response = await axios.post('/api/token/', {
      username,
      password
    });
    if (response.data) {
      setAuthTokens(response.data);
      setUser(JSON.parse(atob(response.data.access.split('.')[1])));
      localStorage.setItem('authTokens', JSON.stringify(response.data));
    }
  };

  const logoutUser = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem('authTokens');
  };

  useEffect(() => {
    if (authTokens) {
      setUser(JSON.parse(atob(authTokens.access.split('.')[1])));
    }
  }, [authTokens]);

  return (
    <AuthContext.Provider value={{ user, authTokens, loginUser, logoutUser }}>
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
