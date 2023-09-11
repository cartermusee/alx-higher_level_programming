#!usr/bin/node
const executeX = (x, theFunction) => {
        for (let i = 0; i < x; i++){
                theFunction();
        }
};
module.exports = executeX;
