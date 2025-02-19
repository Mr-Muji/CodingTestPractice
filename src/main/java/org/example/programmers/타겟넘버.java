package org.example.programmers;

import java.util.Arrays;

/*
 * https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=java
 *
 * 그냥 dps 에 대한 이해만 있으면 간단하게 풀 수 있는 문제다.
 * 1. numbers 배열의 길이만큼 반복하면서
 * 2. dfs 함수를 호출한다.
 * 3. dfs 함수는 numbers 배열의 길이만큼 반복하면서
 * 4. sum + numbers[index] 와 sum - numbers[index] 의 값을 리턴한다.
 * 5. index 가 numbers 배열의 길이와 같아지면 sum 이 target 과 같은지 확인한다.
 *  5-1. 같다면 1을 리턴한다.
 *  5-2. 다르다면 0을 리턴한다.
 * 6. dfs 함수의 리턴값을 answer 에 더해준다.
 * 7. answer 를 리턴한다.
 * 8. 끝
 *
 * */
public class 타겟넘버 {
    public int solution(int[] numbers, int target) {
        int answer = 0;

        answer = dfs(numbers, target, 0, 0);

        return answer;
    }

    public int dfs(int[] numbers, int target, int result, int index) {
        if (numbers.length == index) {
            if (target == result) {
                return 1;
            }
            return 0;
        }
        return (
                dfs(numbers, target, result + numbers[index], index + 1) +
                        dfs(numbers, target, result - numbers[index], index + 1)
        );
    }


    public static void main(String[] args) {
        //int[] numbers = {1, 1, 1, 1, 1};
        int[] numbers = {4, 1, 2, 1};
        int target = 4;
        타겟넘버 s = new 타겟넘버();

        System.out.println(s.solution(numbers, target));
    }
}
