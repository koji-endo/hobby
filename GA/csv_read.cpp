//g++ -std=c++11 -o csv_read_win csv_read.cpp 2> error.txt
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<string> split(string& input, char delimiter)
{
    istringstream stream(input);
    string field;
    vector<string> result;
    while (getline(stream, field, delimiter)) {
        result.push_back(field);
    }
    return result;
}
vector<vector<string>> csv_read(string filename){
    ifstream ifs(filename);
    string line;
    vector<vector<string>> returnee;
    while (getline(ifs, line)) {
        if(line[0]=='#'){
            cout<< "hit" <<endl;
        }else{
            vector<string> strvec = split(line, ' ');
            returnee.push_back(strvec);
        }
    }
    return returnee;
}
void print_vector(vector<vector<string>> lala){
    for_each(begin(lala), end(lala), 
        [&](vector<string> la){ 
            for_each(begin(la), end(la), 
                [&](string i) {
                    cout<<i<<" ";
                }
            );
            cout<<endl;
        }
    );
}

int main(){
    vector<vector<string>> lala;
    lala=csv_read("connect_sei0530.txt");
    print_vector(lala);
} 