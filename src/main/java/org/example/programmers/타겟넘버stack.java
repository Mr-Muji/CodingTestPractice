package org.example.programmers;

import java.util.Stack;

/*
 * https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=java
 *
 * 재귀 말고 스택으로 구현해 보았다.
 * 1. 스택에 [현재 인덱스, 누적 합] 형태로 저장
 * 2. 초기 상태: 인덱스 0, 누적합 0
 * 3. 스택이 빌 때까지 반복
 * 4. 스택에서 pop
 * 5. 인덱스와 누적합을 가져온다.
 * 6. 모든 숫자를 다 사용한 경우, 누적합이 목표값과 같으면 경우의 수 +1
 * 7. 다음 인덱스로 이동하며 +, - 연산을 모두 넣어준다.
 *
 *
 * */

public class 타겟넘버stack {

    public int solution(int[] numbers, int target) {
        int answer = 0;

        // 스택에 [현재 인덱스, 누적 합] 형태로 저장
        Stack<int[]> stack = new Stack<>();
        // 초기 상태: 인덱스 0, 누적합 0
        stack.push(new int[]{0, 0});

        // 스택이 빌 때까지 반복
        while (!stack.isEmpty()) {
            int[] current = stack.pop();
            int index = current[0];
            int sum = current[1];

            // 모든 숫자를 다 사용한 경우
            if (index == numbers.length) {
                // 목표값과 같으면 경우의 수 +1
                if (sum == target) {
                    answer++;
                }
            } else {
                // 다음 인덱스로 이동하며 +, - 연산을 모두 넣어준다.
                stack.push(new int[]{index + 1, sum + numbers[index]});
                stack.push(new int[]{index + 1, sum - numbers[index]});
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] numbers = {4, 1, 2, 1};
        int target = 4;

        타겟넘버stack solution = new 타겟넘버stack();
        System.out.println(solution.solution(numbers, target)); // 결과 출력
    }
}

