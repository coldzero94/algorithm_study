/**
 * @param {string} s
 * @return {number}
 */

let s = "abcabcbb";
var lengthOfLongestSubstring = function (s) {
  let arr = [...s];
  let topNum = 0;

  for (let i = 0; i < arr.length; i++) {
    let testNum = 0;
    let testSet = new Set();
    for (let j = i; j < arr.length; j++) {
      if (testSet.has(arr[j])) {
        break;
      }
      testSet.add(arr[j]);
      testNum += 1;
    }
    topNum = Math.max(topNum, testNum);
  }

  return topNum;
};

console.log(lengthOfLongestSubstring(s));

//url
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
