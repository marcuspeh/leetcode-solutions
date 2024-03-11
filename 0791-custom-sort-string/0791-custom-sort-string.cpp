class Solution {
    string mergeSort(unordered_map<char, int>& orderIndex, string s) {
        if (s.size() <= 1) {
            return s;
        }
        
        string firstHalf = s.substr(0, s.size() / 2);
        string secondHalf = s.substr(s.size() / 2);
        string sortedFirstHalf = mergeSort(orderIndex, firstHalf);
        string sortedSecondHalf = mergeSort(orderIndex, secondHalf);
        
        string result;
        int i = 0;
        int j = 0;
        while (i < sortedFirstHalf.size() && j < sortedSecondHalf.size()) {
            int index1 = orderIndex[sortedFirstHalf[i]];
            int index2 = orderIndex[sortedSecondHalf[j]];
            
            if (index1 < index2) {
                result += sortedFirstHalf[i];
                i++;
                continue;
            }
            result += sortedSecondHalf[j];
            j++;
        }
        
        if (i < sortedFirstHalf.size()) {
            result += sortedFirstHalf.substr(i);
        }
        if (j < sortedSecondHalf.size()) {
            result += sortedSecondHalf.substr(j);
        }
        return result;
    }
public:
    string customSortString(string order, string s) {
        unordered_map<char, int> orderIndex;
        for (int i = 0; i < order.size(); i++) {
            orderIndex[order[i]] = i;
        }
        
        return mergeSort(orderIndex, s);
    }
};