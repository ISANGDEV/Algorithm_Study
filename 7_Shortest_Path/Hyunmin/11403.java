import java.io.*;
import java.util.*;

public class 11403 {

    public static int n;
    public static int[][] graph = new int[101][101];

    public static void main(String[] args) throws IOException {
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; st.hasMoreTokens(); j++)
                graph[i][j] = Integer.parseInt(st.nextToken());
        }

        for (int k = 0; k < n; k++) {
            for (int a = 0; a < n; a++) {
                for (int b = 0; b < n; b++) {
                    if(graph[a][b] == 0 && graph[a][k]==1 && graph[k][b]==1)
                        graph[a][b] = 1;
                }
            }
        }

        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++)
                bw.write(String.valueOf(graph[a][b]) + " ");
            bw.write("\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
