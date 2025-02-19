/*
* 250219 프로그래머스 올바른 괄호 Lv2
* https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=java
*
* 젤 앞이 ')' 면 무조건 실패.
* '('의 개수만큼 그 뒤에 ')' 가 나와야 함.
* 스택으로 풀려면
* (가 나올 때마다 스택에 push 해주고, )가 나올때마다 한 쌍이 되므로 pop 해준다.
* ')' 가 나왔는데 스택이 비어있으면 ')'가 더 많다는 뜻이므로 실패.
* 다 끝났을 때 스택이 딱 비어 있어야 true. 안 비어 있으면 '('가 더 많다는 뜻이므로 실패.
*
* String을 array로 다루는 법 익히기
* String의 특정 부분을 빼내는 법?
* s.substring(x, x)
* s.charAt()
*
* */

package org.example.programmers;

import java.util.*;

public class 올바른괄호 {
    boolean solution(String s) {
        boolean answer = true;

        //String의 첫 번째만 빼내는 법은?
        //s.substring(x, x) = string을 반환
        //s.charAt(0) : char 을 반환
        //s.charAt(0) == '('  *** "(" 하면 안됨!!! '(' 해야 char 형이 됨.
        Stack<Character> stack = new Stack<>();
        char[] arr = s.toCharArray();
        if(s.charAt(0) == ')'){
            answer = false;
        }else{
            for(char c : arr){
                if(c == '('){
                    stack.push(c);
                }else if(stack.isEmpty()){
                    answer = false;
                    break;
                }else{
                    stack.pop();
                }
            }
            if(!stack.isEmpty()){
                answer = false;
            }
        }

        return answer;
    }

    //개선 코드
    boolean solution2(String s) {
        // 길이가 홀수면 무조건 실패
        if (s.length() % 2 != 0) return false;

        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count++;
            } else {
                if (count == 0) {
                    return false;  // 닫는 괄호가 더 많아진 경우
                }
                count--;
            }
        }
        return count == 0;
    }

    public static void main(String[] args){
        올바른괄호 sol = new 올바른괄호();
        System.out.println(sol.solution("()()"));
        System.out.println(sol.solution("(())()"));
        System.out.println(sol.solution(")()("));
        System.out.println(sol.solution("(()("));
    }
}

