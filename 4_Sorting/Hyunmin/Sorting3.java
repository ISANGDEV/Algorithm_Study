
import java.util.*;
import java.io.*;

class Sorting3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        List<Node> list = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());

        String name;
        int score;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");

            name = st.nextToken();
            score = Integer.parseInt(st.nextToken());
            list.add(new Node(name, score));
        }

        Collections.sort(list);

        for(Node temp: list) 
            bw.write(temp.getName() + " ");

        bw.flush();
        bw.close();
        br.close();
    }
}

class Node implements Comparable<Node>{
    String name;
    int score;

    Node(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return this.name;
    }

    @Override
    public int compareTo(Node o) {
        return Integer.compare(this.score, o.score);
    }
}
