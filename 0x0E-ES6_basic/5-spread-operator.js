const concatArrays = (array1, array2, string) => [].concat(...array1, ...array2, ...string);

module.exports = concatArrays;
