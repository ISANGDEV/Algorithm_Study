import java.util.*;
import java.io.*;

class 4963 {
    public static int[][] map;
    public static int hMax;
    public static int wMax;

    public static boolean dfs(int h, int w) {
        if(h < 0 || w < 0 || h >= hMax || w >= wMax)
            return false;

        if(map[h][w]==1) {
            map[h][w] = 0;
            //북
            dfs(h-1, w);
            //북서
            dfs(h-1, w-1);
            //서
            dfs(h, w-1);
            //남서
            dfs(h+1, w-1);
            //남
            dfs(h+1, w);
            //남동
            dfs(h+1, w+1);
            //동
            dfs(h, w+1);
            //북동
            dfs(h-1, w+1);

            return true;
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        List<Integer> answer = new LinkedList<>();

        while(true) {
            st = new StringTokenizer(br.readLine(), " ");
            int w = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            if(w == 0 && h == 0)
                break;

            map = new int[h][w];
            hMax = h;
            wMax = w;

            int count = 0;
            for (int i = 0; i < h; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                for (int j = 0; j < w; j++)
                    map[i][j] = Integer.parseInt(st.nextToken());
            }

            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if(dfs(i, j))
                        count++;
                }
            }
            answer.add(count);
        }
        br.close();
        for (int temp : answer)
            bw.write(temp+"\n");
        bw.flush();
        bw.close();
    }
}




