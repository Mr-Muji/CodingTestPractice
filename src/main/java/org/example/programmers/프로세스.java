/*
 *
 * 배열 정렬하는 법
 * 배열 출력하는 법(스트링으로 변환)
 *
 * 배열 입력시 초기화!!!
 * Queue<int[]> queue2 = new LinkedList<>();
        for(int i = 0; i < priorities.length; i++){
            queue2.add(new int[]{i, priorities[i]});
        }
 *
 */


package org.example.programmers;

import java.util.*;

public class 프로세스 {
    public int solution(int[] priorities, int location) {
        int answer = 0;

        //int[] arr = new int[priorities.length];
        //int[] arr = Arrays.stream(priorities).sorted().toArray();
        //arr을 역순으로

        //priorities를 차례대로 큐에 입력
        Queue<int[]> queue2 = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++) {
            queue2.add(new int[]{i, priorities[i]});
        }
        //queue2 출력
        System.out.println("queue2 = " + queue2);

        //배열 역순 정렬
        int[] arr = new int[priorities.length];

        Arrays.sort(priorities);

        for (int i = 0; i < priorities.length; i++) {
            arr[i] = priorities[priorities.length - i - 1];
        }

        //arr을 차례대로 큐에 입력
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < arr.length; i++) {
            queue.add(arr[i]);
        }

        //queue 출력.
        System.out.println("queue = " + queue);



        int cnt = 0;
        while (!queue.isEmpty()) {
            if (answer != 0) {
                break;
            }
            int temp = queue.poll();

            while (true) {
                int[] temp2 = queue2.poll();
                if (temp == temp2[1]) {
                    cnt++;
                    if (temp2[0] == location) {
                        answer = cnt;
                    }
                    break;
                } else {
                    queue2.add(temp2);
                }
            }
        }


        return answer;
    }

    public static void main(String[] args) {
        프로세스 s = new 프로세스();
        System.out.println(s.solution(new int[]{2, 1, 3, 2}, 2));
        System.out.println(s.solution(new int[]{1, 1, 9, 1, 1, 1}, 0));
    }

}
