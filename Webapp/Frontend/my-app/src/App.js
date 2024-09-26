import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

function App() {
  
    const [socket, setSocket] = useState(null);
    const [imageSrc, setImageSrc] = useState('');
    const [message, setMessage] = useState('');

    useEffect(() => {
      const newSocket = io('http://localhost:5002'); // Connect to Flask backend
      setSocket(newSocket);
  
      // Request frame every 100ms
      const interval = setInterval(() => {
        newSocket.emit('request_frame');
      }, 100);
  
      // Clean up connection
      return () => {
        clearInterval(interval);
        newSocket.disconnect();
      };
    }, []);
  
    useEffect(() => {
      if (socket) {
        socket.on('video_frame', (frame) => {
          setImageSrc(`data:image/jpeg;base64,${frame}`);
        });
      }
    }, [socket]);

    const handleButtonClick = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5002/api/button-click');
        const data = await response.json();
        setMessage(data.message);  // Speichert die Nachricht im State
      } catch (error) {
        console.error("Fehler beim Abrufen der API:", error);
        setMessage("Fehler beim Abrufen der API");
      }
    };
  
    return (
      <div>
        <button onClick={handleButtonClick}>Klick mich!</button>
        <h2>Video Stream</h2>
        {imageSrc ? (
          <img src={imageSrc} alt="Video Stream" style={{ width: '50%' }} />
        ) : (
          <p>Waiting for video stream...</p>
        )}
      </div>
    );

};

export default App;