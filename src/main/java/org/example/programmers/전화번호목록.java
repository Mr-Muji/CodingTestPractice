package org.example.programmers;

import java.util.*;

public class 전화번호목록 {
    public boolean solution(String[] phone_book) {
        boolean answer = true;

        //해시 안 써?
        //-> 효율성 테스트 탈락. 시간초과됨.
        //Arrays.sort(phone_book, (s1, s2) -> Integer.compare(s1.length(), s2.length()));
//        for (int i = 0; i < phone_book.length; i++) {
//            for (int j = i + 1; j < phone_book.length; j++) {
//                if (Objects.equals(phone_book[i], phone_book[j].substring(0, phone_book[i].length()))) {
//                    answer = false;
//                    break;
//                }
//            }
//        }

        HashSet<String> set = new HashSet<>(Arrays.asList(phone_book));

        for(String str : phone_book){
            for(int i = 1; i< str.length(); i++){
                String prefix = str.substring(0, i);
                if(set.contains(prefix)){
                    answer = false;
                    break;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        전화번호목록 s = new 전화번호목록();
        String[] s1 = {"119", "97674223", "1195524421"};
        String[] s2 = {"123", "456", "789"};
        String[] s3 = {"12", "123", "1235", "567", "88"};

        System.out.println(s.solution(s2));
    }
}
