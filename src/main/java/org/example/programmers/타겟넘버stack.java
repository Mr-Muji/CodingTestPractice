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
 * <> 는 제네릭. 저장할 데이터의 타입을 지정.
 * () 는 생성자(Constructor) 호출을 의미함.
 * stack.push(new int[]{0, 0});
 * -> 자바는 배열 생성 시 반드시 new 를 사용하거나, 선언과 동시에 초기화해야 함.
 * */

public class 타겟넘버stack {

    public int solution(int[] numbers, int target) {
        int answer = 0;

        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{0, 0});

        int index = 0;
        int sum = 0;
        int[] a; //배열을 가리킬 수 있는 참조 변수 선언(아직 메모리에 배열 없음)
                //따라서 초기화도 안 된 상태. 배열도 아님. 그냥 참조 변수임

        while (!stack.isEmpty()) {
            a = stack.pop();
            index = a[0];
            sum = a[1];

            if (index == numbers.length) {

                if (sum == target) {
                    answer++;
                }
            } else {
                stack.push(new int[]{index+1, sum + numbers[index]});
                stack.push(new int[]{index+1, sum - numbers[index]});
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        //int[] numbers = {4, 1, 2, 1};
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;

        타겟넘버stack solution = new 타겟넘버stack();
        System.out.println(solution.solution(numbers, target)); // 결과 출력
    }
}

