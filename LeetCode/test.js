/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let str = x.toString();
    let len = str.length;
    let mid = Math.floor(len/2);
    for(let i=0;i<mid;i++){
        if(str[i]!==str[len-1-i]){
            return false;
        }
    }
    return true;
};