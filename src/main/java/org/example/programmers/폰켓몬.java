package org.example.programmers;

import java.io.*;
import java.util.*;

//해시 문제
//hashmap, hashset, linkedhashmap 뭐쓸지 판단
// -> 여기서는 hashset 사용해야 했을듯. set은 중복된 값을 허용하지 않으므로, set에 그냥 다 넣어주면 됨.

// HashMap 선언할 때 int 가 아니고 <Integer, Integer> 이다. 명심

public class 폰켓몬 {
    public int solution(int[] nums) {
        int answer = 0;

        //아래는 hashmap 이용.

//        HashMap<Integer, Integer> map = new HashMap<>();
//        for (int num : nums) {
//            map.put(num, 0);
//        }
//
//
//        int cnt = 0;
//        for (int key : map.keySet()) {
//            cnt++;
//        }
//
//        //이렇게도 가능할듯
//        //answer = Integer.min(nums.length, cnt);
//        answer = (nums.length / 2 <= cnt) ? nums.length / 2 : cnt;

        //이건 hashset 이용

        HashSet<Integer> set = new HashSet<>();
        for(int num: nums){
            set.add(num);
        }

        answer = Integer.min(nums.length/2, set.size());

        return answer;
    }

    public static void main(String[] args) {
        int[] nums = {3, 1, 2, 3};
        int[] nums2 = {3,3,3,2,2,4};
        int[] nums3 = {3,3,3,2,2,2};

        폰켓몬 s = new 폰켓몬();
        System.out.println(s.solution(nums3));
    }
}


