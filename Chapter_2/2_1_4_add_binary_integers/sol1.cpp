// Code to be added to this. Algo same as sol1.py. Refer
#include "string"
using namespace std;
class Solution
{
public:
    string addBinary(string a, string b)
    {
        string s = "";

        int carry = 0, i = a.size() - 1, j = b.size() - 1;
        int sum;
        while(i >= 0 || j >= 0)
        {
          sum=carry;
          if (i >= 0){
              sum =sum+a[i] - '0';
              i--;
          }
          if (j >= 0){
              sum =sum+b[j] - '0';
              j--;
          }

            s = char(sum % 2 + '0') + s;
            carry = sum/2;
        }
        if (carry == 1){
          s = char(carry % 2 + '0') + s;
        }

        return s;
    }
};

int main(int argc, char const *argv[]) {
  Solution obj;
  string a="100";
  string b="1";
  cout<<obj.addBinary(a,b)<<endl;
  return 0;
}
