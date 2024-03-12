#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  for (let idx = list.length - 1; idx >= 0; idx--) {
    reverseList.push(list[idx]);
  }
  return reverseList;
};
