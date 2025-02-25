/*
* 프로그래머스 - 다리를 지나는 트럭
*
*
*
* */

package org.example.programmers;

import java.util.*;

public class 다리를지나는트럭 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;

        Queue<Integer> truck_queue = new LinkedList<>();
        for (int i : truck_weights) {
            truck_queue.add(i);
        }

        Queue<Integer> bridge_queue = new LinkedList<>();

        for (int i = 0; i < bridge_length; i++) {
            bridge_queue.add(0);
        }
        int current_weight = 0;

        while (!truck_queue.isEmpty()) {
            int done = bridge_queue.poll();
            answer++;
            current_weight -= done;
        }

        return answer;
    }

    public int solution2(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int current_weight = 0;
        Queue<Integer> truck_queue = new LinkedList<>();
        Queue<Integer> bridge_queue = new LinkedList<>();

        for (int truck : truck_weights) {
            truck_queue.add(truck);
        }

        // 다리 초기화 (비어있는 상태)
        for (int i = 0; i < bridge_length; i++) {
            bridge_queue.add(0);
        }

        while (!truck_queue.isEmpty() || current_weight > 0) {
            // 다리에서 트럭 내보내기
            current_weight -= bridge_queue.poll();
            answer++;

            // 다리에 새로운 트럭 올릴 수 있는지 확인
            if (!truck_queue.isEmpty()) {
                if (current_weight + truck_queue.peek() <= weight) {
                    int truck = truck_queue.poll();
                    bridge_queue.add(truck);
                    current_weight += truck;
                } else {
                    bridge_queue.add(0); // 대기 상태 (다리 길이 유지)
                }
            }
        }

        return answer;
    }


    public static void main(String[] args) {
        다리를지나는트럭 s = new 다리를지나는트럭();
        System.out.println(s.solution(2, 10, new int[]{7, 4, 5, 6}));
        System.out.println(s.solution(100, 100, new int[]{10}));
        System.out.println(s.solution(100, 100, new int[]{10, 10, 10, 10, 10, 10, 10, 10, 10, 10}));
    }

}
