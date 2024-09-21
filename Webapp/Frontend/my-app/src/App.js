import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

const socket = io.connect("http://127.0.0.1:5001");

function App() {
  /*const [data, setData] = useState(null);

  const fetchData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/init_ui');

      const jsonData = await response.json();
      setData(jsonData);   

      console.log('Response data:', jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };*/

  socket.on('connect', () => {
    console.log('Verbunden mit dem Server');
  });

  const handleSendMessage = () => {
    socket.emit('test', 'Hello from React!');
    console.log('Sent message')
  };

 
    

  return (
    /*<div>
      <button onClick={fetchData}>Starte die Webapp</button>
      {data && <p>Die Daten: {JSON.stringify(data)}</p>}
    </div>*/

    <div>
        <button onClick={handleSendMessage}>Send Message</button>
    </div>
  );
}

export default App;