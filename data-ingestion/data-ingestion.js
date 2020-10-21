const fs = require('fs');
const mongoose = require('mongoose');
const config = require('./ingestion-config');

// import ingestion config
config.languages.map(language => {
    console.log(language.name);
});

// parser functions