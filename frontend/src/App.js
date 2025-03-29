import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState({ message: '' });
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // This would fetch data from your backend API when available
    // For now, we'll simulate an API response
    setTimeout(() => {
      setData({ message: 'Welcome to Mentor Project!' });
      setIsLoading(false);
    }, 1000);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Mentor Project</h1>
        <div className="App-content">
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <div>
              <p>{data.message}</p>
              <div className="tech-stack">
                <h2>Our Tech Stack</h2>
                <ul>
                  <li>Frontend: React</li>
                  <li>Backend: Python FastAPI</li>
                  <li>Database: PostgreSQL</li>
                  <li>Infrastructure: Docker/Kubernetes</li>
                </ul>
              </div>
            </div>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;