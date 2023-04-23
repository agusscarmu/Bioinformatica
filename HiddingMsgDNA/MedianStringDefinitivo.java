package HiddingMsgDNA;

import java.util.Arrays;
import java.util.List;

public class MedianStringDefinitivo {
    
    public static void main(String[] args) {
        int k = 6;
        List<String> dnaStrings = Arrays.asList("GCCCGGAGCAACCCGGGGTGTGCATGACGCCACTTGACATAC",
                                                "GATGACAGACGCGCGGGGATCGTTAAGTTTCTGACAAGTCCC",
                                                "TGTTCCCTCTCAGGTTAGTTGTTCCGACGCTTGGGGGCTGCG",
                                                "ATTAGTAGACGCATGTGCACTAGCTAGAGGGACATCCCCCCA",
                                                "AATTGCTGACGCAGTTGCAGCATTCCGAGTACATATGGTTCA",
                                                "GGACGCATGGTGTCTCGTCAAGGGAAAAGTTAAAAGTCTTTT",
                                                "TTGTAAAGACGCCAGTTTGGAGTATCAGCGTCTAAAAGTACC",
                                                "CCGGATTGGATGAGGGCTACGGGTTGACGCATATAATCGTGA",
                                                "TGACGCCATCGGGTAGGAGAACGGGTCACGCGTCTAATTATA",
                                                "CAAATGGGACGCTCCGAAACACTCATGCGTGAGCAACTTGCG");
        String median = medianString(dnaStrings, k);
        System.out.println(median);
    }
    

    public static String medianString(List<String> dnaStrings, int k) {
        String median = null;
        int minDistance = Integer.MAX_VALUE;
        for (int i = 0; i < Math.pow(4, k); i++) {
            String kmer = numberToPattern(i, k);
            int distance = 0;
            for (String dna : dnaStrings) {
                distance += distance(dna, kmer);
            }
            if (distance < minDistance) {
                minDistance = distance;
                median = kmer;
            }
        }
        return median;
    }
    
    public static int distance(String dna, String kmer) {
        int minDistance = Integer.MAX_VALUE;
        for (int i = 0; i <= dna.length() - kmer.length(); i++) {
            int dist = HammingDistance(dna.substring(i, i + kmer.length()), kmer);
            if (dist < minDistance) {
                minDistance = dist;
            }
        }
        return minDistance;
    }
    
    public static String numberToPattern(int number, int k) {
        StringBuilder pattern = new StringBuilder();
        for (int i = 0; i < k; i++) {
            int digit = number % 4;
            switch (digit) {
                case 0:
                    pattern.append('A');
                    break;
                case 1:
                    pattern.append('C');
                    break;
                case 2:
                    pattern.append('G');
                    break;
                case 3:
                    pattern.append('T');
                    break;
            }
            number = number / 4;
        }
        return pattern.reverse().toString();
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
