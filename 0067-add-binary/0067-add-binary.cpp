class Solution {
public:
    pair<string, string> add(char a, char b, string carry) {
        int count = 0;
        
        char arr[] = {a, b};
        for (char s: arr) {
            if (s == '1') {
                count++;
            }
        }
        
        if (carry == "1") {
            count++;
        }
        return {count % 2 ? "1" : "0", count > 1 ? "1" : "0"};
    }
    
    string addBinary(string a, string b) {
        string result = "";
        
        int length = min(a.length(), b.length());
        string carry = "0";
        int i;
        for (i = 0; i < length; i++) {
            pair<string, string> temp = add(a[a.length() - 1 - i], b[b.length() - 1 - i], carry);
            result = temp.first + result;
            carry = temp.second;
        }
        
        for (; i < a.length(); i++) {
            pair<string, string> temp = add(a[a.length() - 1 - i], '0', carry);
            result = temp.first + result;
            carry = temp.second;
        }
        
        for (; i < b.length(); i++) {
            pair<string, string> temp = add('0', b[b.length() - 1 - i], carry);
            result = temp.first + result;
            carry = temp.second;
        }
        if (carry == "1") {
            result = carry + result;
        }
        
        return result;
    }
};