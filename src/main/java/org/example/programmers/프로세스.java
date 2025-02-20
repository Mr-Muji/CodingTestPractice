/*
 *
 * 배열 정렬하는 법
 * 배열 출력하는 법(스트링으로 변환)
 */


package org.example.programmers;

import java.util.Arrays;

public class 프로세스 {
    public int solution(int[] priorities, int location) {
        int answer = 0;

        //int[] arr = new int[priorities.length];
        int[] arr = Arrays.stream(priorities).sorted().toArray();
        //arr을 역순으로
        int index = priorities.length - 1;
        int count = 0;
        while (true) {
            if (priorities[count] == arr[index]) {
                count++;
                index--;
                answer++;
                if (count == priorities.length) {
                    break;
                }
            } else {
                count++;
                if (count == priorities.length) {
                    count = 0;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args){
        프로세스 s = new 프로세스();
        System.out.println(s.solution(new int[]{2, 1, 3, 2}, 2));
        System.out.println(s.solution(new int[]{1,1,9,1,1,1}, 0));
    }

}
