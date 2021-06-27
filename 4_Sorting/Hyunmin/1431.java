import java.util.*;
import java.io.*;

class 1431 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        List<Node> list = new ArrayList<>();

        for (int i = 0; i < n; i++)
            list.add(new Node(br.readLine()));

        Collections.sort(list);

        for(Node temp: list)
            bw.write(temp.getSerial()+"\n");

        bw.flush();
        bw.close();
        br.close();
    }
}

class Node implements Comparable<Node> {
    String Serial;

    Node(String Serial){
        this.Serial = Serial;
    }
    @Override
    public int compareTo(Node o) {
        //1.
        if(this.Serial.length()!=o.Serial.length()) {
            return this.Serial.length()-o.Serial.length();
        }
				//2.
        else {
            int aNum = 0;
            int bNum = 0;
            for (int i = 0; i < this.Serial.length(); i++) {
                if(Character.isDigit(this.Serial.charAt(i)))
                    aNum += Character.getNumericValue(this.Serial.charAt(i));
                if(Character.isDigit(o.Serial.charAt(i)))
                    bNum += Character.getNumericValue(o.Serial.charAt(i));
            }
            if(aNum!=bNum) {
                return Integer.compare(aNum, bNum);
            }
        }
        //3.
        int aDic = 0;
        int bDic = 0;
        for (int i = 0; i < this.Serial.length(); i++) {
            aDic = this.Serial.charAt(i);
            bDic = o.Serial.charAt(i);
            if(aDic!=bDic)
                break;
        }
        return Integer.compare(aDic, bDic);
    }
    public String getSerial() {
        return this.Serial;
    }
}
