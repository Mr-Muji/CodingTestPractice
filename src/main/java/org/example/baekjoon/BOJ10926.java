package org.example.baekjoon;

import java.io.*;

/*
* BufferdReader 쓰려면 반드시 예외처리 해줘야함.
*
* */

public class BOJ10926 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write(s + "??!");
        bw.flush();
        bw.close();

    }
}
