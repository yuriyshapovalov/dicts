
const assets = [
    { type: "nouns", filename: 'nouns.dict'},
    { type: "verbs", filename: 'verbs.dict'},
    { type: "pronouns", filename: 'pronouns.dict'},
    { type: "adjectives", filename: 'adjectives.dict'},
    
];

const languages = [
    { name: 'arabic', path: "data/arabic" },
    { name: 'chinese', path: "data/chinese" },
    { name: 'english', path: "data/english" },
    { name: 'farsi', path: "data/farsi" },
    { name: 'french', path: "data/french" },
    { name: 'german', path: "data/german" },
    { name: 'greek', path: "data/greek" },
    { name: 'hindi', path: "data/hindi" },
    { name: 'italian', path: "data/italian" },
    { name: 'japanese', path: "data/japanese" },
    { name: 'portuguese', path: "data/portuguese" },
    { name: 'spanish', path: "data/spanish" },
    { name: 'swedish', path: "data/swedish" },
    { name: 'turkish', path: "data/turkish" },
];

module.exports = {
    assets,
    languages
};