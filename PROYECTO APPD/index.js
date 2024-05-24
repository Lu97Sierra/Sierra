const express = require('express');
const app = express();
const path = require('path');

const libraryRoutes = require('./routes/library.js');
const mangasRoutes = require('./routes/mangas.js');
const usersRoutes = require('./routes/users.js');
const bodyParser = require("body-parser");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use('/api', libraryRoutes);
app.use('/api', mangasRoutes);
app.use('/api', usersRoutes);

app.use(express.static('public'));
app.use(express.static(path.join(__dirname, 'public')));

// Ruta para servir el archivo HTML
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'html', 'index.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port: ${PORT}`));