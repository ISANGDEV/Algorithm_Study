import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> list = new ArrayList<>();

        int n,m,k,result = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        //n, m, k 한 줄에 입력
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        //배열 크기 n만큼 생성 후 입력
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        while(st2.hasMoreTokens()) {
            list.add(Integer.parseInt(st2.nextToken()));
        }

        Collections.sort(list, Collections.reverseOrder());

        result = m/(k+1) * (k*list.get(0) + list.get(1)) + m%(k+1)*list.get(0);

        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
        br.close();

    }
}

