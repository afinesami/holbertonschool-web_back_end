export default function appendToEachArrayValue(array, appendString) {
  const array2 = array;
  for (const value of array) {
    const idx = array.indexOf(value);
    array2[idx] = appendString + value;
  }

  return array2;
}
