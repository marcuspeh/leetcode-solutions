class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0;
        int i = a.size() - 1;
        int j = b.size() - 1;
        string result = "";
        
        while (i >= 0 || j >= 0 || carry) {
            int temp = 0;
            if (i >= 0 && a[i--] == '1') temp++;
            if (j >= 0 && b[j--] == '1') temp++;
            if (carry) temp++;
            
            result += '0' + temp % 2;
            carry = temp / 2;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};