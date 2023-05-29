#include<iostream>
#include<random>
#include<math.h>
#include<set>
using namespace std;



struct node{
  int key;
  int level;
  node **next;
};

class skipList{
  node *head;
  int maxlvl, level, size;
  double p;
public:
  skipList(float _p, int _maxlvl);
  void add(int value);
  bool search(int value);
  void erase(int value);
  void display();
};

int node_level(double p){
  random_device rd;
  int lvl = 1, num = rd();
  num = num < 0 ? -num : num;
  while((num % 100) + 1 < (100 * p)){
    lvl++;
    num = rd();
  }
  return lvl;
}

skipList::skipList(float _p, int _maxlvl){
  head = new node;
  maxlvl = _maxlvl;
  head->next = new node* [maxlvl];
  for(int i = 0; i < maxlvl; i++){
    head->next[i] = nullptr;
  }
  level = 1;
  p = _p;
}

void skipList::add(int value){
  node *newNode = new node;
  newNode->key = value;
  int lvl = node_level(p);
  lvl = lvl <= maxlvl ? lvl : maxlvl;
  newNode->level = lvl;
  if(level < lvl){
    level = lvl;
  }
  newNode->next = new node* [lvl];
  for(int i = 0; i < lvl; i++){
    node *ptr = head;
    while(ptr->next[i] != nullptr && ptr->next[i]->key < value){
      ptr = ptr->next[i];
    }
    newNode->next[i] = ptr->next[i];
    ptr->next[i] = newNode;
  }
  size++;
}


bool skipList::search(int value){
  node *heading = head;
  for(int i = level - 1;  i >= 0; i--){
    node *ptr = heading;
    while(ptr->next[i] != nullptr && ptr->next[i]->key < value){
      ptr = ptr->next[i];
    }
    if(ptr->next[i] != nullptr && ptr->next[i]->key == value){
      return true;
    }
  }
  return false;
}


void skipList::erase(int value){
  set<node *> pointers;
  int lvl = level;
  for(int i = 0; i < level; i++){
    node *ptr = head;
    while(ptr->next[i] != nullptr && ptr->next[i]->key < value){
      ptr = ptr->next[i];
    }
    while(ptr->next[i] != nullptr && ptr->next[i]->key == value){
      pointers.insert(ptr->next[i]);
      node *tmp = ptr->next[i];
      ptr->next[i] = ptr->next[i]->next[i];
      tmp->next[i] = nullptr;
    }
  }
  for(node *pointer : pointers){
    delete pointer;
    pointer = nullptr;
  }
  if(head->next[0] != nullptr){
    level = head->next[0]->level;
  }
  else{
    level = 1;
  }
  for(node *ptr = head->next[0]; ptr != nullptr; ptr = ptr->next[0]){
    if(ptr->level > level){
      level = ptr->level;
    }
  }
}


void skipList::display(){
  for(int i = 0; i < level; i++){
    for(node * ptr = head->next[i]; ptr != nullptr; ptr = ptr->next[i]){
      cout << ptr->key << " ";
    }
    cout << endl;
  }
}


int main(){
  double p;
  int maxlvl, n;
  cin >> p >> maxlvl >> n;
  skipList L(p, maxlvl);
  for(int i = 0; i < n; i++){
    int number;
    cin >> number;
    L.add(number);
  }
  L.display();
  while(true){
    string command;
    int number;
    cin >> command;
    if(command == "find"){
      cin >> number;
      if(L.search(number)){
        cout << number << " exists in List" << endl;
      }
      else{
        cout << "Not found!" << endl;
      }
    }
    else if(command == "delete"){ 
      cin >> number;
      L.erase(number);
    }
    else if(command == "display"){
      L.display();
    }
    else if(command == "exit"){
      break;
    }
  }
  return 0;

}

