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
    let isDuplicate = false;
    for (let j = i; j < arr.length; j++) {
      for (let k = i; k < j; k++) {
        if (arr[k] === arr[j]) {
          isDuplicate = true;
          break;
        }
      }
      if (isDuplicate) {
        break;
      }
      testNum += 1;
    }
    if (testNum > topNum) {
      topNum = testNum;
    }
  }

  return topNum;
};

console.log(lengthOfLongestSubstring(s));

//url
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
