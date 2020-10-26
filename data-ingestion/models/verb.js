const mongoose = require('mongoose');

const VerbSchema = new mongoose.Schema({
    id: String,
    word: String,
    description: String,
    topic: String,
    phonetic: String
});

module.exports = VerbSchema;