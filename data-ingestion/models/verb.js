const mongoose = require('mongoose');

const VerbSchema = mongoose.Schema("Verb", {
    id: String,
    word: String,
    description: String,
    topic: String,
    tags: [String],
    phonetic: String
});

module.exports = VerbSchema;