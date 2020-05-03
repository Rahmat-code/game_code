//Tower of Honoi code
#include<iostream>
using namespace std;

void honoi_tower(int n, char from_rod, char to_rod, char aux_rod){
    if(n==1){
        cout<<"Move disk 1 from rod "<<from_rod<<" to rod "<<to_rod<<endl;
        return;
    }
    honoi_tower( n-1, from_rod, aux_rod, to_rod);
    cout<<"Move disk "<<n<<" from rod "<<from_rod<<" to rod "<<to_rod<<endl;
    honoi_tower(n-1, aux_rod, to_rod, from_rod);
}

int main(){
    int n;
    cout<<"Enter the number of disks : "<<endl;
    cin>>n;
    // A is the source , B is the destination and C is the temporary rod
    honoi_tower(n,'A', 'C', 'B');//A B and C are the name of rod
    return 0;
}
