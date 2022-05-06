const express = require('express');
const bodyParser = require('body-parser');

const bookController = require('./controller/bookController');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

app.use('/book', bookController);

app.listen(PORT, () => console.log(`Ouvindo na porta ${PORT}`));