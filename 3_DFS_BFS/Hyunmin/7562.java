import java.util.*;
import java.io.*;

class 7562 {
    public static boolean[][] visited;
    public static int max;
    public static int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2};
    public static int[] dy = {-1, -2, -2, -1, 1, 2, 2, 1};
    public static int endX;
    public static int endY;

    public static int bfs(int startX, int startY) {
        Queue<Node> q = new LinkedList<>();

        visited = new boolean[max][max];
        q.offer(new Node(startX, startY, 0));
        if(!visited[startX][startY])
            visited[startX][startY] = true;

        while(!q.isEmpty()) {
            Node poped = q.poll();

            if(poped.x==endX && poped.y==endY)
                return poped.prev;

            for (int i = 0; i < 8; i++) {
                int xX = poped.x + dx[i];
                int yY = poped.y + dy[i];
                if(xX >= 0 && yY >= 0 && xX < max && yY < max) {
                    if(!visited[xX][yY]) {
                        visited[xX][yY] = true;
                        q.offer(new Node(xX, yY, poped.prev + 1));
                    }
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        while(t--> 0) {
            int l = Integer.parseInt(br.readLine());

            max = l;

            st = new StringTokenizer(br.readLine(), " ");
            int startX = Integer.parseInt(st.nextToken());
            int startY = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine(), " ");
            endX = Integer.parseInt(st.nextToken());
            endY = Integer.parseInt(st.nextToken());
            sb.append(bfs(startX, startY)).append("\n");
        }

        br.close();
        bw.write(sb.toString()+"\n");
        bw.flush();
        bw.close();
    }
}
class Node {
    int x;
    int y;
    int prev;
    Node(int x, int y, int prev) {
        this.x = x;
        this.y = y;
        this.prev = prev;
    }
}




