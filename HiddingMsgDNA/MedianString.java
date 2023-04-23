package HiddingMsgDNA;

public class MedianString {
    
    public static void main(String []args){
        // String [] dna = {"TAGAGAAGATGACTTTGTGGCGCCATGAACGTATTGCGTAGA", 
        // "GGCGCATGCTGTAAGTTTGAGATCCCTTGTCTGAAAGACCGT", 
        // "TTCAACACTTATGGCGCGGTCGTAATTACTAGCCGTTTATAA", 
        // "TGGATCTTGCGGACCTTGTTTCTTGCAGGGGGCGCGCGTAGC", 
        // "AAACGGCAATGAAGATATGCGACTGGCGCGTACATGGTACAT",
        // "TGTGGAAAATCACACCCATATTACGAACAAGGCGCGTTACAT",
        // "TATTTTGGCTCAGTTAAGGGCGCGGTGGCGGGTCGGGTTATA",
        // "GGCGCCAGAATGAGACGATCGATCAATATTCACTCACAAGCT",
        // "AACGCTGCTGCTGCGCTTGGCGCTCAATCCTCCTACTGTATC",
        // "ACTAATAGCCGCCTAAGAGGCGCGGAAGCGCCGAGACTCCAG"};
        String [] dna = {"AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTTCGGGACAG"};
        int k = 3;
        System.out.println(medianString(dna, k));
    }

    public static String medianString(String[]Dna, int k){
        String median="";
        int n=Dna[0].length();
        int distance = Integer.MAX_VALUE;

        for(int j=0;j<Dna.length;j++){
            for(int i=0;i<n-k;i++){
                String pattern=Dna[j].substring(i, i+k);
                int d=d(pattern,Dna);
                if(distance>d){
                    distance=d;
                    median=pattern;
                }
            }
        }
        return median;
    }

    public static int d(String pattern, String[]adn){
        int d=0;
        int k=pattern.length();

        for(String text:adn){
            for(int i=0;i<text.length()-k;i++){
                String p=text.substring(i, i+k);
                d+=HammingDistance(pattern,p);
            }
        }

        return d;
    }

    public static int HammingDistance(String pattern, String pattern2){
        int hammingDistance=0;

        for(int i=0;i<pattern.length();i++){
            if(pattern.charAt(i)!=pattern2.charAt(i)){
                hammingDistance++;
            }
        }

        return hammingDistance;
    }
}
