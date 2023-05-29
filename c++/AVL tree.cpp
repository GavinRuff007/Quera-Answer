#include<bits/stdc++.h>
//salam man project haye (AVL tree)&(LU decomposition) ro ba aghaye erfan shahabi dorost kardam!!!
using namespace std;
struct Node
{
public:
int k;
Node *lft;
Node *rght;
int h;
};
Node * minval(Node* node)
{
Node* cur = node;
while (cur->lft != NULL)
cur = cur->lft;

return cur;
}
int max(int a, int b);
int h(Node *N)
{
if (N == NULL)
return 0;
return N->h;
}
int max(int a, int b)
{
return (a > b)? a : b;
}
Node* nodenew(int k)
{
Node* node = new Node();
node->k = k;
node->lft = NULL;
node->rght = NULL;
node->h = 1;
return(node);
}
Node *rghtRotate(Node *y)
{
Node *x = y->lft;
Node *T2 = x->rght;
x->rght = y;
y->lft = T2;
y->h = max(h(y->lft),
h(y->rght)) + 1;
x->h = max(h(x->lft),
h(x->rght)) + 1;
return x;
}
Node *lftRotate(Node *x)
{
Node *y = x->rght;
Node *T2 = y->lft;
y->lft = x;
x->rght = T2;
x->h = max(h(x->lft),
h(x->rght)) + 1;
y->h = max(h(y->lft),
h(y->rght)) + 1;
return y;
}
int getBalance(Node *N)
{
if (N == NULL)
return 0;
return h(N->lft) -
h(N->rght);
}

Node* insert(Node* node, int k)
{
if (node == NULL)
return(nodenew(k));

if (k < node->k)
node->lft = insert(node->lft, k);
else if (k > node->k)
node->rght = insert(node->rght, k);
else
return node;
node->h = 1 + max(h(node->lft),
h(node->rght));
int balance = getBalance(node);
if (balance > 1 && k < node->lft->k)
return rghtRotate(node);
if (balance < -1 && k > node->rght->k)
return lftRotate(node);
if (balance > 1 && k > node->lft->k)
{
node->lft = lftRotate(node->lft);
return rghtRotate(node);
}
if (balance < -1 && k < node->rght->k)
{
node->rght = rghtRotate(node->rght);
return lftRotate(node);
}
return node;
}
void preorder(Node *rishe)
{
if(rishe != NULL)
{
cout << rishe->k << " ";
preorder(rishe->lft);
preorder(rishe->rght);
}
}
Node* del(Node* rishe, int k)
{
if (rishe == NULL)
return rishe;
if ( k < rishe->k )
rishe->lft = del(rishe->lft, k);

else if( k > rishe->k )
rishe->rght = del(rishe->rght, k);
else
{
if( (rishe->lft == NULL) ||
(rishe->rght == NULL) )
{
Node *temp = rishe->lft ?
rishe->lft :
rishe->rght;
if (temp == NULL)
{
temp = rishe;
rishe = NULL;
}
else
*rishe = *temp;
free(temp);
}
else
{
Node* temp = minval(rishe->rght);
rishe->k = temp->k;
rishe->rght = del(rishe->rght,
temp->k);
}
}
if (rishe == NULL)
return rishe;
rishe->h = 1 + max(h(rishe->lft),
h(rishe->rght));
int balance = getBalance(rishe);
if (balance > 1 &&
getBalance(rishe->lft) >= 0)
return rghtRotate(rishe);
if (balance > 1 &&
getBalance(rishe->lft) < 0)
{
rishe->lft = lftRotate(rishe->lft);
return rghtRotate(rishe);
}
if (balance < -1 &&
getBalance(rishe->rght) <= 0)
return lftRotate(rishe);
if (balance < -1 &&
getBalance(rishe->rght) > 0)
{
rishe->rght = rghtRotate(rishe->rght);
return lftRotate(rishe);
}

return rishe;
}

int main()
{
Node *rishe = NULL;
cout<<"baraye payane insert khorooj ra vared konid"<<endl<<"baraye add insert"<<endl<<"baraye hazf delete"<<endl<<"baraye namayesh search avl"<<endl;

string c;
while(c!="khorooj")
{

cin>>c;
if(c=="insert")
{

int p;
cin >>p;
rishe = insert(rishe, p);

}
if(c=="delete")
{
int p;
cin >>p;
rishe = del(rishe, p);

}
if(c=="search")
{
int p;
cin >>p;
rishe = del(rishe, p);
preorder(rishe);
}
}


return 0;
}

