#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <iostream>

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
    each(begin(lala), end(lala), [&](vector<string> la){ each(begin(la), end(la), [&](string i) {
cout<<i<<endl;
}
}
}

int main(){
    vector<vector<string>> lala;
    lala=csv_read("connect.txt");
    print_vector(lala);
} 