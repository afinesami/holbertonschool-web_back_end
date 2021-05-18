const cleanSet = (set, string) => {
  if (!string || !string.length) return '';
  let value = '';
  for (const el of set) {
    if (el && el.startsWith(string)) {
      value += value.length === 0 ? el.replace(string, '') : el.replace(string, '-');
    }
  }
  return value;
};

export default cleanSet;
