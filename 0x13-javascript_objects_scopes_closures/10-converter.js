#!/usr/bin/node
exports.converter = function (base) {
  function Base (n) {
    if (n < base) {
      return n.toString(base);
    } else {
      return Base(Math.floor(n / base)) + (n % base).toString();
    }
  }

  return Base;
};
