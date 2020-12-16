/*
See Below for original Problem:
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Algorithm
'OnePassHash' = O(n)
- Use the Map<> type. Utlize the map functions:
    .has to check if value in map
    .set to add to map
    .get to retreive value during return

Additional Notes:
- must utlize the ! non-null assertion operator to not raise intellisence error during map retrieval of value

*/

function twoSum(nums: number[], target: number): number[] {

    // Map var to store <ith number, index of number>
    let myMap = new Map<number, number>();
    let result: number[] = [];

    // loop through end of the array
    for (let i=0; i<= nums.length; i++) {
        // determine compliment of the ith number
        var complimentNumber = target - nums[i];
     
        // So long as a postive number
        if (complimentNumber>0) {

            // IF compliment to maket targer Already in the map
            if (myMap.has(complimentNumber)) {

                result = [i, myMap.get(complimentNumber)!]; // note had to use ! (non-null assertion op)
                return result;
            }

            // Not in had, add to the hash
            else {

                myMap.set(nums[i], i);

            }
        }
    }

    return [];

};

var myVar = twoSum([2,7,11,15], 9);
console.log(myVar);
