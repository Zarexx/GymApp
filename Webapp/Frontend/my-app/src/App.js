import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

const socket = io.connect("http://127.0.0.1:5001");

function App() {
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    socket.emit('chat_message', message);
    setMessage('');
  };

  return (
    <div>
      <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} />
      <button onClick={handleSubmit}>Senden</button>   

    </div>
  );
}

export default App;