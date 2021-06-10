module.exports = function calculateNumber(a, b = 0) {
  const aNum = Number(a);
  const bNum = Number(b);
  
  if (Number.isNaN(aNum) || Number.isNaN(bNum))
    throw TypeError('Parameters must be numbers');
  
    return Math.round(aNum) + Math.round(bNum);
  };