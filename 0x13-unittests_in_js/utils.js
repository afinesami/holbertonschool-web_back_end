const Utils = {
    isNegZero(n) {
      const num = Number(n);
      return num === 0 && 1 / num === -Infinity;
    },
    calculateNumber(type, a, b = 0) {
      let aNum = Number(a);
      let bNum = Number(b);
  
      if (Number.isNaN(aNum) || Number.isNaN(bNum))
        throw TypeError('Parameters must be numbers or able to coerce to number');
  
      aNum = Math.round(aNum);
      bNum = Math.round(bNum);
  
      let quotient;
  
      switch (type) {
        case 'SUM':
          return aNum + bNum;
        case 'SUBTRACT':
          return aNum - bNum;
        case 'DIVIDE':
          if (bNum === 0) return 'ERROR';
          quotient = aNum / bNum;
          return this.isNegZero(quotient) ? 0 : quotient;
        default:
          throw Error(
            'Invalid operation type. Valid types are "SUM", "SUBTRACT", and "DIVIDE".'
          );
      }
    }
  };
  
  module.exports = Utils;