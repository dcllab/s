#include <iostream>
using namespace std;
string encrypt(string s, int key) {
    string cipher;
    for(int i=0; s[i]; i++) {
        char c = s[i] - 'a';
        c += key;
        c %= 26;
        c += 'a';
        cipher.push_back(c);
    }
    return cipher;
}
string decrypt(string s, int key) {
    return encrypt(s, (26-key));
}
int main() {
    string s;
    int key;
    cout<<"Enter message - ";
    cin>>s;
    cout<<"Enter a key - ";
    cin>>key;
    string cipher = encrypt(s, key);
    cout<<"Cipered message - "<<cipher<<endl;
    string original = decrypt(cipher, key);
    cout<<"Original message - "<<original<<endl<<endl;
    return 0;
}
