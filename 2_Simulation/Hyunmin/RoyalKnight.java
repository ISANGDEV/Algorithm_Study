public class RoyalKnight {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution("a1"));
        System.out.println(sol.solution("c2"));
    }
}

class Solution {
    public int solution(String place) {
        int answer = 0;
        int[][] arr = {{-2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}};

        int i = place.charAt(0) - 96;
        int j = place.charAt(1) - 48;

        for (int x = 0; x < 8; x++) {
            if (i + arr[x][0] > 0 && i + arr[x][0] < 9) {
                if (j + arr[x][1] > 0 && j + arr[x][1] < 9) {
                    answer++;
                }
            }
        }        
        return answer;
    }
}
