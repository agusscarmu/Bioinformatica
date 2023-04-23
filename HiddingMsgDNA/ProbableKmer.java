package HiddingMsgDNA;

import java.util.HashMap;

public class ProbableKmer {
    


    public static void main (String[]args){
        // Crear el diccionario
        HashMap<Character, double[]> profile = new HashMap<Character, double[]>();
        String adn="TCAAGATACTGTTTTCCGCCTGGTCATAAAATGCAGATTCACCCCACTCGATGAAAGTAGCTCGGGATGACTTCCCGACGATACATATCGACTCAGACCCTGGAAATTGGTTCGCATACCATGCACCTATGGTTGTTCCACCGGGTGTCTGTATTATCTATTCTTGCCTAAAGTCGTTTCCCAAGATCAGACTACGTATCTGCAAGCAAAGCACGTTCTAACAGCTCATAACGGCGCTGTTATCTAACGCGCTGCCGATTCAGATGCGACATCACATCCTAAAACTTAGGCGTGCCTATACAGGCGCTATCTTATGTCGGGTGTCAAGTTTTATAGTGTTGAATTCCCGATTGCAACTAACCGGTGAAAGGGCGGGAACCTCCCTCTATTGTCTTCCCAGGCTACGTGGCCTCCCGGACGTGTTTGCGTCTTCACTGAGTGATCTAGACAGTTCGGAAATGGCGTGTCCGGTAGTTGCGACGGACACAATTGTCCACCGTCAGGAAGTTGAAGGTTATAACGGCCGGTCTTCGGGGCGCGCTTGTCAGCTAGCTAGTTAAGCGTTATGCGACGTAGTTCCCAAGGAGGTTTCGGACCGGCATTTTGCTACTGCACCCCCACGCGACTTCCGGCAGCCAGTCGTTGGCCTGGGTATGCAATAAGTGTTGTAGGTGAGATCCTGAACGAGTCTGTATCTGCAACCTCAGATATATCACCCGAACCTTGAGGTAAATTCAATCGTATCCCTTATCCCAACGAGTGATCGGCGTAGGGACCAAATCCATTACGCGAAATTTTTAGCAATGGCCATATATCGACATACTTGGAATCACGGATCAACATACTCGTGTGTATTCGTGTGCAGGGGTCCTATTACTTTACCCGGAATTTCCGTGCGAAGCTAAAGACTGGGGAGTAATGCAGCACTGAAAGAGTCTGCGCTCCGACCCAAGGAGGCCCGCCCCGTCTACGGAGTATTTAGCCCTACTATTTCGCAAAA";
        int k = 15;
        // Agregar elementos al diccionario
        profile.put('A', new double[]{0.318, 0.273, 0.182, 0.273, 0.303, 0.273, 0.394, 0.182, 0.258, 0.288, 0.303, 0.182, 0.258, 0.258, 0.273});
        profile.put('C', new double[]{0.273, 0.227, 0.273, 0.197, 0.242, 0.182, 0.182, 0.152, 0.273, 0.303, 0.182, 0.333, 0.197, 0.333, 0.258});
        profile.put('G', new double[]{0.136, 0.288, 0.197, 0.242, 0.212, 0.364, 0.318, 0.394, 0.288, 0.212, 0.227, 0.273, 0.379, 0.212, 0.273});
        profile.put('T', new double[]{0.273, 0.212, 0.348, 0.288, 0.242, 0.182, 0.106, 0.273, 0.182, 0.197, 0.288, 0.212, 0.167, 0.197, 0.197});

        System.out.println(MostProbableKmer(adn, k, profile));
    }


    public static String MostProbableKmer(String adn, int k, HashMap<Character, double[]>profile){
        String kmer="";
        int n= adn.length();
        float bestPr=0;

        for(int i=0;i<n-k+1;i++){
            String pattern = adn.substring(i, i+k);
            float Pr=Pr(pattern, profile);
            if(bestPr<Pr){
                bestPr=Pr;
                kmer=pattern;
            }
        }

        return kmer;
    }

    public static float Pr(String kmer, HashMap<Character, double[]>profile){

        int k=kmer.length();
        float Pr=1;

        for(int i=0;i<k;i++){
            char nucleotido = kmer.charAt(i);
            double[]p=profile.get(nucleotido);
            Pr*=p[i];
        }

        return Pr;
    }

}