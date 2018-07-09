#include <iostream>
#include <string>
 
using namespace std;
 
int
main(int argc, char const* argv[])
{
        string d10 = "10";      // 10進数
        string o80 = "010";     // 8進数
        string xFF = "0xFF";    // 16進数
        string FF = "FF";       // 16進数, 0xなし
        int a = std::stoi(d10); // 10進数
        int b = std::stoi(o80, nullptr, 8);     // 8進数
        int c = std::stoi(xFF, nullptr, 16);    // 16進数
        int d = std::stoi(FF, nullptr, 16);     // 16進数, 0xなし
        cout << a << endl;
        cout << b << endl;
        cout << c << endl;
        cout << d << endl;
        return 0;
}