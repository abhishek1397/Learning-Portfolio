# Run length Encoding

```cpp
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

void runlengthencode(const char* input, char* output){
    int n = strlen(input);
    int k = 0;

    for(int i = 0; i < n; i++){
        int count = 1;

        while(i < n - 1 && input[i] == input[i + 1]){
            count++;
            i++;
        }

        output[k++] = input[i];

        char countstr[10];
        sprintf(countstr, "%d", count);

        for(int j = 0; countstr[j] != '\0'; j++){
            output[k++] = countstr[j];
        }
    }

    output[k] = '\0';
}

int main(){
    char input[100];
    char output[200];

    cout << "Enter a string to encode: ";
    cin.getline(input,100);

    runlengthencode(input, output);

    cout << "Run-Length Encoded string: " << output << endl;

    return 0;
}
```

## Updated Code:

```cpp
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

string runlengthencode(const string& input){
    int n = input.length();
    int visited[256] = {0};
    string output = "";

    for(int i = 0; i < n; i++){
        
        char ch = input[i];

        if(visited[(unsigned char)ch] == 1)
            continue;

        int count = 0;
        for(int j = 0; j < n; j++){
            if(input[j] == ch){
                count++;
            }
        }

        visited[(unsigned char)ch] = 1;

        output += ch;

        char countstr[10];
        sprintf(countstr, "%d", count);

        for(int j = 0; countstr[j] != '\0'; j++){
            output += countstr[j];
        }
    }

    return output;
}

int main(){
    string input;

    cout << "Enter a string to encode: ";
    getline(cin, input);

    string encoded = runlengthencode(input);

    cout << "Run-Length Encoded string: " << encoded << endl;

    return 0;
}

```
