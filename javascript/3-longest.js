/**
 * @param {string} s
 * @return {number}
 */

let s = "dvdf";
var lengthOfLongestSubstring = function (s) {
  let arr = [...s];
  let topArr = [];
  let testArr = [];
  let testMode = false;
  for (let i = 0; i < arr.length; i++) {
    if (testMode === true) {
      if (topArr[0] !== arr[i]) {
        for (let j = 1; j < topArr.length; j++) {
          testArr.push(topArr[j]);
        }
        console.log(testArr);
      }
      if (
        (compareArr(topArr, testArr) === "stay" ||
          compareArr(topArr, testArr) === "same") &&
        checkArr(testArr, arr[i]) === false
      ) {
        testArr.push(arr[i]);
      } else if (
        (compareArr(topArr, testArr) === "stay" ||
          compareArr(topArr, testArr) === "same") &&
        checkArr(testArr, arr[i]) === true
      ) {
        // 초기화
        testArr = [];
        testMode = false;
      } else if (
        compareArr(topArr, testArr) === "change" &&
        checkArr(testArr, arr[i]) === false
      ) {
        testArr.push(arr[i]);
      } else if (
        compareArr(topArr, testArr) === "change" &&
        checkArr(testArr, arr[i]) === true
      ) {
        topArr = testArr;
        testArr = [];
        testMode = false;
      }
    } else {
      if (checkArr(topArr, arr[i]) === false) {
        topArr.push(arr[i]);
      } else if (checkArr(topArr, arr[i]) === true) {
        testArr.push(arr[i]);
        testMode = true;
      }
    }
  }
  console.log(`탑||${topArr}`);
  console.log(`테스트||${testArr}`);
  return finalCheckArr(topArr, testArr);
  // console.log(topArr);
  // return topArr.length;
};

console.log(lengthOfLongestSubstring(s));

function checkArr(checkArr, checkStr) {
  if (checkArr.includes(checkStr) === true) {
    return true;
  } else {
    return false;
  }
}

function compareArr(originArr, newArr) {
  const originLength = originArr.length;
  const newLength = newArr.length;
  if (originLength > newLength) {
    return "stay";
  } else if (originLength === newLength) {
    return "same";
  } else if (originLength < newLength) {
    return "change";
  }
}

function finalCheckArr(topArr, testArr) {
  const originLength = topArr.length;
  const testLength = testArr.length;
  if (originLength > testLength) {
  } else {
    topArr = testArr;
  }
  return topArr.length;
}
