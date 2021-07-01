import java.io.*;
import java.util.*;

class Edge implements Comparable<Edge> {

    private double distance;
    private SubEdge nodeA;
    private SubEdge nodeB;

    public Edge(double distance, SubEdge nodeA, SubEdge nodeB) {

        this.distance = distance;
        this.nodeA = nodeA;
        this.nodeB = nodeB;
    }

    public double getDistance() {
        return this.distance;
    }

    public SubEdge getNodeA() {
        return this.nodeA;
    }

    public SubEdge getNodeB() {
        return this.nodeB;
    }

    // 거리(비용)가 짧은 것이 높은 우선순위를 가지도록 설정
    @Override
    public int compareTo(Edge other) {
        if (this.distance < other.distance) {
            return -1;
        }
        return 1;
    }
}

class SubEdge {
    public int idx;
    public double x;
    public double y;
    SubEdge (int idx, double x, double y) {
        this.idx = idx;
        this.x = x;
        this.y = y;
    }
    public int getIdx() {
        return this.idx;
    }
}

public class Main {

    // 노드의 개수(V)와 간선(Union 연산)의 개수(E)
    // 노드의 개수는 최대 100,000개라고 가정
    public static int v, e;
    public static int[] parent = new int[100001]; // 부모 테이블 초기화하기
    // 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
    public static ArrayList<Edge> edges = new ArrayList<>();
    public static ArrayList<SubEdge> subEdges = new ArrayList<>();
    public static double result = 0;

    // 특정 원소가 속한 집합을 찾기
    public static int findParent(int x) {
        // 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if (x == parent[x]) return x;
        return parent[x] = findParent(parent[x]);
    }

    // 두 원소가 속한 집합을 합치기
    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        Scanner sc = new Scanner(System.in);

        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());


        // 부모 테이블상에서, 부모를 자기 자신으로 초기화
        for (int i = 1; i <= v; i++) {
            parent[i] = i;
        }

        // 모든 좌표에 대한 정보를 입력 받기
        subEdges.add(new SubEdge(0, 0, 0)); // 0번째에 더미 추가
        for (int i = 1; i <= v; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            subEdges.add(new SubEdge(i, a, b));
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            double cost = Math.sqrt(Math.pow(subEdges.get(a).x - subEdges.get(b).x,2) + Math.pow(subEdges.get(a).y - subEdges.get(b).y,2));

            // 처음 아이디어는 비용 계산 후 이미 연결된 총 비용을 뺴는 식으로 생각
            // -> 그렇게 엣지에 넣지 않고 연결만 해놓는 방법 ?
            // 이미 연결되어 있으면 검사를 안하기 때문에, 미리 연결을 해놓는 방법을 생각해야 됨
            unionParent(a, b); // a 와 b는 subEdge 의 idx 임. 이것으로 연결 완료
        }

        for (int i = 1; i <= v; i++) {
            for (int j = 1; j <= v && j!=i; j++) {
                SubEdge a = subEdges.get(i);
                SubEdge b = subEdges.get(j);
                double cost = Math.sqrt(Math.pow(a.x-b.x, 2) + Math.pow(a.y-b.y, 2));
                edges.add(new Edge(cost, a, b));
            }
        }

        // 간선을 비용순으로 정렬
        Collections.sort(edges);

        // 간선을 하나씩 확인하며
        for (int i = 0; i < edges.size(); i++) {
            double cost = edges.get(i).getDistance();
            int a = edges.get(i).getNodeA().getIdx();
            int b = edges.get(i).getNodeB().getIdx();
            // 사이클이 발생하지 않는 경우에만 집합에 포함
            if (findParent(a) != findParent(b)) {
                unionParent(a, b);
                result += cost;
            }
        }

        bw.write(String.format("%.2f", result));
        br.close();
        bw.flush();
        bw.close();
        br.close();
    }
}
