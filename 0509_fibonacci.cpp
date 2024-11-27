/*
* https://leetcode.com/problems/fibonacci-number/
*/
class Solution {
public:
    int fib(int n) {
        float sqrt_5 = sqrt(5.0);
        float phi = (1 + sqrt_5) * 0.5;
        float psi = 1 - phi;
        return round((pow(phi, n) - pow(psi, n)) * (1.0/sqrt_5));
    }
};