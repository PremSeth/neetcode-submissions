class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            auto it = seen.find(target- nums[i]);
            if (it != seen.end()){
                return std::vector {it->second, i};
            }
            seen[nums[i]] = i;
        }         
    }
};
