import React, { useEffect, useRef } from 'react';
import io from 'socket.io-client';

function App() {
    const videoRef = useRef(null);
    const socket = io("http://127.0.0.1:5002");

    useEffect(() => {
        socket.on('request_frames', (data) => {
          const img = new Image();
          img.onload = () => {
            videoRef.current.src = img.src;
          };
          img.src = `data:image/jpeg;base64,${data}`;
        });
      }, []);
    
      return (
        <video ref={videoRef} autoPlay />
      );
}

export default App;