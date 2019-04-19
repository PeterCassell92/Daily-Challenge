

class daily7b {

    public static void main(String args[]) {
        String message1 = "11111111";
        int n1=message1.length();
        Integer[] ways1=new Integer[n1+1];
        int res1 = solution(message1,n1,ways1);
        System.out.println(message1 +" has " +res1 + " possible unique decodes.");

        String message2 = "2232";
        int n2=message2.length();
        Integer[] ways2=new Integer[n2+1];
        int res2 = solution(message2,n2,ways2);
        System.out.println(message2 +" has " +res2 + " possible unique decodes.");

        String message3 = "21312";
        int n3=message3.length();
        Integer[] ways3=new Integer[n3+1];
        int res3 = solution(message3,n3,ways3);
        System.out.println(message3 +" has " +res3 + " possible unique decodes.");

        String message4 = "2010213262110";
        int n4=message4.length();
        Integer[] ways4=new Integer[n4+1];
        int res4 = solution(message4,n4,ways4);
        System.out.println(message4 +" has " +res4 + " possible unique decodes.");

        

    }

    private static int solution(String message,int k,Integer[] ways) {
        int n=message.length();
        if(k==0)
        {
            return 1;
        }
        if(message.charAt(n-k)=='0')
        {
            return 0;
        }

        if(ways[k]!=null)
        {
            //System.out.println(k+" : " +ways[k]);
            return ways[k];
        }

        ways[k]=solution(message,k-1,ways);

        if(k>=2 && Integer.valueOf(message.substring(n-k,n-k+2))<27)
            ways[k]+=solution(message,k-2,ways);
        return ways[k];

    }

}