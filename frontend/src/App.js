import React, { useState, useEffect } from 'react';
import './App.css';
import RegisterForm from './components/RegisterForm';

function App() {
  const [data, setData] = useState({ message: 'Loading...' });
  const [showRegister, setShowRegister] = useState(false);

  useEffect(() => {
    // Simulate API response
    setTimeout(() => {
      setData({ 
        message: 'Welcome to the Mentor Project!',
        tech_stack: ['React', 'FastAPI', 'SQLAlchemy', 'PostgreSQL']
      });
    }, 1000);
  }, []);

  const handleRegistrationSuccess = () => {
    setShowRegister(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Mentor Project</h1>
      </header>
      <main className="App-content">
        {showRegister ? (
          <>
            <RegisterForm onRegistrationSuccess={handleRegistrationSuccess} />
            <button className="back-button" onClick={() => setShowRegister(false)}>
              Back to Home
            </button>
          </>
        ) : (
          <>
            <div className="welcome-container">
              <h2>{data.message}</h2>
              {data.tech_stack && (
                <div className="tech-stack">
                  <h3>Built with:</h3>
                  <ul>
                    {data.tech_stack.map((tech, index) => (
                      <li key={index}>{tech}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
            <button className="register-button" onClick={() => setShowRegister(true)}>
              Create an Account
            </button>
          </>
        )}
      </main>
    </div>
  );
}

export default App;