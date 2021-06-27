import java.util.*;
import java.io.*;

class Sorting4 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        while(st.hasMoreTokens())
            a.add(Integer.parseInt(st.nextToken()));

        st = new StringTokenizer(br.readLine());
        while(st.hasMoreTokens())
            b.add(Integer.parseInt(st.nextToken()));

        Collections.sort(a);
        Collections.sort(b, Collections.reverseOrder());

        //7 8 9 10
        //5 5 5 4
        for (int i = 0; i < k; i++) {
            if(a.get(i) < b.get(i))
                a.set(i, b.get(i));
        }

        int total = 0;
        for(int temp: a)
            total += temp;

        bw.write(String.valueOf(total));

        bw.flush();
        bw.close();
        br.close();
    }
}
