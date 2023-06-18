import sys
from collections import defaultdict
from collections import deque

sys.stdin = open('./2_swap/input.txt','r')
sys.stdout = open('./2_swap/output.txt','w')

class Solution:
    def __init__(self, s:str,t:str) -> None:
        self.s= s
        self.t=t
        self.__odd_index = []
        self.__even_index = []
    

    def solve(self)->str:
        # self.print_state()
        self.s_odd=deque(sorted([self.s[i] for i in range(len(self.s)) if i%2==1]))
        self.s_even=deque(sorted([self.s[i] for i in range(len(self.s)) if i%2==0]))
        self.t_odd=deque(sorted([self.t[i] for i in range(len(self.t)) if i%2==1]))
        self.t_even=deque(sorted([self.t[i] for i in range(len(self.t)) if i%2==0]))
        
        for i in range(len(s)):
            if i%2==1:
                s_el= self.s_odd.popleft() if len(self.s_odd) >0 else ''
                t_el= self.t_odd.popleft() if len(self.t_odd) >0 else ''
                if  s_el == t_el:
                    continue
                return 'No'
            if i%2==0:
                s_el= self.s_even.popleft() if len(self.s_even) >0 else ''
                t_el= self.t_even.popleft() if len(self.t_even) >0 else ''
                if  s_el == t_el:
                    continue
                return 'No'
        
        return 'Yes'

    # def pre_process(self):
    #     for i in range(len(self.s)):
    #         if i%2==0:
    #             self.__even_index.append(self.t[i])
    #         else:
    #             self.__odd_index.append(self.t[i])

    def print_state(self):
        print(f"even indexes:{self.__even_index}")
        print(f"odd indexes:{self.__odd_index}")
        
    
    
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    s = input().strip()
    t = input().strip()
    sol= Solution(s,t)
    print(sol.solve())
    # sol.print_state()

