package org.example.programmers;

import java.io.*;
import java.util.*;

public class 붕대감기 {
    public int solution(int[] bandage,
                        int health,
                        int[][] attacks) {

        int answer = 0;

        int attacks_check = 0;

        int full_time = attacks[attacks.length - 1][0];
        System.out.println("full_time = " + full_time);

        int full_health = health;

        int success_count = 0;

        for (int time = 1; time <= full_time; time++) {

            if (time == attacks[attacks_check][0]) { //공격 체크
                System.out.println("공격 받음");
                health -= attacks[attacks_check][1];

                success_count = 0;  // 성공 카운트 초기화

                attacks_check++;

                if (health <= 0) {    //체력이 0이 되거나 그 이하가 되었다면 끝
                    health = -1;
                    break;
                }

            } else {    //공격받지 않았다면
                health += bandage[1];
                if (health > full_health) {   //풀 체력을 넘을 수 없다
                    health = full_health;
                }
                success_count++;
            }

            //연속 성공 시 추가 회복
            if (success_count == bandage[0]) {
                health += bandage[2];
                success_count = 0;  //연속 성공 초기화
                if (health > full_health) {   //풀 체력을 넘을 수 없다
                    health = full_health;
                }
            }

            System.out.println("------------------");
            System.out.println("시간 = " + time);
            System.out.println("현재 체력 = " + health);
            System.out.println("연속 성공 = " + success_count);
        }

        answer = health;


        return answer;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        붕대감기 s = new 붕대감기();

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

//        int[] bandage = {5, 1, 5};
//        int health = 30;
//        int[][] attacks = {{2, 10}, {9, 15}, {10, 5}, {11, 5}};

//        int[] bandage = {3, 2, 7};
//        int health = 20;
//        int[][] attacks = {{1, 15}, {5, 16}, {8, 6}};

        //[1, 1, 1]	5	[[1, 2], [3, 2]]
        int[] bandage = {1, 1, 1};
        int health = 5;
        int[][] attacks = {{1, 2}, {3, 2}};

        int answer = s.solution(bandage, health, attacks);
        System.out.println("answer = " + answer);

        bw.write("answer = " + String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}
