using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> seen_str;
        for (string& str : strs){
            string unsort = str;
            std::sort(str.begin(), str.end());
            seen_str[str].push_back(unsort);
        }
        vector<vector<string>> values;
        for (auto& p : seen_str){
            values.push_back(p.second);
        }
        return values;
    }
};
