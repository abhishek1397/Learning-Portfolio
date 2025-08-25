//insertion
#include <iostream>

using namespace std;

int main()
{

int num[10]={5,15,22,1,-15,24};
int size = 6;
//transversal

cout<<"Initial array: ";
for (int i=0;i<size;i++){
cout<<num[i]<<" ";
}
cout<<endl;



int pos =3; //insert at index 3
int value=99;

// shift elements to right

for (int i=size;i>pos;i--){
num[i]=num[i-1];
}

num[pos]=value;
size++;

cout<<"after insertion of " << value<<" at position "<< pos<<": ";
for (int i=0;i<size;i++){
cout<<num[i]<<" ";
}

cout<<endl;
}
-------------------------------------------------------------------------------------------
//deletion

#include <iostream>
using namespace std;

int main() {
	int num[10]={5,15,22,1,-15,24};
	int size = 6;

//transversal
		cout<<"Initial array: ";
		for (int i=0;i<size;i++){
			cout<<num[i]<<" ";
	}
		cout<<endl;

	int pos =2; //delete at index 3

// shift elements to right

	for (int i=pos;i<size;i++){
		num[i]=num[i+1];
	}
	size--;

	cout<<"after deletion of  at position "<< pos<<": ";
	for (int i=0;i<size;i++){
		cout<<num[i]<<" ";
		}

	cout<<endl;
}

-----------------------------------------
 finding biggest and smallest element in array using loops:
 
#include <iostream>
using namespace std;

int main(){
int num[]={5,15,22,1,-15,24};
int size=6;

int smallest = INT_MAX;

for(int i=0;i<size;i++){
    if(num[i]<smallest){
        smallest=num[i];
    }}

cout<<"smallest= "<<smallest<<endl;
return 0;

}
