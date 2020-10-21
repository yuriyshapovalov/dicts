const fs = require('fs');
const mongoose = require('mongoose');
const config = require('./ingestion-config');
const VerbSchema = require('./models/verb');

mongoose.connect('mongodb://localhost:27017/dicts');

const Verb = mongoose.model("Verb", VerbSchema);

// import ingestion config
config.languages.map( language => {
    console.log(language.name);
    // get verbs
    config.assets.map( asset => {
        switch (asset.type) {
            case 'verb': {
                console.log(asset.filename);
            }; break;
        }
    });

    
    let verb = new Verb(parseVerb());

});

// parser functions