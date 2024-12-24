package org.example.baekjoon;

import java.io.*;
import java.util.StringTokenizer;

//TIP 코드를 <b>실행</b>하려면 <shortcut actionId="Run"/>을(를) 누르거나
// 에디터 여백에 있는 <icon src="AllIcons.Actions.Execute"/> 아이콘을 클릭하세요.
public class BOJ1000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));

        String s = br.readLine();

        StringTokenizer st = new StringTokenizer(s);

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int result = a + b;

        bw.write("result : " + result + "\n");
        bw.flush();
        bw.close();

    }
}