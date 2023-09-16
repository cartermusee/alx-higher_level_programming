#!/usr/bin/node
exports.converter = function (base) {
  function Base (n) {
    return n.toString(base);
  }

  return Base;
};
