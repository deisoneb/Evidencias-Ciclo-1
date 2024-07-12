// src/js/server.js
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const path = require('path');
const { exec } = require('child_process');

const app = express();
const PORT = 3000;

// Serve static files from the src directory
app.use(express.static(path.join(__dirname, '../')));

// Proxy API requests to the Flask backend
app.use('/save_drawing', createProxyMiddleware({ 
    target: 'http://localhost:5000', 
    changeOrigin: true 
}));

// Start the Express server
app.listen(PORT, () => {
    console.log(`Frontend server running on http://localhost:${PORT}`);
});

// Start the Python backend
exec('python3 src/python/server.py', (err, stdout, stderr) => {
    if (err) {
        console.error(`Error al ejecutar el servidor Python: ${err}`);
        return;
    }
    console.log(`Servidor Python iniciado en http://localhost:5000`);
});

// Catch-all route to serve index.html for any unmatched routes
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../index.html'));
});