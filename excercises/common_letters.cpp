#include <iostream>
#include <vector>

using namespace std;

void unique_chars(char str[], char unique[], int &unique_size) {
    unique_size = 0;
    for (int i = 0; str[i] != '\0'; i++){
        bool exists = false;
        for (int j = 0; j < unique_size; j++){
            if (unique[j] == str[i]){
                exists = true;
                break;
            }
            
        }

        if (exists == false){
            unique[unique_size] = str[i];
            unique_size++;
        }
        
        
    }

    
}

void common_letters(char str1[], char str2[], char common[], int &common_size) {
    char unique1[100], unique2[100]; // Tablice przechowujące unikalne znaki
    int size1, size2;

    unique_chars(str1, unique1, size1);
    unique_chars(str2, unique2, size2);

    common_size = 0;
    for (int i = 0; i < size1; i++) {
        for (int j = 0; j < size2; j++) {
            if (unique1[i] == unique2[j]) {
                common[common_size] = unique1[i]; // Dodajemy do tablicy wspólnych liter
                common_size++;
                break;
            }
        }
    }
}

int main() {
    char str1[100], str2[100];
    char common[100];
    int common_size;

    cout << "Enter the first string: ";
    cin >> str1;
    cout << "Enter the second string: ";
    cin >> str2;

    common_letters(str1, str2, common, common_size);

    cout << "Common letters: ";
    for (int i = 0; i < common_size; i++) {
        cout << common[i] << " ";
    }
    cout << endl;

    return 0;
}