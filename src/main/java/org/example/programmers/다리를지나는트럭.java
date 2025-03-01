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
        int time = 0;
        int currentWeight = 0;

        Queue<Integer> waitingTrucks = new LinkedList<>(); // 대기 중인 트럭
        Queue<Integer> bridgeTrucks = new LinkedList<>(); // 다리 위의 트럭
        Queue<Integer> timeOnBridge = new LinkedList<>(); // 각 트럭이 다리에 올라간 시간

        // 대기열에 트럭 추가
        for (int truckWeight : truck_weights) {
            waitingTrucks.add(truckWeight);
        }

        // 다리는 초기에 비어있음 (0으로 초기화)
        for (int i = 0; i < bridge_length; i++) {
            bridgeTrucks.add(0);
        }

        // 모든 트럭이 다리를 건널 때까지 반복
        while (!bridgeTrucks.isEmpty()) {
            time++; // 시간 증가

            // 다리의 맨 앞 트럭이 나감
            currentWeight -= bridgeTrucks.poll();

            // 대기 중인 트럭이 있고 다리에 더 올릴 수 있는 경우
            if (!waitingTrucks.isEmpty() && currentWeight + waitingTrucks.peek() <= weight) {
                int newTruck = waitingTrucks.poll();
                bridgeTrucks.add(newTruck);
                currentWeight += newTruck;
            } else {
                // 새 트럭을 올릴 수 없으면 0 추가 (빈 공간)
                bridgeTrucks.add(0);
            }

            // 모든 대기 트럭이 다리에 올라갔고, 다리 위에 트럭이 없으면 종료
            if (waitingTrucks.isEmpty() && currentWeight == 0) {
                break;
            }
        }

        return time;
    }

    public static void main(String[] args) {
        다리를지나는트럭 s = new 다리를지나는트럭();
        System.out.println(s.solution(2, 10, new int[]{7, 4, 5, 6}));
        System.out.println(s.solution(100, 100, new int[]{10}));
        System.out.println(s.solution(100, 100, new int[]{10, 10, 10, 10, 10, 10, 10, 10, 10, 10}));
    }

}
