
import java.util.*;
import java.io.*;

class Main {
    private static int bottomUp(int x, int[] input) {
        int[] dpTable = new int[x];
        dpTable[0] = input[0];
        dpTable[1] = Math.max(input[0], input[1]);

        for (int i = 2; i < x; i++) {
            //이전꺼 vs 이이전꺼 + 현재(한칸 떨어져있기 때문에 현재꺼를 추가해서 비교해줘야 함)
            dpTable[i] = Math.max(dpTable[i-1], dpTable[i-2] + input[i]);
        }

        return dpTable[x-1];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int x = Integer.parseInt(br.readLine());
        int[] input = new int[x];
        st = new StringTokenizer(br.readLine(), " ");
        int i = 0;
        while(st.hasMoreTokens())
            input[i++] = Integer.parseInt(st.nextToken());


        bw.write(String.valueOf(bottomUp(x, input)));

        bw.flush();
        bw.close();
        br.close();
    }
}

