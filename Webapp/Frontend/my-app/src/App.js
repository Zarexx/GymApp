import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

const socket = io.connect("http://127.0.0.1:5001");

function App() {
 
  async function handleSubmit() {
    try {
      const response = await fetch('http://127.0.0.1:5002/init_ui/testUser');
      const jsonData = await response.json();
      console.log(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }

  
  async function threadStart() {
    try {
      const response = await fetch('http://127.0.0.1:5002/req_thread');
      const jsonData = await response.json();
      console.log(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }


  return (
    <div>
        <button onClick={handleSubmit}>UI daten</button> 
  
        <button onClick={threadStart}>thread starten</button> 
    </div>

   
  );
}

export default App;