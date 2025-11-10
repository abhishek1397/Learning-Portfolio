# Run length Encoding

```cpp
Codeshare logo
 ShareSign UpLog In
1
run length coding
2
​
3
#include <iostream>
4
#include <cstring>
5
using namespace std;
6
​
7
void runlengthencode(const char* input, char* output){
8
  int n = strlen(input);
9
  int k=0;
10
  for(int i=0;i<n;i++){
11
    int count =1;
12
    while(i<n-1 && input[i]  == input[i+1]){
13
      count++;
14
      i++;
15
    }
16
    
17
    output[k++]=input[i];
18
    char countstr[10];
19
    sprintf(countstr, "%d", count);
20
    for(int j=0;countstr[j]!='\0';j++){
21
      output[k++] = countstr[j];
22
    }
23
  }
24
  output[k] ='\0';
25
    
26
}
27
​
28
int main(){
29
  char input[100];
30
  char output[200];
31
  
32
  cout<<"Enter a string to encode: ";
33
  cin>>input;
34
  runlengthencode(input,output);
35
  cout<<"Run-Length Encoded string: "<<output<<endl;
36
  return 0;
37
}





px
Hide Ads


```
