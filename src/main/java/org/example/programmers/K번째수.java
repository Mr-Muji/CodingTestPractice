package org.example.programmers;

import java.util.*;

//Lv.1

//ArrayList 사용. 정렬 시 Collections.sort()
//subList 사용 시 범위에 주의
//Array 출력 시 Arrays.toString() 사용
//Array 정렬 시 Arrays.sort()

public class K번째수 {
    public int[] solution(int[] array, int[][] commands) {

        int[] answer = new int[commands.length];

//        ArrayList<Integer> list = new ArrayList<>();
//        for (int num : array) {
//            list.add(num);
//        }
//        for (int i = 0; i < commands.length; i++) {
//            List<Integer> subList;
//            subList = list.subList(commands[i][0] - 1, commands[i][1]);
//            Collections.sort(subList);
//            answer[i] = subList.get(commands[i][2] - 1);
//        }

        for(int i = 0; i < commands.length; i++){
            int[] subArray = Arrays.copyOfRange(array, commands[i][0] -1, commands[i][1]);
            Arrays.sort(subArray);

            answer[i] = subArray[commands[i][2]-1];
        }

        return answer;
    }

    public static void main(String[] args) {
        K번째수 sol = new K번째수();

        //[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
        int[] array = {1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

        System.out.println(Arrays.toString(sol.solution(array, commands)));
    }
}
