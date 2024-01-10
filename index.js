const express = require('express');
const app = express();
const path = require('path');
const fs = require('fs');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));

let jsonData
fs.readFile('data.json', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
    }
    jsonData = JSON.parse(data);
});

app.get('/', (req, res) => {
    res.render('index', { data: jsonData });
});

const getMonumentById = async (id) => { 
    return jsonData[id]
}
app.get('/monument/:id', async (req, res) => {
    const id = req.params.id;
    const monument = await getMonumentById(id);

    if (monument) {
        res.render('monument-details', { monument });
    } else {
        res.status(404).send('Monument not found');
    }
});
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});