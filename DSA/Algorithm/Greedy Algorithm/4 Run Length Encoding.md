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

void runlengthencode(const char* input, char* output){
    int n = strlen(input);
    int visited[256] = {0};  
    int k = 0;

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

        output[k++] = ch;

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
