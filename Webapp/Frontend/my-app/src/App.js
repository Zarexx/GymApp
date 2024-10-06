import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import './MainPage.css'; // Korrigierter Pfad für das Styling

const App = () => {
    const [socket, setSocket] = useState(null);
    const [imageSrc, setImageSrc] = useState('');
    const [message, setMessage] = useState('');
    const [chatMessages, setChatMessages] = useState([]); // State to hold chat messages
    const [selectedExercise, setSelectedExercise] = useState(''); // State for the selected exercise

    const exercises = ['Chestpress', 'Squat', 'Deadlift', 'Bench Press']; // Add your exercises here

    useEffect(() => {
        const newSocket = io('http://localhost:5002'); // Connect to Flask backend
        setSocket(newSocket);

        // Request frame every 1ms
        const interval = setInterval(() => {
            newSocket.emit('request_frame');
            newSocket.emit('request_chat_message');
        }, 1); 

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
                        // Listen for chat messages from the backend
            socket.on('chat_message', (chatMessage) => {
                setChatMessages((prevMessages) => [...prevMessages, chatMessage]);
                console.log(chatMessages);
            });
        }
    }, [socket]);




    // Function to start the thread
    const start_thread = async () => {
        if (!selectedExercise) {
            setMessage("Bitte wähle eine Übung aus.");
        }
        try {

            const response = await fetch(`http://127.0.0.1:5002/api/thread_start/${selectedExercise}`);
            const data = await response.json();
            setMessage(data.message);  // Store the message in state
        } catch (error) {
            console.error("Fehler beim Abrufen der API:", error);
            setMessage("Fehler beim Abrufen der API");
        }
    };

    // Function to stop the thread
    const stop_thread = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5002/api/thread_stop');
            const data = await response.json();
            setMessage(data.message);  // Store the message in state

            setImageSrc('');           // Clear the video frame
            setChatMessages([]);        // Clear the chat messages
        } catch (error) {
            console.error("Fehler beim Abrufen der API:", error);
            setMessage("Fehler beim Abrufen der API");
        }
    };

    return (
        <div className="main-container">
            <div className="sidebar">
                <div className="Logo">
                    <img src="path_to_logo.png" alt="Logo" /> {/* Replace 'path_to_logo.png' with the correct image path */}
                </div>
                <div className="name-container">
                    nh süße
                </div>
                <div className="button-Trainingsplan">
                    <button className="Trainingsplan-button">STARTSEITE</button>
                </div>
                <div className="button-Placeholder">
                    <button className="Placeholder-button">TRAININGSPLAN</button>
                </div>
                <div className="button-Placeholder">
                    <button className="Placeholder-button">STATISTIK</button>
                </div>
            </div>
            <div className="content">
                <div className="exercise-header">
                    <div className="exercise-header-text">
                        {/* Dropdown Menu for Exercises */}
                        <select
                            value={selectedExercise}
                            onChange={(e) => setSelectedExercise(e.target.value)}
                            className="exercise-dropdown"
                        >
                            <option value="">Wähle eine Übung</option>
                            {exercises.map((exercise, index) => (
                                <option key={index} value={exercise}>{exercise}</option>
                            ))}
                        </select>
                    </div>
                </div>
                <div className="camera-chat-container">
                    <div className="camera-stream">
                        <div className="image-container">
                            {imageSrc ? (
                                <img src={imageSrc} alt="Video Stream" style={{ width: '100%', height: '100%' }} />
                            ) : (
                                <p>Waiting for video stream...</p>
                            )}
                        </div>
                    </div>
                    <div className="chat-error">
                        
                        {/* Render chat messages */}
                        <div>
                            <ul>
                                {chatMessages.map((msg, index) => (
                                    <li key={index}>{msg}</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="buttons">
                    <button className="start-button" onClick={start_thread}>Start</button>
                    <button className="stop-button" onClick={stop_thread}>Beenden</button>
                    <button className="trainer-button">Trainer-Holen</button>
                </div>
                {message && <p>{message}</p>} {/* Display the message */}
            </div>
        </div>
    );
};

export default App;
