import 'dart:io';
import 'dart:math';
void main(){
Random random=Random();
List <int> list1=[];
List <int> list2=[];
List <int> list3=[];
for(int i=0;i<10;i++){
  list1.add(10+ random.nextInt(10));
  list2.add(10+ random.nextInt(10));
  print("ingresa dato de lista 3 $i");
  list3.add(int.parse(stdin.readLineSync()!));


}

List <int >listacon=list3+list2+list1;
double suma=0 ;
for(int i=0;i<listacon.length;i++){
   suma += listacon[i];}
print("lista 1");
print(list1);
print("lista 2");
print(list2);
print("lista 3");
print(list3);
print("lista concatenada");
print(listacon);
listacon.sort;
print("lista ordenada");
print(listacon.reversed);
print("Promedio");
print(suma/30);


}