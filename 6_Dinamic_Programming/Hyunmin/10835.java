import java.util.*;
import java.io.*;

class 10835 {
    public static int cardNum;

    public static int[] left;
    public static int[] right;

    public static int[][] dp;
    public static int topDown(int l, int r) {
        //dp[cards[0][l]][cards[1][r]]에 값을 넣어야 한다고 추상적으로 생각했으나, dp[l][r]도 가능하고 더 효율적인 것 같다.
        if(l >= cardNum || r >= cardNum ) 
            return 0;
        //dp 배열 초기값이 0이라면 이미 계산해서 나온 0이어도 아직 계산 안했다고 생각해서 시간초과 발생
        //if(dp[cards[0][l]][cards[1][r]]!=0) //0인지 검사 시 틀린다. 
        //=> 
        if(dp[l][r]!=-1)
            return dp[l][r];
        //dp에 저장할 데이터 => point
        //1. 언제든지 왼쪽 카드만 통에 버릴 수도 있고 왼쪽 카드와 오른쪽 카드를 둘 다 통에 버릴 수도 있다. 이때 얻는 점수는 없다.
        dp[l][r] = Math.max(dp[l][r], topDown(l+1, r)); //L+1이 왼쪽카드를 통에 버리는 행위임
        dp[l][r] = Math.max(dp[l][r], topDown(l+1, r+1));//양쪽 버림

        //2. 오른쪽 카드에 적힌 수가 왼쪽 카드에 적힌 수보다 작은 경우에는 오른쪽 카드만 통에 버릴 수도 있다.
        //오른쪽 카드만 버리는 경우에는 오른쪽 카드에 적힌 수만큼 점수를 얻는다.
        if(left[l] > right[r]) 
            dp[l][r] = Math.max(dp[l][r] , topDown(l, r+1) + right[r]);

        //3. (1)과 (2)의 규칙에 따라 게임을 진행하다가 어느 쪽 더미든 남은 카드가 없다면 게임이 끝나며 그때까지 얻은 점수의 합이 최종 점수가 된다.
        return dp[l][r];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        cardNum = Integer.parseInt(br.readLine());
        //cards = new int[cardNum][cardNum];
        //=> cardNum으로 Left랑Right를 만들면 ArrayIndexOutOfBounds에러가 뜬다.
        dp = new int[2100][2100];

        //dp 배열 초기값이 0이라면 이미 계산해서 나온 0이어도 아직 계산 안했다고 생각해서 시간초과 발생
        //=> -1로 초기화 => 이중반복문 X => 향상된 for 문 + 2차원 배열 Arrays.fill
        for (int[] arr : dp)
            Arrays.fill(arr, -1);

        st = new StringTokenizer(br.readLine(), " ");
        left = new int[st.countTokens()];
        for (int i = 0; st.hasMoreTokens(); i++)
            left[i] = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        right = new int[st.countTokens()];
        for (int i = 0; st.hasMoreTokens(); i++)
            right[i] = Integer.parseInt(st.nextToken());
        
        bw.write(String.valueOf(topDown(0, 0)));
        bw.flush();
        bw.close();
        br.close();
    }
}

