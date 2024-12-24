package org.example.baekjoon;

import java.io.*;
import java.util.*;

/*
double을 사용해야 함. double result = (double)a/b; 해야 값이 0이 나오지 않음.
long 은 정수형임

* */

public class BOJ1008 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        StringTokenizer st = new StringTokenizer(s);

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        double result = (double)a / b;

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}
