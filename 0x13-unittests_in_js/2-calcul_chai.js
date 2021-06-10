function calculateNumber(type, a, b) {
    const n1 = Math.round(a);
    const n2 = Math.round(b);
  
    if (type === 'SUBTRACT') {
      return n1 - n2;
    }
  
    if (type === 'DIVIDE') {
      if (n2 === 0) {
        return 'Error';
      }
      return n1 / n2;
    }
  
    return n1 + n2;
  }
  
  module.exports = calculateNumber;