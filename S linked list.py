#singlly linked list
class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class ll:
  def __init__(self):
    self.head=None
    self.temp=None
  def append(self,data):
    newnode=node(data)
    if self.head is None:
      self.head=newnode
      self.temp=newnode
    else:
      self.temp.next=newnode
      self.temp=newnode
  def dis(self):
    temp=self.head
    temp1=self.head
    while(temp!=None):
      while(temp==temp1):
            print(temp.data,end="")
            break
      temp=temp.next
      if temp!=None:
         print("=>",temp.data,end="")
      
      
  def max(self):
    self.temp=self.head
    maxi=0
    while self.temp:
      if maxi<self.temp.data:
        maxi=self.temp.data
      self.temp=self.temp.next
    print(maxi)
if __name__=='__main__':
  l=ll()
  while True:
    i=int(input())
    if(i<0):
      break
    l.append(i)
  l.max()
l.dis()
