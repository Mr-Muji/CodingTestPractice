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

    public static void main(String[] args) {
        다리를지나는트럭 s = new 다리를지나는트럭();
        System.out.println(s.solution(2, 10, new int[]{7, 4, 5, 6}));
        System.out.println(s.solution(100, 100, new int[]{10}));
        System.out.println(s.solution(100, 100, new int[]{10, 10, 10, 10, 10, 10, 10, 10, 10, 10}));
    }

}
